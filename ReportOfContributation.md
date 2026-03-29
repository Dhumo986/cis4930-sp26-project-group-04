# Contribution Reports — CIS 4930 Group 04
## Real-World Data Storytelling — Spotify Track Analysis
## Spring 2026

---
---

# Contribution Report — Dhruv Upadhyay
## FSU ID: DTU24

---

## Overview

This document outlines my individual contributions to the
CIS 4930 group project. All work is tracked and visible
in the GitHub repository under the `dhruv-analysis` and
`Question` branches.

---

## Repository Setup

- Created the GitHub repository `cis4930-sp26-project-group-04`
- Set up the full folder structure (`data/raw`, `data/processed`,
  `figures/`, `notebooks/`)
- Wrote the `README.md` with project description, research
  questions, dataset justification, and task checklist
- Added `.gitignore` for Python and Jupyter files
- Uploaded the raw Spotify dataset to `data/raw/`
- Added instructor as collaborator

---

## Notebook Contributions — `notebooks/analysis.ipynb`

### Section 1 — Data Loading and Initial Inspection
- Loaded the Spotify dataset using `pd.read_csv()`
- Sampled down to 50,000 rows using `.sample(n=50000, random_state=42)`
- Ran `.info()`, `.describe()`, `.shape` for initial inspection
- Created a `pd.Series` by hand showing average audio feature values
- Created a `pd.DataFrame` by hand with mean, median, and std
  for all key numeric features
- Checked missing values per column
- Checked unique genres and value counts
- Wrote markdown explanation of findings

### Section 2 — Cleaning and Transformation
- Dropped 3 rows with missing values in artists, album_name, track_name
- Dropped unnecessary `Unnamed: 0` column
- Converted `duration_ms` to `duration_sec` using `pd.to_numeric()`
- Converted `explicit` column from bool to int
- Converted `track_genre` to categorical dtype
- Derived new column `popularity_tier` using `np.where()`
  (high = popularity >= 50, low = popularity < 50)
- Derived new column `tempo_category` using `.apply()`
  (slow / medium / fast based on BPM)
- Filled remaining numeric nulls with median values
- Exported cleaned dataset to `data/processed/spotify_cleaned.csv`
- Wrote markdown explanation of cleaning steps

### Section 3 — Descriptive Statistics and EDA
- Ran `.describe()` on all key numeric columns
- Ran explicit `.mean()`, `.median()`, `.min()`, `.max()`, `.std()`
  on popularity, danceability, and energy
- Computed grouped stats by genre using `groupby().agg()`
- Computed grouped stats by explicit flag
- Computed grouped stats by tempo category
- Used multi-column `groupby(['track_genre', 'tempo_category'])`
  with `agg(['mean', 'count', 'std'])` — required by rubric
- Built a `pivot_table` of popularity by genre and tempo category
- Computed correlation matrix using `.corr()`
- Visualized correlation matrix as a seaborn heatmap
- Answered 3 research questions with grouped stats
- Wrote markdown explanation of all findings

---

## Extra Analysis — `notebooks/questions.ipynb`

### Question 1 — What Do the Top 10% Most Popular Songs Have in Common?
- Defined top 10% threshold using `.quantile(0.90)`
- Split dataset into top 10% and rest
- Compared average audio features between the two groups
- Analyzed explicit content percentage in top 10% vs rest
- Identified top genres dominating the top 10%
- Analyzed tempo category distribution in top 10%
- Created bar chart comparing audio features (exported to figures/)
- Created bar chart of top genres in top 10% (exported to figures/)
- Created scatter plot of popularity vs danceability (exported to figures/)
- Wrote full markdown findings and conclusion

### Question 2 — Do Happy Songs Get More Popular or Do People Prefer Sad Songs?
- Derived mood category column using `.apply()`:
  Happy (valence >= 0.7), Neutral (0.3-0.7), Sad (valence <= 0.3)
- Computed average popularity by mood category
- Identified happiest and saddest genres by average valence
- Analyzed mood vs popularity per genre
- Computed correlation between valence and popularity (-0.0385)
- Created bar chart of popularity by mood (exported to figures/)
- Created scatter plot of valence vs popularity (exported to figures/)
- Wrote full markdown findings and conclusion

