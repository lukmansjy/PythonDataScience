import pandas as pd

dataTitanic = pd.read_csv('data/titanic.csv')
print(dataTitanic) # Tidak ditampilkan semua

# Menampilkan semua data titanic di CMD
# pd.options.display.max_rows = len(dataTitanic)
# pd.options.display.min_rows = len(dataTitanic)
# print(dataTitanic)

print(dataTitanic.info()) # Menampilkan info data titanic
print(dataTitanic.describe()) # Menampilkan diskripsi data titanic
print(dataTitanic.describe(include='O')) # Menampilkan diskripsi data titanic yang non numberic