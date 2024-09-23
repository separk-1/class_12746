# Seongeun Park / seongeup / 12-746 A1 / Homework 4-2

import pandas as pd

df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

total_vehicles = len(df)
print(f"1. The number of electric vehicles (both hybrid and battery) that were registered in the state of Washington at the time the file was created: {total_vehicles}")

bev_count = df[df['Electric Vehicle Type'] == 'Battery Electric Vehicle (BEV)'].shape[0]
bev_percent = (bev_count / total_vehicles) * 100
print(f"2. The percent of vehicles that are battery electric vehicles (BEVs): {bev_percent:.4f}%")

average_range = df[df['Electric Range'] > 0]['Electric Range'].mean()
print(f"3. The average electric range of all the vehicles: {average_range:.4f} miles")

oldest_year = df['Model Year'].min()
oldest_car = df[df['Model Year'] == oldest_year][['Make', 'Model']].iloc[0]
print(f"4. The oldest car is from {oldest_year} and is a {oldest_car['Make']} {oldest_car['Model']}.")