import pandas as pd
df = pd.read_csv('wild_boars.csv')
 
columns = df.columns[1:]
with open ('mode of boars', 'w') as f:
    for column in columns: 
        mode = df[column].mode().values
        
        f.write(f'{column} {mode}\n')