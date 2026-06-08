import pandas as pd
df = pd.read_csv('wild_boars.csv')
 
columns = df.columns[2:]
with open ('median of boars', 'w') as f:
    for column in columns: 
        median = df[column].median()
        f.write(f'{column} {median:.2f}\n')