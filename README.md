
# **   Interactive Asset Performance Tracker**

This repository contains a comprehensive data project involving scraping financial data from the Yahoo Finance library, cleaning and organizing it, and creating an interactive dashboard for analysis. The dashboard provides insightful visualizations, filters, and a customizable UI.



## Key Features
### 1.Data Collection and Cleaning
**Custom Data Scraping:**
Due to privacy restrictions and the removal of the direct download option from Yahoo Finance, the data was not readily available on any platform.
Developed a custom solution using the yahoofinance library to scrape data for over 70 financial instruments, including stocks, ETFs, cryptocurrencies, and currency pairs.

**Historical Data:**
Collected several years of historical data, including Symbol, Date, Open, Close, Adj Close, and Volume.

**Error Handling and Cleaning:**
Processed and cleaned a dataset of more than 20k rows that initially contained numerous errors and inconsistencies.
Structured and organized the data into meaningful columns for analysis.

### 2. Enrichment
**Logos and Symbol Mapping:** Downloaded PNG logos for each financial instrument. Uploaded logos to an online service to generate direct retrieval URLs. Created a CSV file mapping Symbol, Type (Stock, ETF, Crypto, etc.), and Logo URL.

**Data Augmentation:** Merged the logo data with the primary dataset using SQL-like queries. Appended enriched data to the cleaned dataset for a complete overview.

### 3. Interactive Dashboard
**Filters and Insights:**
Built an interactive dashboard with filters for days, months, and years. Displays key metrics, including stock open dates, percentage changes, and up/down movements.

**Dynamic Results:**
The dashboard provides real-time updates based on filter selections, ensuring dynamic, on-the-fly calculations and visualizations.

**UI Features:**
Added a toggle button for switching between dark and light modes for a personalized user experience.
Enhanced the dashboard's UI with navigators for easy data exploration.

**Advanced Queries:**
Appended and merged data with custom queries to join and analyze data seamlessly.
Incorporated logo information into the dashboard for a polished, visually enriched interface.

## Applied Steps
### Applied on ALL Stocks Data
![App Screenshot](https://github.com/Nirajmahajan27/Market-Analysis/blob/main/Applied%20Steps/Screenshot%202024-11-22%20164511.png?raw=true)

### Appplied on Trackers
![App Screenshot](https://github.com/Nirajmahajan27/Market-Analysis/blob/main/Applied%20Steps/Screenshot%202024-11-22%20164552.png?raw=true)

## Dashboard Screenshots

![App Screenshot](https://github.com/Nirajmahajan27/Market-Analysis/blob/main/Portfolio%20Images/Screenshot%202024-11-22%20151442.png?raw=true)

![App Screenshot](https://github.com/Nirajmahajan27/Market-Analysis/blob/main/Portfolio%20Images/Screenshot%202024-11-22%20151605.png?raw=true)

![App Screenshot](https://github.com/Nirajmahajan27/Market-Analysis/blob/main/Portfolio%20Images/Screenshot%202024-11-22%20151652.png?raw=true)

![App Screeshot](https://github.com/Nirajmahajan27/Market-Analysis/blob/main/Portfolio%20Images/Screenshot%202024-11-22%20151715.png?raw=true)
## Tools and Technologies
Python Libraries: yahoofinance, pandas etc

Power BI: Used for designing the interactive dashboard and visualizations.

DAX (Data Analysis Expressions): For custom measures and complex 
calculations.

Data Storage: CSV files for storing cleaned and enriched datasets.

CSV Integration: To ingest and manage large datasets.

Data Modeling: To optimize data relationships for efficient processing.

## Challenges and Solutions
**Data Accessibility:**
Addressed the lack of available data due to Yahoo Finance’s restrictions by implementing custom scraping techniques.

**Data Cleaning:**
Overcame errors and inconsistencies in the raw dataset through manual and programmatic cleaning.

**Dynamic User Experience:**
Designed the dashboard to respond instantly to user inputs, creating a highly interactive tool.



