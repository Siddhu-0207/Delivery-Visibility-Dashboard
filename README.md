# Delivery Visibility Dashboard

A Power BI dashboard that visualizes delivery performance for a fictional furniture retailer (Furniture STORe).  
It explores shipment on-time rates, transit times, transportation cost, carrier performance and city-level delivery hotspots.
![WhatsApp Image 2025-12-19 at 6 50 44 PM](https://github.com/user-attachments/assets/e42fc136-eb7b-4916-8f66-fafb312e02ab)

---


- `supply_chain_dashboard.pbix` — the Power BI report  
- `generate_dataset.py` — small Python script to create a synthetic shipment dataset  
  

---

## Tech Used
- Power BI Desktop (.pbix)  
- Python (data generation / ETL)  
- CSV / Excel for data storage  
- ArcGIS map visuals inside Power BI 

---


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



