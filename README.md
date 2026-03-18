# 🎵 Spotify Track Analysis — Real-World Data Storytelling

> CIS 4930 — Introduction to Python | Spring 2026 | Group 04 | Project01

---

## Group Members

| Name           | FSU ID        |
|----------------|---------------|
| Thomas Schmidt | tns23@fsu.edu |
| Rafik Taleb    | rt24e@fsu.edu |
| Imran Ahmed    | ia24c@fsu.edu |
| Dhruv Upadhyay | dtu24@fsu.edu |

---

## Project Description

This project analyzes a real-world Spotify tracks dataset to explore what
makes songs popular across different genres and time periods. Using Python,
pandas, NumPy, and seaborn/matplotlib, we perform exploratory data analysis
(EDA) to uncover patterns in audio features like danceability, energy,
tempo, and loudness — and how they relate to a track's popularity score.

**Dataset source:**
[Spotify Tracks Dataset — Kaggle](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)

The dataset contains ~114,000 tracks with 4+ numeric columns (popularity,
danceability, energy, tempo, loudness, valence) and 2+ categorical columns
(track_genre, explicit) — satisfying all project dataset requirements.

---

## Research Questions

1. **What audio features are most strongly correlated with a track's popularity?**
2. **Which genres have the highest average energy and danceability?**
3. **How has the distribution of song tempo changed over release years?**
4. **Do explicit tracks tend to score higher in popularity than non-explicit ones?**
5. **Is there a relationship between loudness and energy across different genres?**

---

## 📁 Repository Structure

```
cis4930-sp26-project-group-XX/
│
├── data/
│   ├── raw/                  # Original unmodified dataset
│   │   └── spotify_tracks.csv
│   └── processed/            # Cleaned and transformed data exports
│       └── spotify_cleaned.csv
│
├── figures/                  # Exported plots (PNG, dpi=300)
│   ├── popularity_by_genre.png
│   ├── energy_danceability_scatter.png
│   ├── tempo_distribution.png
│   └── correlation_heatmap.png
│
├── notebooks/
│   └── analysis.ipynb        # Main Jupyter notebook
│
├── .gitignore                # Python gitignore
└── README.md                 # This file
```

---

##  Tools & Libraries

- Python 3.x
- pandas
- NumPy
- matplotlib
- seaborn
- Jupyter Notebook

---

## Notebook Structure

The main analysis notebook (`notebooks/analysis.ipynb`) is organized into
the following sections:

1. **Data Loading and Initial Inspection**
   - Load CSV with `pd.read_csv()`
   - `.info()`, `.describe()`, `.shape`

2. **Cleaning and Transformation**
   - Handle missing values (drop + fill strategies)
   - Type conversions (`pd.to_numeric`, `pd.to_datetime`)
   - Derive new columns with `np.where` and `.apply`

3. **Descriptive Statistics and EDA**
   - `.mean()`, `.median()`, `.std()` on key numeric columns
   - Grouped stats by genre and explicit flag
   - Correlation matrix

4. **Visualizations and Feature Exploration**
   - Line plot — popularity trend over release years
   - Bar plot — average energy by genre
   - Histogram — distribution of danceability
   - Scatter plot — energy vs. loudness
   - Heatmap — correlation matrix

5. **Summary and Key Findings**
   - Plain-English interpretations of results
   - Answers to research questions

---

## ✅ Dataset Requirements Checklist

- [x] Real-world dataset (not a built-in toy dataset)
- [x] CSV format
- [x] ~114,000 rows (within 500–50,000 range after sampling if needed)
- [x] 4+ numeric columns: popularity, danceability, energy, tempo, loudness, valence
- [x] 2+ categorical columns: track_genre, explicit
- [x] Clear real-world context and research questions

---

## Collaboration

Work is split among all four group members. See commit history for
individual contributions.

Branches used: `data-cleaning`, `eda`, `viz`, `docs`
