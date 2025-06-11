
# 🎾 Sports Radar Dashboard

An interactive data analytics web application built using **Streamlit**, powered by **PostgreSQL**, and enriched with data from the **SportRadar API**. This tool visualizes, filters, and analyzes tennis competition data, offering insights for sports analysts, fans, and decision-makers.

## 🔍 Project Overview

This project extracts tennis competition and ranking data via the SportRadar API, stores it in a PostgreSQL database, and visualizes it through an intuitive dashboard. It allows real-time search, filtering, ranking insights, and country-wise performance analysis.

## 🚀 Features

### ✅ Homepage Dashboard
- Total number of competitors
- Number of countries represented
- Highest points scored by a competitor

### 🔎 Search & Filter Competitors
- Filter by **name**, **rank range**, **country**, and **minimum points**
- Live display of filtered results

### 📋 Competitor Detail Viewer
- Detailed view of a selected competitor: rank, movement, country, competitions played

### 🌍 Country-Wise Analysis
- Average points and competitor count by country

### 🏆 Leaderboards
- Top-ranked competitors
- Competitors with highest points

## 🗃️ Database Schema

### `competitors`
| Column           | Type        | Description                   |
|------------------|-------------|-------------------------------|
| competitor_id    | VARCHAR(50) | Primary Key                  |
| name             | VARCHAR     | Competitor's full name        |
| country          | VARCHAR     | Country name                  |
| country_code     | CHAR(3)     | ISO country code              |
| abbreviation     | VARCHAR     | Short name/abbreviation       |

### `competitor_rankings`
| Column              | Type        | Description                         |
|---------------------|-------------|-------------------------------------|
| rank_id             | SERIAL      | Primary Key                        |
| rank                | INT         | Rank in current week               |
| movement            | INT         | Rank change from previous week     |
| points              | INT         | Ranking points                     |
| competitions_played | INT         | Number of competitions played      |
| competitor_id       | VARCHAR(50) | Foreign key referencing competitors|

Other tables:
- `categories`
- `competitions`
- `complexes`
- `venues`

## ⚙️ Setup Instructions

### 🔧 Requirements
- Python 3.8+
- PostgreSQL
- Streamlit
- pip

### 🔌 Installation

```bash
git clone https://github.com/your-username/sports_radar_dashboard.git
cd sports_radar_dashboard
pip install -r requirements.txt
```

### 🛠 Configure Database
1. Create a PostgreSQL database named `sports_radar`.
2. Execute the provided schema SQL to create tables.
3. Load data using `data_ingestion.py` or insert manually.
4. Update DB credentials in `db.py`.

### ▶️ Run the App

```bash
streamlit run main.py
```

## 🧠 Skills Gained

- 🐍 Python scripting
- 🔌 API data extraction (SportRadar)
- 🧮 SQL data modeling & queries
- 📊 Data visualization using Streamlit

## 📊 Sample Visuals

- Competitor filters in sidebar
- Interactive tables
- Country-wise average points
- Leaderboards

## 📂 Folder Structure

```
sports_radar_dashboard/
│
├── main.py                # Streamlit frontend
├── db.py                  # Database logic
├── utils.py               # Plotting utilities (optional)
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── /data/                 # (Optional) Raw JSON or CSV dumps
```

## 📎 References

- [SportRadar Tennis API](https://developer.sportradar.com/tennis/reference/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)

## 📬 Contact

**Author**: [Your Name]  
**Email**: [your.email@example.com]  
**GitHub**: [github.com/your-username](https://github.com/your-username)
