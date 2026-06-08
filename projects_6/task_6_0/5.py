import pandas as pd
df = pd.read_csv('wild_boars.csv')

columns = df.columns[4:]

with open ('Percentiles', 'w') as f:
    for column in columns:
        f.write(f'{column}:\nPercentile 25 (Q1): {df[column].quantile(0.25):.1f}')
        f.write(f'\nMediane 50 (Q2): {df[column].quantile(0.5):.1f}')
        f.write(f'\nPercentile 75 (Q3): {df[column].quantile(0.75):.1f}\n\n')
    
