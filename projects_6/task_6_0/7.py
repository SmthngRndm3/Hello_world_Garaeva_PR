import pandas as pd
df = pd.read_csv('wild_boars.csv')

columns = df.columns[2:]

with open ('variance etc.', 'w') as f:
    for column in columns:
        f.write(f'{column}:\nVariance(^2): {df[column].var():.1f}')
        f.write(f'\nStandart deviation: {df[column].std():.1f}')
        coef_var = (df[column].std() / df[column].mean()) * 100
        f.write(f'\nCoefficient of variation: {coef_var:.1f}%\n\n')