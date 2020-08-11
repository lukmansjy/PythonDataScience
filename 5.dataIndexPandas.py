import pandas as pd

dataTitanic = pd.read_csv('data/titanic.csv')
print(dataTitanic)

print('# Memilih kolom age (type: Series)')
print(dataTitanic['age'])

print('# Memilih kolom age (type: DataFrame)')
print(dataTitanic[['age']])

print('# Memilih lebih dari 1 kolom')
print(dataTitanic[['age', 'fare']])

print('# memilih data dengan dot notation')
print(dataTitanic.age)

# Memilih data dengan iloc, format .iloc[baris, kolom]
print('# Memilih baris pertama')
print(dataTitanic.iloc[0])

print('# Memilih baris no index 0 - 11')
print(dataTitanic.iloc[0:11])

print('# Memilih semua baris, dan kolom no index 3 (hanya menampilkan age)')
print(dataTitanic.iloc[:, 3])

print('# Memilih 5 data terakhir dan yg paling akhir tidak pilih, dan memilih 4 kolom terakhir')
print(dataTitanic.iloc[-5:-1, -4:])

print('# Memilih data pada baris dengan no indek 0, 2, 4')
print(dataTitanic.iloc[[0, 2, 4]])

print('# Memilih data pada baris dengan no indek 0, 2, 4, 5 dan kolom 1, 3, 6')
print(dataTitanic.iloc[[0, 2, 4, 5], [1, 3, 6]])

# Memilih data dengan nama baris atau kolom, menggunakan loc, format .loc['nama baris', 'nama klom']
dataTitanic2 = pd.read_csv('data/titanic.csv', index_col='embarked') # membaca file csv dan merubah index kolom menjadi embarked
print(dataTitanic2)

print('# Memilih data yang embarked berlabel S')
print(dataTitanic2.loc['S'])

print('# Memilih data yang embarked berlabel S, dan kolom age')
print(dataTitanic2.loc['S', 'age'])

print('# Memilih data yang embarked berlabel S, dan kolom age dan fare')
print(dataTitanic2.loc['S', ['age', 'fare']])

print('# Memilih data yang embarked berlabel S, Q, dan kolom age dan fare')
print(dataTitanic2.loc[['S', 'Q'], ['age', 'fare']])
