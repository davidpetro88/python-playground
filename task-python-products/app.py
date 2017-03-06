# from collections import Counter
import pandas as pd

# print(open('csv/products.csv').read())
print("Example Load Files Using Pandas")
print("\n")
df = pd.read_csv('csv/products.csv')
print("Show Columns")
print(df.columns)
print("\n")

print("Show All Products")
print(df.to_string())
print("\n")

print("Products by position 0 to 3")
print(df[0:3])
print("\n")

print("Find by name")
print(df[df['description'] == 'bermuda tommy GG'])
print("\n")

print("Find by code")
print(df[df['code'] == 6])
print("\n")

print("Price Greater Than 90.00")
print(df[df['price'] > 90.00])
print("\n")

print("Price Less Than 20.00")
print(df[df['price'] < 20.00])
print("\n")

print("Sum all quantity products")
print(df['quantity'].sum())
print("\n")

print("Mean quantity products")
print(df['quantity'].mean())
print("\n")

print("Product with max quantity")
print( df.iloc[[int(df['quantity'].idxmax())]])
print("\n\n")

print("Product with smaller quantity")
print( df.iloc[[int(df['quantity'].idxmin())]])
print("\n\n")

print("Product with max price")
print( df.iloc[[int(df['price'].idxmax())]])
print("\n\n")

print("Product with smaller price")
print( df.iloc[[int(df['price'].idxmin())]])
print("\n\n")
