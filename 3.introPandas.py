import pandas as pd
# from sqlalchemy import create_engine

dataCsv = pd.read_csv('data/titanic.csv')

# Print 8 data pertama
# print(dataCsv.head(8))

# Print 10 data terakhir
# print(dataCsv.tail(10))

# Print All data
print(dataCsv)

# Export ke data excel
# dataCsv.to_excel('data/titanic.xlsx', index=False, sheet_name='titanic')

# dataExcel = pd.read_excel('data/titanic.xlsx')

# print(dataExcel)

# Read data HTML from web
# dataHTML = pd.read_html('https://www.fdic.gov/Bank/individual/failed/banklist.html')

# print(dataHTML[0])

# Sql
# engine = create_engine('sqlite:///:memory:')
# dataCsv.to_sql('dataSql', con=engine)
#
# dataSql = pd.read_sql('dataSql', con=engine)
#
# print(dataSql)