### Question 4 — Do Shorter Songs Get More Popular Than Longer Ones on Spotify?
- Removed 271 outlier songs over 10 minutes before analysis
- Categorized songs into 4 length buckets using `.apply()`:
  Short (< 2.5 min), Medium (2.5-4 min),
  Long (4-6 min), Very Long (> 6 min)
- Computed average popularity by length category
- Computed correlation between duration and popularity (+0.0114)
- Identified shortest genres: grindcore (127s), children (139s), study (141s)
- Identified longest genres: minimal-techno (361s),
  detroit-techno (349s), chicago-house (349s)
- Created bar chart of popularity by song length (exported to figures/)
- Created scatter plot of duration vs popularity (exported to figures/)
- Wrote full markdown findings and conclusion

---

## Figures Exported

All figures saved to `figures/` at dpi=300:

| Figure | Section |
|--------|---------|
| correlation_heatmap.png | Section 3 |
| top10_vs_rest_features.png | Question 1 |
| top10_genres.png | Question 1 |
| top10_popularity_danceability.png | Question 1 |
| popularity_by_mood.png | Question 2 |
| valence_vs_popularity.png | Question 2 |
| popularity_by_length.png | Question 4 |
| duration_vs_popularity.png | Question 4 |

---

## Git Contributions

| Branch | Purpose |
|--------|---------|
| `dhruv-analysis` | Main analysis work (Sections 1, 2, 3) + Questions |
| `Question` | Bonus Q&A analysis (Questions 1, 2, and 4) |

Branches were merged using pull requests following proper
git workflow as required by the rubric.

---

## Key Findings From My Analysis

- The Spotify dataset contains **49,999 tracks** across **114 genres**
  after cleaning
- **Pop-film and k-pop** are the most popular genres on average
- **Explicit songs** score **3.66 points higher** in popularity
  than clean songs on average
- **Loudness** has the strongest positive correlation with
  popularity (0.053) — though all correlations are weak
- **Instrumentalness** has the strongest negative correlation
  with popularity (-0.093) — vocal songs do better
- The top 10% most popular songs tend to have higher danceability,
  louder sound, and belong to pop, k-pop, or metal genres
- **Neutral songs** (valence 0.3-0.7) are more popular than
  either happy or sad songs
- Valence has a slight **negative correlation** (-0.0385) with
  popularity — people slightly prefer sadder songs on Spotify
- The **sweet spot for song length is 4-6 minutes** — scoring
  34.39 average popularity vs 30.53 for short songs
- Duration has almost no real impact on popularity
  (correlation = +0.0114)

---

## Tools Used

- Python 3, pandas, NumPy, matplotlib, seaborn, Jupyter Lab, Git / GitHub

# Contribution Report — Rafik Taleb
## FSU ID: rt24e

---

## Overview

I contributed to the project by adding two new research
questions with comprehensive exploratory data analysis,
visualizations, and key findings. All work was completed
on the `rafik-analysis` branch and merged into the main
analysis.

---

## Extra Analysis — `notebooks/questions.ipynb`

### Question 3 — Do Explicit Songs Differ in Audio Features Compared to Non-Explicit Songs?

- Compared audio features (loudness, speechiness, energy, etc.)
  between explicit and clean songs
- Created 5 visualizations:
  - Bar charts comparing features
  - Difference chart showing gap between explicit and clean
  - Box plots for distribution comparison
  - Genre explicit percentage chart
  - Correlation heatmap
- Wrote full markdown findings and conclusion

**Key Finding:** Explicit songs are **1.9 dB louder** with
**2.6x higher speechiness** than clean songs. However,
explicit content does not significantly impact popularity.

---

### Question 4 — Do Songs With Higher Loudness Get More Streams?

- Grouped songs by loudness categories and compared
  average popularity across groups
- Created 2 visualizations:
  - Bar chart of popularity by loudness category
  - Genre correlation heatmap for loudness vs popularity
- Wrote full markdown findings and conclusion

**Key Finding:** Moderate loudness songs **(-10 to -5 dB)**
are the most popular — not the loudest songs. Genre
correlation with loudness varies significantly.

---

## Figures Exported

All figures saved to `figures/` at dpi=300:

| Figure | Question |
|--------|---------|
| explicit_vs_clean_features.png | Question 3 |
| explicit_feature_difference.png | Question 3 |
| explicit_boxplots.png | Question 3 |
| explicit_by_genre.png | Question 3 |
| explicit_correlation_heatmap.png | Question 3 |
| popularity_by_loudness.png | Question 4 |
| loudness_popularity_correlation_heatmap.png | Question 4 |

