import pandas as pd
import numpy as np

# =========================================================
# 1. LOAD DATA
# =========================================================

input_file = "sale.csv"
output_file = "sale_cleaned.csv"

df = pd.read_csv(input_file)

print("=" * 60)
print("DATA CLEANING - SALES DATA")
print("=" * 60)

print(f"Original shape: {df.shape}")


# =========================================================
# 2. STANDARDIZE COLUMN NAMES
# =========================================================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nColumns after standardization:")
print(df.columns.tolist())


# =========================================================
# 3. REMOVE DUPLICATES
# =========================================================

duplicate_count = df.duplicated().sum()

print(f"\nDuplicate rows: {duplicate_count}")

df = df.drop_duplicates()


# =========================================================
# 4. CLEAN TEXT COLUMNS
# =========================================================

text_columns = df.select_dtypes(include=["object"]).columns

for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

# Replace multiple spaces with one space
for col in text_columns:
    df[col] = df[col].str.replace(r"\s+", " ", regex=True)


# =========================================================
# 5. HANDLE MISSING VALUES
# =========================================================

print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Numeric columns
numeric_columns = [
    "row_id",
    "postal_code",
    "unit_price",
    "unit_cost",
    "quantity",
    "discount",
    "sales",
    "profit"
]

# Convert numeric columns
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")


# =========================================================
# 6. CONVERT DATE COLUMNS
# =========================================================

df["order_date"] = pd.to_datetime(
    df["order_date"],
    errors="coerce"
)

df["ship_date"] = pd.to_datetime(
    df["ship_date"],
    errors="coerce"
)


# =========================================================
# 7. CHECK INVALID VALUES
# =========================================================

print("\nInvalid values:")

print("Quantity <= 0:",
      (df["quantity"] <= 0).sum())

print("Unit Price <= 0:",
      (df["unit_price"] <= 0).sum())

print("Unit Cost <= 0:",
      (df["unit_cost"] <= 0).sum())

print("Discount < 0:",
      (df["discount"] < 0).sum())

print("Discount > 1:",
      (df["discount"] > 1).sum())


# =========================================================
# 8. REMOVE INVALID RECORDS
# =========================================================

df = df[
    (df["quantity"] > 0) &
    (df["unit_price"] > 0) &
    (df["unit_cost"] > 0) &
    (df["discount"] >= 0) &
    (df["discount"] <= 1)
]


# =========================================================
# 9. HANDLE MISSING VALUES
# =========================================================

# Remove rows where important business information is missing

important_columns = [
    "order_id",
    "order_date",
    "customer_id",
    "product_id",
    "sales"
]

df = df.dropna(subset=important_columns)


# =========================================================
# 10. CLEAN POSTAL CODE
# =========================================================

df["postal_code"] = (
    df["postal_code"]
    .fillna(0)
    .astype(int)
    .astype(str)
)


# =========================================================
# 11. CREATE DATE DIMENSION COLUMNS
# =========================================================

df["year"] = df["order_date"].dt.year
df["quarter"] = "Q" + df["order_date"].dt.quarter.astype(str)
df["month"] = df["order_date"].dt.month
df["month_name"] = df["order_date"].dt.month_name()
df["day"] = df["order_date"].dt.day
df["day_of_week"] = df["order_date"].dt.day_name()


# =========================================================
# 12. CALCULATE ADDITIONAL BUSINESS METRICS
# =========================================================

# Calculate total cost
df["total_cost"] = df["unit_cost"] * df["quantity"]

# Calculate gross profit based on unit price and cost
df["calculated_profit"] = (
    df["unit_price"] * df["quantity"] - df["total_cost"]
)

# Shipping duration
df["shipping_days"] = (
    df["ship_date"] - df["order_date"]
).dt.days


# =========================================================
# 13. ROUND NUMERIC VALUES
# =========================================================

df["unit_price"] = df["unit_price"].round(2)
df["unit_cost"] = df["unit_cost"].round(2)
df["discount"] = df["discount"].round(2)
df["sales"] = df["sales"].round(2)
df["profit"] = df["profit"].round(2)
df["total_cost"] = df["total_cost"].round(2)
df["calculated_profit"] = df["calculated_profit"].round(2)


# =========================================================
# 14. CREATE ORDER DATE KEY
# =========================================================

df["date_id"] = (
    df["order_date"].dt.strftime("%Y%m%d").astype(int)
)


# =========================================================
# 15. REORDER COLUMNS
# =========================================================

columns_order = [
    "row_id",
    "order_id",
    "order_date",
    "ship_date",
    "ship_mode",

    "customer_id",
    "customer_name",
    "segment",

    "country",
    "city",
    "state",
    "postal_code",
    "region",

    "product_id",
    "category",
    "sub-category" if "sub-category" in df.columns else "sub_category",
    "product_name",

    "unit_price",
    "unit_cost",
    "quantity",
    "discount",
    "sales",
    "profit",

    "date_id",
    "year",
    "quarter",
    "month",
    "month_name",
    "day",
    "day_of_week",

    "total_cost",
    "calculated_profit",
    "shipping_days"
]

# Fix column name if it was converted to sub_category
if "sub-category" not in df.columns and "sub_category" in df.columns:
    pass

df = df[columns_order]


# =========================================================
# 16. SORT DATA
# =========================================================

df = df.sort_values(
    by=["order_date", "order_id"]
).reset_index(drop=True)


# =========================================================
# 17. FINAL DATA QUALITY CHECK
# =========================================================

print("\n" + "=" * 60)
print("FINAL DATA QUALITY CHECK")
print("=" * 60)

print("Final shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nData types:")
print(df.dtypes)


# =========================================================
# 18. EXPORT CLEANED DATA
# =========================================================

df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print("\n" + "=" * 60)
print("CLEANING COMPLETED")
print("=" * 60)

print(f"Output file: {output_file}")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")