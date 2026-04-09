import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('f1.csv')
print(df.shape)
print(df.dtypes)
print(df.head())
print(df.isnull().sum())
print(df.describe())

df = df[(df['Avg Lap Sec'] > 60) & (df['Avg Lap Sec'] < 150)]
df = df.dropna(subset=['Best Lap Sec'])
df = df[(df['Best Lap Sec'] > 55) & (df['Best Lap Sec'] < 150)]
print(df.shape)

race_summary = df.groupby(['Race Year', 'Race Id', 'Race Name']).agg(
    Avg_Lap_Sec  = ('Avg Lap Sec',  'mean'),
    Best_Lap_Sec = ('Best Lap Sec', 'min'),
    Total_Laps   = ('Laps',         'sum'),
    Pit_Laps     = ('Pit Laps',     'sum'),
    Avg_Pit_Pct  = ('Pit Pct',      'mean')
).reset_index()

driver_summary = df.groupby(['Driver Id', 'Race Year']).agg(
    Avg_Lap_Sec  = ('Avg Lap Sec',  'mean'),
    Best_Lap_Sec = ('Best Lap Sec', 'min'),
    Total_Laps   = ('Laps',         'sum'),
    Avg_Pit_Pct  = ('Pit Pct',      'mean')
).reset_index()

sns.set_style('darkgrid')

yearly = race_summary.groupby('Race Year')['Avg_Lap_Sec'].mean()
plt.figure(figsize=(12, 5))
plt.plot(yearly.index, yearly.values, marker='o', color='coral', linewidth=2)
plt.title('Average Lap Time per Season (2010-2026)')
plt.xlabel('Season')
plt.ylabel('Avg Lap Time (s)')
plt.tight_layout()
plt.savefig('season_pace.png', dpi=150)
plt.show()

plt.figure(figsize=(10, 4))
plt.hist(df['Avg Lap Sec'], bins=50, color='steelblue', edgecolor='black')
plt.title('Distribution of Average Lap Times')
plt.xlabel('Avg Lap Sec')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('lap_distribution.png', dpi=150)
plt.show()

plt.figure(figsize=(16, 5))
sns.boxplot(data=df, x='Race Year', y='Avg Lap Sec', palette='Blues')
plt.title('Lap Time by Season')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('boxplot_by_year.png', dpi=150)
plt.show()

numeric_cols = ['Avg Lap Sec', 'Best Lap Sec', 'Laps', 'Pit Laps', 'Pit Pct']
corr = df[numeric_cols].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', square=True)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('heatmap.png', dpi=150)
plt.show()

top_drivers = (
    driver_summary.groupby('Driver Id')['Avg_Lap_Sec']
    .mean()
    .sort_values()
    .head(15)
)
plt.figure(figsize=(10, 6))
top_drivers.plot(kind='barh', color='steelblue')
plt.title('Top 15 Drivers by Avg Lap Time')
plt.xlabel('Avg Lap Time (s)')
plt.tight_layout()
plt.savefig('top_drivers.png', dpi=150)
plt.show()

pit_trend = race_summary.groupby('Race Year')['Avg_Pit_Pct'].mean()
plt.figure(figsize=(12, 5))
plt.plot(pit_trend.index, pit_trend.values, marker='s', color='orange', linewidth=2)
plt.title('Avg Pit Stop % per Season')
plt.xlabel('Season')
plt.ylabel('Pit Stop %')
plt.tight_layout()
plt.savefig('pit_strategy.png', dpi=150)
plt.show()

best_lap = race_summary.groupby('Race Year')['Best_Lap_Sec'].mean()
plt.figure(figsize=(12, 5))
plt.scatter(best_lap.index, best_lap.values, color='red', s=80, zorder=5)
plt.title('Best Lap Per Season')
plt.xlabel('Season')
plt.ylabel('Best Lap (s)')
plt.tight_layout()
plt.savefig('best_lap_season.png', dpi=150)
plt.show()

race_summary.to_csv('race_summary.csv', index=False)
driver_summary.to_csv('driver_summary.csv', index=False)
