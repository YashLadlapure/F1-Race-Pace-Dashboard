# 🏎️ F1 Race Pace & Pit Strategy Dashboard (2010–2026)

![Tableau](https://img.shields.io/badge/Tableau-Public-blue?logo=tableau)
![Python](https://img.shields.io/badge/Python-3.10-green?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-1.5-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

An end-to-end **Data Engineering & Visualization** project built on a real-world Formula 1 dataset of **372,493 lap records** spanning **2010 to 2026**. Covers data cleaning, feature engineering, EDA in Python, and an interactive Tableau Public dashboard.

---

## 🔗 Live Dashboard

➡️ **[View on Tableau Public](https://public.tableau.com/app/profile/yash.ladlapure/viz/F1_Race_Pace_Dashboard_2010_2026/Dashboard1)**

---

## 📘 About

Formula 1 generates massive amounts of telemetry and race data every season. This project takes raw lap-level F1 data and answers three core questions:

- **Are F1 cars getting faster over the years?**
- **Which drivers consistently post the best lap times?**
- **How has pit stop strategy evolved from 2010 to 2026?**

The full pipeline goes from raw CSV → Python cleaning → aggregated datasets → Tableau dashboard.

---

## 📁 Repository Structure

```
F1-Race-Pace-Dashboard/
├── README.md                   # Project overview (this file)
├── DOCUMENTARY.md              # Full project story & deep dive
├── notebooks/
│   └── F1_EDA.ipynb            # EDA notebook (Google Colab)
├── data/
│   └── dataset_schema.md       # Column descriptions & data dictionary
├── dashboard/
│   └── tableau_info.md         # Dashboard structure & design notes
└── reports/
    └── project_report.md       # Full technical write-up
```

---

## 📊 Dataset

| Column | Type | Description |
|--------|------|-------------|
| `Race Id` | Dimension | Unique race identifier |
| `Race Name` | Dimension | Grand Prix name |
| `Race Year` | Dimension | Season year (2010–2026) |
| `Driver Id` | Dimension | Unique driver ID |
| `Constructor Id` | Dimension | Team/constructor ID |
| `Avg Lap Sec` | Measure | Average lap time in seconds |
| `Best Lap Sec` | Measure | Fastest single lap in seconds |
| `Laps` | Measure | Total laps completed |
| `Pit Laps` | Measure | Laps where a pit stop occurred |
| `Pit Pct` | Measure | % of laps with pit stops |
| `Total Laps` | Measure | Total laps in the race |

> **372,493 rows** | **11 columns** | **2010–2026**

---

## 🔧 Tech Stack

| Tool | Role |
|------|------|
| Python 3 (Pandas, Matplotlib, Seaborn) | Data cleaning, EDA, aggregation |
| Google Colab | Notebook environment |
| Tableau Public | Dashboard & interactive visualization |
| GitHub | Version control |

---

## 🔄 Pipeline

```
Raw f1.csv (372,493 rows, 11 cols)
        │
        ▼
[1] Load & inspect with Pandas
        │
        ▼
[2] Clean — filter outliers (Avg Lap Sec outside 60–150s)
        │
        ▼
[3] Feature Engineering
    ├─ race_summary.csv   (groupby Race Year + Race Id)
    └─ driver_summary.csv (groupby Driver Id + Race Year)
        │
        ▼
[4] EDA visualizations (line, histogram, boxplot, heatmap, bar)
        │
        ▼
[5] Export cleaned CSVs → connect to Tableau
        │
        ▼
[6] Build 4 charts + dashboard in Tableau Public
        │
        ▼
[7] Publish → Live on Tableau Public
```

---

## 📈 Dashboard Sheets

### 1. Season Pace — Line Chart
- X: Race Year | Y: AVG(Avg Lap Sec)
- Shows pace improvement from 2010–2019, plateau post-2022 regulation changes

### 2. Top 15 Drivers — Horizontal Bar Chart
- X: AVG(Avg Lap Sec) | Y: Driver Id (Top 15 filter)
- Ranks drivers by their average lap speed across all seasons

### 3. Pit Strategy — Dual-Axis Line Chart
- X: Race Year | Y1: AVG(Avg Lap Sec) | Y2: AVG(Pit Pct)
- Shows correlation between pit stop frequency and lap time trends

### 4. Best Lap Per Season — Dot / Scatter Chart
- X: Race Year | Y: AVG(Best Lap Sec) | Mark: Circle
- Each dot = one season's fastest average lap

---

## 📐 KPIs

| Metric | Value |
|--------|-------|
| Average Lap Time | **91.2 seconds** |
| Total Laps in Dataset | **372,493** |

---

## 🎨 Design

- Background: Dark navy (`#0D1117`)
- Canvas: `1200 x 800 px` fixed
- Layout: Tiled 2x2 grid
- Titles: White (`#FFFFFF`), Bold
- Accent colors: Coral red, Steel blue

---

## 🛠️ Known Issues Fixed

| Issue | Cause | Fix |
|-------|-------|-----|
| KPI values truncated | Text box too small | Resized containers |
| Best Lap chart clipped | Canvas was 1000px wide | Expanded to 1200px |
| Titles not visible | Color was `#333333` (dark gray) | Changed to `#FFFFFF` + Bold |

---

## 👤 Author

**Yash Ladlapure** — [GitHub](https://github.com/YashLadlapure) | [Portfolio](https://yashladlapure.github.io/portfolio-website/)

---

## 📄 License

MIT — open to use and extend.
