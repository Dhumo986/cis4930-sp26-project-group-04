from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Track(models.Model):
    SOURCE_CHOICES = [
        ('csv', 'CSV Import'),
        ('api', 'API Fetch'),
    ]

    track_id = models.CharField(max_length=100, unique=True)
    track_name = models.CharField(max_length=255)
    artists = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='tracks')
    popularity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    danceability = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    energy = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    tempo = models.FloatField()
    loudness = models.FloatField()
    valence = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    duration_ms = models.IntegerField()
    explicit = models.BooleanField(default=False)
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES, default='csv')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.track_name} — {self.artists}"

    class Meta:
        ordering = ['-popularity']
        indexes = [
            models.Index(fields=['genre']),
            models.Index(fields=['popularity']),
        ]


class DataRun(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ]

    triggered_at = models.DateTimeField(auto_now_add=True)
    records_fetched = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"DataRun [{self.status}] @ {self.triggered_at:%Y-%m-%d %H:%M}"

    class Meta:
        ordering = ['-triggered_at']
