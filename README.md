# Delivery Visibility Dashboard

A Power BI dashboard that visualizes delivery performance for a fictional furniture retailer (Furniture STORe).  
It explores shipment on-time rates, transit times, transportation cost, carrier performance and city-level delivery hotspots.

---

## What’s included
- `supply_chain_dashboard.pbix` — the Power BI report 
- `data/shipments_sample.csv` — sample dataset used in the report  
- `generate_dataset.py` — small Python script to create a synthetic shipment dataset  
- `screenshots/` 

---

## Tech
- Power BI Desktop (.pbix)  
- Python (data generation / ETL)  
- CSV / Excel for data storage  
- ArcGIS map visuals inside Power BI 

---

## Quick overview
The dashboard shows:
- KPI cards for Total Shipments, On-Time Delivery Rate, Avg Transit Duration and Avg Transport Cost  
- Product-level and carrier performance views  
- An interactive map of delivery locations and city hotspots  
- Tables to inspect individual shipments and delay reasons


---

## Dataset (basic schema)
- `Shipment_ID`, `Product_Name`, `Dispatch_Date`, `Actual_Delivery_Date`  
- `Delivery_Status` (Delivered / Delayed), `Delay_Reason`  
- `Transit_Duration`, `Transportation_Cost_INR`, `Carrier_Name`  
- `Origin_City`, `Destination_City`, `Lat`, `Lon`

---

## Reproduce locally
1. Open the PBIX in Power BI Desktop: **File → Open → supply_chain_dashboard.pbix**  
2. If the report uses local CSV: File → Transform data → edit source to point to `data/shipments_sample.csv`, then Refresh  
3. To regenerate the sample dataset:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows
   pip install -r requirements.txt
   python generate_dataset.py --n 100 --out data/shipments_sample.csv
