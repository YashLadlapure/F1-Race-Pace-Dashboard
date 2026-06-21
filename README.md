# F1 Race Pace & Pit Strategy Dashboard (2010–2026)

![Tableau](https://img.shields.io/badge/Tableau-Public-blue?logo=tableau)
![Python](https://img.shields.io/badge/Python-3.10-green?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-1.5-orange)

End-to-end data project on 372,493 F1 lap records from 2010 to 2026. Python for cleaning and EDA, Tableau Public for the dashboard.

**[View Dashboard on Tableau Public](https://public.tableau.com/app/profile/yash.ladlapure/viz/F1_Race_Pace_Dashboard_2010_2026/Dashboard1)**

---

## What I was trying to answer

- Are F1 cars actually getting faster each year?
- Which drivers post the most consistent lap times across seasons?
- How has pit stop frequency changed since 2010?

---

## Pipeline

Raw CSV → Pandas cleaning (filtered laps outside 60–150s) → feature engineering into `race_summary.csv` and `driver_summary.csv` → EDA → Tableau dashboard.

---

## Dataset

372,493 rows, 11 columns. Key fields: `Race Year`, `Driver Id`, `Avg Lap Sec`, `Best Lap Sec`, `Pit Pct`.

Full schema in `data/dataset_schema.md`.

---

## Structure

```
F1-Race-Pace-Dashboard/
├── notebooks/F1_EDA.ipynb
├── data/dataset_schema.md
├── dashboard/tableau_info.md
└── reports/project_report.md
```
