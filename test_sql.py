import pandas as pd
from mysql_connector import engine

# Five most populated cities in the world
cities = ['Tokyo', 'Delhi', 'Shanghai',
          'São Paulo', 'Mexico City']
# and their countries
countries = ['Japan', 'India', 'China',
             'Brazil', 'Mexico']
# the continents they are located in
continents = ['Asia', 'Asia', 'Asia',
              'North America', 'South America']
# and their populations
population = [37468000, 28514000, 25582000,
              21650000, 21581000]

# Create Pandas DataFrame
largest_cities_df = pd.DataFrame({
    "City":  cities,
    "Country": countries,
    "Continent": continents,
    "Population": population
})

with engine.begin() as conn:
    # Invoke DataFrame method to_sql() to
    # create the table 'largest_cities' and
    # insert all the DataFrame rows into it
    largest_cities_df.to_sql(
        name='largest_cities', # database table
        con=conn, # database connection
        index=False # Don't save index
    )