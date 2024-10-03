import pandas as pd 
  
gapminder_csv_url ='https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'
# load the data with pd.read_csv 
record = pd.read_csv(gapminder_csv_url) 
  
print('unique no of boroughs are: ',record['Borough'].unique()) 

brooklyn_count = record[record['Borough'] == 'Brooklyn'].shape[0]

# Print the result
print(f"Number of records with Brooklyn Borough: {brooklyn_count}")
