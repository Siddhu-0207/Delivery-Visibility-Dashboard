import pandas as pd
import random
from datetime import datetime, timedelta

# Number of sample records
num_records = 100

# Furniture STOR. dataset 
shipment_data = []

# Furniture Product list
products = ["Chair", "Table", "Bed", "Cabinet", "Sofa", "Desk", "Shelf"]

# Logistics providers (consistent and India-based) (own and third-party)
carriers = ["Furniture STOR Logistics", "RapidShip India"]

# Indian cities covered
cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai"]

# Probability for missing values (10% chance)
missing_prob = 0.1

for i in range(num_records):
    shipment_id = f"SHP_{1000 + i}"
    order_id = f"ORD_{500 + i}"
    customer_id = f"CUST_{300 + i}"
    product_name = random.choice(products)
    
    # Product weight (kg); might be missing sometimes
    product_weight = round(random.uniform(10, 150), 2) if random.random() > missing_prob else None

    #dispatch date in March 2025
    dispatch_date = datetime(2025, 3, random.randint(1, 15), random.randint(8, 18))
    
    # Expected delivery is between 3 to 10 days after dispatch (suitable for furniture deliveries)
    expected_delivery = dispatch_date + timedelta(days=random.randint(3, 10))
    
    # Actual delivery may be on time or delayed by up to 24 hours
    actual_delivery = expected_delivery + timedelta(hours=random.randint(-12, 24))
    transit_duration = round((actual_delivery - dispatch_date).total_seconds() / 3600, 2)  # in hours

    current_location = random.choice(cities)
    status = "Delivered" if actual_delivery <= expected_delivery else "Delayed"
    delay_reason = random.choice(["Weather", "Traffic", "Warehouse Issue", "Handling Delay"]) if status == "Delayed" else None
    carrier_name = random.choice(carriers)
    
    # Transportation cost (INR); might be missing sometimes
    transport_cost = round(random.uniform(500, 5000), 2) if random.random() > missing_prob else None

    # Customer rating might also be missing
    customer_rating = random.choice([1, 2, 3, 4, 5]) if random.random() > missing_prob else None

    shipment_data.append([
        shipment_id, order_id, customer_id, product_name, product_weight, dispatch_date,
        expected_delivery, actual_delivery, transit_duration, current_location, status,
        delay_reason, carrier_name, transport_cost, customer_rating
    ])

# Creating a DataFrame with units indicated in column headers
df = pd.DataFrame(shipment_data, columns=[
    "Shipment_ID", "Order_ID", "Customer_ID", "Product_Name", "Product_Weight (kg)",
    "Dispatch_Date", "Expected_Delivery_Date", "Actual_Delivery_Date", "Transit_Duration (hrs)",
    "Current_Location", "Delivery_Status", "Delay_Reason", "Carrier_Name",
    "Transportation_Cost (INR)", "Customer_Rating"
])

# Saving the DataFrame to a CSV file 
file_path = "furniture_stor_delivery_data_100_india.csv"
df.to_csv(file_path, index=False, date_format='%d-%m-%Y %H:%M:%S')
print("Dataset saved as furniture_stor_delivery_data_100_india.csv")
