import os
import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from spotifyapp.models import Genre, Track, DataRun


class Command(BaseCommand):
    help = 'Seed the database from the Project 1 Spotify CSV'

    def add_arguments(self, parser):
        parser.add_argument(
            '--limit',
            type=int,
            default=5000,
            help='Max number of rows to load (default: 5000)',
        )

    def handle(self, *args, **options):
        limit = options['limit']
        csv_path = os.path.join(
            os.path.dirname(__file__), '..', '..', '..', 'data', 'raw', 'spotify_tracks.csv'
        )
        csv_path = os.path.abspath(csv_path)

        if not os.path.exists(csv_path):
            self.stderr.write(f'CSV not found at: {csv_path}')
            return

        self.stdout.write(f'Loading CSV from {csv_path} ...')
        df = pd.read_csv(csv_path)
        df = df.dropna(subset=['track_id', 'track_name', 'artists', 'track_genre'])
        df = df.head(limit)

        run = DataRun.objects.create(status='pending')
        count = 0

        try:
            with transaction.atomic():
                for _, row in df.iterrows():
                    genre, _ = Genre.objects.get_or_create(name=row['track_genre'])
                    Track.objects.update_or_create(
                        track_id=str(row['track_id']),
                        defaults={
                            'track_name': str(row['track_name'])[:255],
                            'artists': str(row['artists'])[:255],
                            'genre': genre,
                            'popularity': int(row.get('popularity', 0)),
                            'danceability': float(row.get('danceability', 0.0)),
                            'energy': float(row.get('energy', 0.0)),
                            'tempo': float(row.get('tempo', 0.0)),
                            'loudness': float(row.get('loudness', 0.0)),
                            'valence': float(row.get('valence', 0.0)),
                            'duration_ms': int(row.get('duration_ms', 0)),
                            'explicit': bool(row.get('explicit', False)),
                            'source': 'csv',
                        }
                    )
                    count += 1
                    if count % 500 == 0:
                        self.stdout.write(f'  Loaded {count} tracks...')

            run.status = 'success'
            run.records_fetched = count
            run.save()
            self.stdout.write(self.style.SUCCESS(f'Done! Loaded {count} tracks.'))

        except Exception as e:
            run.status = 'failed'
            run.notes = str(e)
            run.save()
            self.stderr.write(f'Error during seed: {e}')
