import pandas as pd
df = pd.read_csv('wild_boars.csv')

with open ('coef. var. FM', 'w') as f:
        
    coef_var = (df.groupby('gender')['tusk_length_cm'].std() / df.groupby('gender')['tusk_length_cm'].mean()) * 100
    f.write(f'\nCoefficient of variation: {coef_var}%\n')
    
    
         