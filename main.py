import oracledb
from pymongo import MongoClient
from pandas import DataFrame

connection = oracledb.connect(user='NACHO', password='NACHO', host="localhost")
cursor = connection.cursor()
result = cursor.execute('SELECT ID_AUTO FROM AUTOMOVIL ')

result = cursor.fetchall()  

numeros_serie_oracle = []
for vehiculos in result:
    numeros_serie_oracle.append(vehiculos[0])

def get_database():
 
   CONNECTION_STRING = "mongodb://localhost:27017"
 
   client = MongoClient(CONNECTION_STRING)
 
   return client['obligatorio_2']
  
if __name__ == "__main__":   

   dbname = get_database()

collection_name = dbname['mediciones']
print(numeros_serie_oracle)

for num_serie in numeros_serie_oracle:

    item_details = collection_name.find({"numero_serie" : num_serie})
    for item in item_details:
        items_df = DataFrame(item_details)
        print(items_df)