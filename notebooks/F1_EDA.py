# =============================================================
# F1 Race Pace & Pit Strategy — EDA & Data Engineering
# Dataset: f1.csv | 372,493 laps | 2010-2026
# Author: Yash Ladlapure
# =============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------------
# 1. LOAD DATA
# ---------------------------------------------------------------
df = pd.read_csv('f1.csv')
print("Shape:", df.shape)          # (372493, 11)
print(df.dtypes)
print(df.head())

# ---------------------------------------------------------------
# 2. INSPECT & UNDERSTAND
# ---------------------------------------------------------------
print(df.info())
print(df.describe())
print("Null values:\n", df.isnull().sum())
print("Unique years:", sorted(df['Race Year'].unique()))
print("Unique drivers:", df['Driver Id'].nunique())

# ---------------------------------------------------------------
# 3. CLEAN — Remove outliers
# F1 lap times realistically fall between 60s and 150s
# ---------------------------------------------------------------
before = len(df)
df = df[(df['Avg Lap Sec'] > 60) & (df['Avg Lap Sec'] < 150)]
after = len(df)
print(f"Removed {before - after} outlier rows. Remaining: {after}")

# Also drop rows where Best Lap Sec is null or out of range
df = df.dropna(subset=['Best Lap Sec'])
df = df[(df['Best Lap Sec'] > 55) & (df['Best Lap Sec'] < 150)]
print("After Best Lap clean:", len(df))

# ---------------------------------------------------------------
# 4. FEATURE ENGINEERING — Aggregate summaries
# ---------------------------------------------------------------

# 4a. Race-level summary (grouped by year + race)
race_summary = df.groupby(['Race Year', 'Race Id', 'Race Name']).agg(
    Avg_Lap_Sec   = ('Avg Lap Sec',  'mean'),
    Best_Lap_Sec  = ('Best Lap Sec', 'min'),
    Total_Laps    = ('Laps',         'sum'),
    Pit_Laps      = ('Pit Laps',     'sum'),
    Avg_Pit_Pct   = ('Pit Pct',      'mean')
).reset_index()

print("race_summary shape:", race_summary.shape)
print(race_summary.head())

# 4b. Driver-level summary (grouped by driver + year)
driver_summary = df.groupby(['Driver Id', 'Race Year']).agg(
    Avg_Lap_Sec   = ('Avg Lap Sec',  'mean'),
    Best_Lap_Sec  = ('Best Lap Sec', 'min'),
    Total_Laps    = ('Laps',         'sum'),
    Avg_Pit_Pct   = ('Pit Pct',      'mean')
).reset_index()

print("driver_summary shape:", driver_summary.shape)
print(driver_summary.head())

# ---------------------------------------------------------------
# 5. EDA VISUALIZATIONS
# ---------------------------------------------------------------

sns.set_style('darkgrid')
plt.rcParams['figure.figsize'] = (12, 5)

# --- 5a. Average Lap Time per Season (Line Chart) ---
yearly = race_summary.groupby('Race Year')['Avg_Lap_Sec'].mean()
plt.figure()
plt.plot(yearly.index, yearly.values, marker='o', color='coral', linewidth=2)
plt.title('Average Lap Time per Season (2010-2026)')
plt.xlabel('Season')
plt.ylabel('Avg Lap Time (seconds)')
plt.tight_layout()
plt.savefig('season_pace.png', dpi=150)
plt.show()

# --- 5b. Distribution of Avg Lap Times (Histogram) ---
plt.figure()
plt.hist(df['Avg Lap Sec'], bins=50, color='steelblue', edgecolor='black')
plt.title('Distribution of Average Lap Times')
plt.xlabel('Avg Lap Sec')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('lap_distribution.png', dpi=150)
plt.show()

# --- 5c. Boxplot of Lap Times by Year ---
plt.figure(figsize=(16, 5))
sns.boxplot(data=df, x='Race Year', y='Avg Lap Sec', palette='Blues')
plt.title('Lap Time Distribution by Season')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('boxplot_by_year.png', dpi=150)
plt.show()

# --- 5d. Correlation Heatmap ---
numeric_cols = ['Avg Lap Sec', 'Best Lap Sec', 'Laps', 'Pit Laps', 'Pit Pct']
corr = df[numeric_cols].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', square=True)
plt.title('Feature Correlation Heatmap')
plt.tight_layout()
plt.savefig('heatmap.png', dpi=150)
plt.show()

# --- 5e. Top 15 Drivers by Avg Lap Time ---
top_drivers = (
    driver_summary.groupby('Driver Id')['Avg_Lap_Sec']
    .mean()
    .sort_values()
    .head(15)
)
plt.figure(figsize=(10, 6))
top_drivers.sort_values(ascending=True).plot(kind='barh', color='steelblue')
plt.title('Top 15 Drivers by Average Lap Time')
plt.xlabel('Avg Lap Time (seconds)')
plt.tight_layout()
plt.savefig('top_drivers.png', dpi=150)
plt.show()

# --- 5f. Pit Strategy Trend ---
pit_trend = race_summary.groupby('Race Year')['Avg_Pit_Pct'].mean()
plt.figure()
plt.plot(pit_trend.index, pit_trend.values, marker='s', color='orange', linewidth=2)
plt.title('Average Pit Stop % per Season')
plt.xlabel('Season')
plt.ylabel('Avg Pit Stop %')
plt.tight_layout()
plt.savefig('pit_strategy.png', dpi=150)
plt.show()

# --- 5g. Best Lap Per Season (Scatter) ---
best_lap = race_summary.groupby('Race Year')['Best_Lap_Sec'].mean()
plt.figure()
plt.scatter(best_lap.index, best_lap.values, color='red', s=80, zorder=5)
plt.title('Best (Fastest) Lap Per Season')
plt.xlabel('Season')
plt.ylabel('Avg Best Lap (seconds)')
plt.tight_layout()
plt.savefig('best_lap_season.png', dpi=150)
plt.show()

# ---------------------------------------------------------------
# 6. EXPORT CLEANED DATA
# ---------------------------------------------------------------
race_summary.to_csv('race_summary.csv', index=False)
driver_summary.to_csv('driver_summary.csv', index=False)
print("Exported: race_summary.csv & driver_summary.csv")
print("Done! Upload these CSVs to Tableau as data sources.")
