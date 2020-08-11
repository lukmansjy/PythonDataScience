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


#### Membersikan data dari NaN ####

age = dataTitanic['age']

# secara default panda akan skip Nan (skipna)
print(age.count())
print(age.mean())
print(age.median())
print(age.sum())
print(age.std())

# Mendapatkan umur bersih (tanpa missing value/NaN)
ageClean = age.dropna()
print('Age Clean')
print(ageClean)

print('# Menghilangakan baris yang ada NaN nya')
dataTitanicClean = dataTitanic.dropna()
print(dataTitanicClean)

print('# Menghilangakan kolom yang ada NaN nya')
dataTitanicClean2 = dataTitanic.dropna(axis=1)
print(dataTitanicClean2)

print('# Tidak di drop minimal 8 data yang bukan NaN')
dataTitanicClean2 = dataTitanic.dropna(thresh=8) # jika thresh=7 maka minimal 7, dst
print(dataTitanicClean2)

''' 
Note: Sebenarnya jangn pernah menghilangkan data yang ada NaNnya,
karena siapa tau ada data penting. Jika digunakan untuk AI/ML
biasanya data-data kosong (NaN) diisi dengan data rata-rata kolom tsb.
Contohnya menggunakan fillna()
'''

print( dataTitanic.age.fillna(value=dataTitanic.age.mean()) )
# Memasukkan ke DataFrame
dataTitanic.age = dataTitanic.age.fillna(value=dataTitanic.age.mean())
print(dataTitanic)


## Merubah type data panda series di menjadi array
'''
Karena biasanya di library Machine Learning seperti Library sklearn membutuhkan array
'''
print(dataTitanic.age.values)
