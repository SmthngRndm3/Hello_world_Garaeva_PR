import pandas as pd
df = pd.read_csv('wild_boars.csv')

with open ('IQR FM', 'w') as f:
        
    q1 = df.groupby('gender')['length_cm'].quantile(0.25) 
    q3 = df.groupby('gender')['length_cm'].quantile(0.75)
    iqr = q3 - q1 
    f.write(f'Interquartile Range(kg): {iqr} ')