---

## Git Contributions

| Branch | Purpose |
|--------|---------|
| `rafik-analysis` | Questions 3 and 4 analysis |

---

## Key Findings From My Analysis

- Explicit songs are **1.9 dB louder** than clean songs
- Explicit songs have **2.6x higher speechiness** — capturing
  rap and spoken word content
- Explicit content does **not** significantly boost popularity
- **Moderate loudness (-10 to -5 dB)** is the sweet spot
  for popularity — not maximum loudness
- Loudness vs popularity correlation varies greatly by genre

---

## Tools Used

- Python 3, pandas, NumPy, matplotlib, seaborn, Jupyter Lab, Git / GitHub

# Contribution Report — Thomas Schmidt
## FSU ID: tns23

---

## Overview

I contributed to the project by implementing Section 4 —
Visualizations and Feature Exploration in the main analysis
notebook. This included creating all four required plot types,
exporting figures, and writing plain-English findings. All work
was completed on the `viz` branch and merged into main.

---

## Notebook Contributions — `notebooks/analysis.ipynb`

### Section 4 — Visualizations and Feature Exploration
- Reloaded cleaned dataset to ensure Section 4 runs independently
- Created a line plot of average popularity by genre (top 20, sorted)
  - No release year column exists in the dataset, so genre was
    used as the ordered x-axis
- Created a bar plot of average energy by genre (top 15)
  using seaborn viridis color palette
- Created a histogram of danceability distribution with
  mean and median reference lines
- Created a scatter plot of energy vs loudness showing the
  strong positive correlation (r ≈ 0.76)
- Exported all 4 figures to `figures/` at dpi=300
- Wrote markdown key findings for each visualization

---

## Figures Exported

All figures saved to `figures/` at dpi=300:

| Figure | Section |
|--------|---------|
| popularity_by_genre.png | Section 4 |
| energy_by_genre.png | Section 4 |
| danceability_distribution.png | Section 4 |
| energy_vs_loudness.png | Section 4 |

---

## Git Contributions

| Branch | Purpose |
|--------|---------|
| `viz` | Section 4 — Visualizations and Feature Exploration |

Branch was merged using a pull request following proper
git workflow as required by the rubric.

---

## Key Findings From My Analysis

- Pop-film and k-pop lead average popularity across all genres,
  with a steep drop-off after the top 5
- Death-metal, grindcore, and metalcore are the most energetic
  genres (energy > 0.9)
- Danceability is roughly normally distributed, centered around
  0.55–0.60 with a slight left skew
- Energy and loudness have a strong positive correlation (r ≈ 0.76),
  the strongest relationship among all audio features
- High-popularity tracks appear across all energy/loudness levels,
  confirming these features alone do not determine popularity

---

## Tools Used

- Python 3, pandas, NumPy, matplotlib, seaborn, Jupyter Lab, Git / GitHub


---
---

# Contribution Report — Imran
## FSU ID: IA24C

---

## Overview

I contributed to the project by improving the interpretation and write-up quality of the analysis notebook, with a focus on clearer conclusions and stronger evidence-based explanations.

---

## Notebook Contributions `notebooks/analysis.ipynb`

### Section 4 — Research Q4 and Q5 Write-Up Improvements
- Expanded the Key Findings for **Research Q4 (Song Length Sweet Spot)**
  with clearer interpretation of quantile-level popularity patterns
- Added concrete numeric comparisons for each duration quantile
  to support conclusions
- Expanded the Key Findings for **Research Q5 (Collaboration Effect)**
  with clearer solo vs collaboration comparisons
- Added artist-count trend interpretation (1–6 artists) and caveats
  about lower sample sizes in high artist-count groups
- Improved readability and narrative clarity for final report use

---

## Key Findings From My Contributions

- Mid-length songs (Q3–Q4) show higher average popularity than very short and very long tracks
- Collaboration has a modest positive effect on popularity overall, with small-to-moderate collaborations performing best
- Adding explicit numeric evidence and caveats made the conclusions more defensible and easier to communicate

---

## Tools Used

- Python 3, pandas, NumPy, matplotlib, seaborn, Jupyter Lab, Git / GitHub

---
---