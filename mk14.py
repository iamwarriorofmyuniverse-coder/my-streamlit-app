import matplotlib.pyplot as plt
import pandas as pd

# Load data
sales = pd.read_csv("sales_data.csv")

# --- ADD A NEW CATEGORY MANUALLY TO GET A 3RD BAR ---
new_data = pd.DataFrame(
    [
        {
            "Date": "10-05-2026",
            "Product": "T-Shirt",
            "Category": "c",
            "Units_sold": 15,
            "Revenue": 150000,
            "Region": "South",
        }
    ]
)

sales = pd.concat([sales, new_data], ignore_index=True)

# Parse Date and sort
sales["Date"] = pd.to_datetime(sales["Date"], format="%d-%m-%Y")
sales = sales.sort_values("Date")

# --- Visualization ---
plt.figure(figsize=(12, 8))

# Plot 1: Total Revenue by Category (Now shows 3 bars!)
plt.subplot(2, 2, 1)
# Use a colormap instead of a fixed 2-color list so it automatically colors all bars
sales.groupby("Category")["Revenue"].sum().plot(
    kind="bar", color=plt.cm.tab10.colors
)
plt.title("Total Revenue by Category")
plt.ylabel("Revenue")
plt.xlabel("Category")
plt.xticks(rotation=0)

# Plot 2: Daily Units Sold
plt.subplot(2, 2, 2)
sales.set_index("Date")["Units_sold"].plot(marker="o", color="teal")
plt.title("Daily Units Sold Trend")
plt.ylabel("Units")
plt.grid(True, linestyle="--", alpha=0.5)

# Plot 3: Region Distribution
plt.subplot(2, 2, 3)
sales["Region"].value_counts().plot(
    kind="pie", autopct="%1.1f%%", startangle=90, colors=plt.cm.Pastel1.colors
)
plt.title("Sales by Region")
plt.ylabel("")

# Plot 4: Revenue vs Units
plt.subplot(2, 2, 4)
plt.scatter(
    sales["Units_sold"], sales["Revenue"], color="purple", alpha=0.7, edgecolors="k"
)
plt.title("Revenue vs Units Sold")
plt.xlabel("Units Sold")
plt.ylabel("Revenue")
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()