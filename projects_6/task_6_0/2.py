import pandas as pd
df = pd.read_csv('wild_boars.csv')
 
columns = df.columns[2:]
with open ('averge all about boars', 'w') as f:
    for column in columns: 
        average = df[column].mean()
        f.write(f'{column} {average:.2f}\n')