# F1 Race Pace & Pit Strategy — Project Report

**Author:** Yash Ladlapure
**Dataset:** f1.csv (372,493 rows, 2010–2026)
**Tools:** Python, Pandas, Matplotlib, Seaborn, Tableau Public

## Objective

Analyze 16 years of Formula 1 lap data to understand how race pace and pit stop strategy have changed over time, identify the fastest drivers, and visualize findings in an interactive dashboard.

## Data Cleaning

The raw dataset had outliers in lap time columns where values were physically impossible for an F1 car. Filtering was applied to keep only rows where `Avg Lap Sec` fell between 60 and 150 seconds. Null values in `Best Lap Sec` were also dropped. No imputation was done — rows with bad data were simply removed since the dataset was large enough.

## Feature Engineering

Two aggregated tables were created from the cleaned data.

`race_summary` groups by Race Year, Race Id, and Race Name. It computes mean of Avg Lap Sec, min of Best Lap Sec, sum of Laps and Pit Laps, and mean of Pit Pct per race.

`driver_summary` groups by Driver Id and Race Year. It computes the same aggregations at the driver level across all races in a season.

Both tables were exported as CSVs and loaded into Tableau as separate data sources.

## EDA Findings

Average lap times showed a clear downward trend from 2010 to 2019, meaning cars got faster each year as aerodynamic and power unit development accelerated. There was a visible plateau from 2020 to 2022 when the ground-effect regulation change forced teams to start fresh. The lap time distribution was roughly normal, centered around 88–95 seconds depending on the season. The correlation heatmap showed Pit Pct and Pit Laps were strongly correlated with each other (expected) and had a weaker correlation with Avg Lap Sec. The top 15 drivers by average lap time were consistently dominated by a small set of driver IDs across multiple seasons.

## Dashboard

Four sheets were built in Tableau and assembled into a single dashboard:

**Season Pace** shows the average lap time trend per season as a line chart. The downward slope from 2010 to 2019 is clearly visible, followed by the regulation-change plateau.

**Top 15 Drivers** is a horizontal bar chart filtered to the 15 drivers with the lowest average lap times across the dataset. Sorted ascending so the fastest driver appears at the top.

**Pit Strategy** is a dual-axis line chart. The left axis shows average lap time and the right axis shows average pit stop percentage per season. The two lines together show how changes in pit strategy correlated with pace changes over the years.

**Best Lap Per Season** is a scatter/dot chart (mark type: Circle) showing the average fastest lap per season. Unlike the other charts this one uses dots instead of a line to emphasize that each season's best lap is a discrete data point rather than part of a continuous trend.

The dashboard uses a dark navy background, white bold titles, and a fixed 1200x800px canvas. KPIs at the top show overall average lap time (91.2s) and total laps in the dataset (372,493).

## Issues Encountered

The KPI text boxes were clipping the numbers because the containers were too small for the font size. Resizing them fixed it. The Best Lap Per Season chart was cutting off at around 2020 because the dashboard canvas was only 1000px wide — expanding it to 1200px resolved the issue. Chart titles were nearly invisible because Tableau's default title color (#333333 dark gray) blended into the navy background. Changed to #FFFFFF with Bold on all four sheets.

## Insights

F1 cars got measurably faster from 2010 to 2019. The 2022 regulation change caused a temporary slowdown as teams adapted to ground-effect aerodynamics. Pit stop strategy has shifted toward fewer, more calculated stops over the 16-year window. A small group of drivers consistently appears at the top of the average lap time rankings across multiple seasons, confirming that top-team driver lineups have remained stable.
