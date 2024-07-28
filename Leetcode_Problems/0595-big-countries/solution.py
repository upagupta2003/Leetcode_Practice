import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    #select name, population, area from world where population >= 25000000 or area >= 3000000;
    df = world[['name','population','area']]
    df = df[(df['population'] >= 25000000 ) | (df['area'] >= 3000000)]
    return df


