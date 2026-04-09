# Dataset Schema

**File:** f1.csv
**Rows:** 372,493
**Columns:** 11
**Range:** 2010 – 2026

| Column | Type | Description |
|---|---|---|
| Race Id | string | Unique identifier for each race |
| Race Name | string | Name of the Grand Prix |
| Race Year | int | Season year |
| Driver Id | string | Unique driver identifier |
| Constructor Id | string | Team/constructor identifier |
| Avg Lap Sec | float | Average lap time in seconds for that driver in that race |
| Best Lap Sec | float | Fastest single lap time in seconds |
| Laps | int | Total laps completed by the driver |
| Pit Laps | int | Number of laps where a pit stop was made |
| Pit Pct | float | Percentage of laps where a pit stop occurred |
| Total Laps | int | Total laps in the race |

After cleaning, values where `Avg Lap Sec` was outside 60–150 seconds were removed as outliers. Rows with null `Best Lap Sec` were also dropped. The final clean dataset was aggregated into two derived tables:

- **race_summary.csv** — grouped by Race Year + Race Id + Race Name
- **driver_summary.csv** — grouped by Driver Id + Race Year
