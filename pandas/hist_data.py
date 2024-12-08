import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv('kc_tax.csv')

print(data.columns)
tax_Assessed = data['TaxAssessedValue']

ax = tax_Assessed.hist(bins=20)
ax.plot()