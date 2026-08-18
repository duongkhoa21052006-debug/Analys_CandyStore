

##  Project Overview

**Candy Store Data Pipeline & Analytics** is a data analytics project designed to clean, transform, and analyze candy store sales data.

The project uses **Python** for data cleaning and preprocessing, then provides an **interactive web-based dashboard** built with HTML, CSS, and JavaScript for exploring sales performance.

The dashboard allows users to upload a cleaned CSV file and analyze key business metrics such as sales, profit, orders, product performance, and regional performance.

---

##  Objectives
* Clean and preprocess raw sales data using Python.
* Improve data quality by handling duplicates, missing values, invalid values, and inconsistent data types.
* Transform raw data into a structured dataset suitable for analysis.
* Build an interactive dashboard for business performance analysis.
* Provide filters and visualizations to support data-driven decision making.

---

## Technologies
* **Python**
  * Pandas
  * NumPy
* **HTML5**
* **CSS3**
* **JavaScript**
* **Chart.js**
* **PapaParse**
* **CSV**

---

## 📂 Project Structure

```text
Candy-Store-Data-Pipeline-Analytics/
│
├── data/
│   ├── sale.csv
│   └── sale_cleaned.csv
│
├── cleaning/
│   └── clean_data.py
│
├── dashboard/
│   └── index.html
│
└── README.md
```

---

## 🔄 Data Pipeline

The project follows the workflow below:

```text
Raw CSV Data
     │
     ▼
Python Data Cleaning
     │
     ▼
Cleaned CSV Data
     │
     ▼
Upload CSV to Web Dashboard
     │
     ▼
Data Processing
     │
     ▼
Interactive Dashboard
```

---

## 🧹 Data Cleaning

Python is used to clean and preprocess the raw sales dataset.

The cleaning process includes:

* Standardizing column names.
* Removing duplicate records.
* Removing unnecessary whitespace from text fields.
* Converting numeric columns to appropriate data types.
* Converting date columns to DateTime format.
* Handling missing values.
* Detecting and removing invalid values.
* Validating quantity, price, cost, and discount values.
* Standardizing postal codes.
* Creating additional time-related attributes.

### Additional Features

The cleaning process also generates analytical fields such as:

* `date_id`
* `year`
* `quarter`
* `month`
* `month_name`
* `day`
* `day_of_week`
* `total_cost`
* `calculated_profit`
* `shipping_days`

---

## 📊 Dashboard
The web dashboard provides an interactive interface for analyzing the cleaned sales data.

### Key Performance Indicators
The dashboard displays:
* **Total Sales**
* **Total Profit**
* **Total Orders**
* **Quantity Sold**

### Visualizations
The dashboard includes:
* Sales by Month
* Sales by Category
* Profit by Region
* Top 10 Products
* Detailed Sales Table

### Filters
Users can filter the dashboard by:
* Year
* Region
* Category

---

## 🌐 Web Dashboard
The dashboard supports direct CSV upload.
Users can:
1. Open the dashboard.
2. Upload `sale_cleaned.csv`.
3. The system automatically reads the CSV file.
4. Data is processed in the browser.
5. KPIs, charts, and tables are updated automatically.
No database or real-time server is required for the current version.

---

##  Dataset
The dataset contains sales transaction information including:
* Order information
* Customer information
* Product information
* Location information
* Sales
* Profit
* Quantity
* Discount
* Shipping information
* Date information
The cleaned dataset contains **9,994 records and 33 columns**.
---

##  Business Questions
The dashboard can be used to answer questions such as:
* What is the total sales revenue?
* What is the total profit?
* Which months generate the highest sales?
* Which product categories perform best?
* Which regions generate the most profit?
* Which products have the highest sales?
* How many orders and products were sold?
* How does business performance change across different years?

---
##  How to Run
### 1. Clean the data
Run the Python cleaning script:

```bash
python clean_data.py
```

This generates:

```text
sale_cleaned.csv
```

### 2. Open the dashboard

Open:

```text
dashboard/index.html
```

For the best experience, use **VS Code with Live Server**.

### 3. Upload the cleaned dataset

Click:

```text
Upload CSV
```

and select:

```text
sale_cleaned.csv
```
The dashboard will automatically load the data.

---

##  Future Improvements
Possible improvements for future versions:
* Connect the dashboard to a SQL Server database.
* Add an ETL pipeline using SSIS.
* Build a Data Warehouse using a Star Schema.
* Add customer segmentation.
* Add sales forecasting using Machine Learning.
* Add more advanced business KPIs.
* Add date-range filtering.
* Add export functionality.
* Deploy the dashboard as a web application.

---
##  Project Purpose
This project was developed to practice practical skills in:
* Data Cleaning
* Data Preprocessing
* Exploratory Data Analysis
* Data Visualization
* Business Intelligence
* Web-based Dashboard Development
* Data Pipeline Development

---
## Project Status
**Completed**
Current version supports:
* CSV data cleaning
* Cleaned data generation
* CSV upload
* Interactive dashboard
* KPI analysis
* Data visualization
* Filtering
* Detailed data table
