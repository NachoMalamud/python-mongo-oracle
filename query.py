from pandas import DataFrame
from main import get_database
dbname = get_database()
 
# Create a new collection
collection_name = dbname['mediciones']
 
item_details = collection_name.find()
for item in item_details:
   # This does not give a very readable output
   items_df = DataFrame(item_details)
   print(items_df)
   print(item['numero_serie'], ['fecha_medida'], ['modelo'], ['temperatura'], ['voltaje'], ['presion'])