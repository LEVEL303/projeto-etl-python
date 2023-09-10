# ========================== EXTRACT ===========================

import pandas as pd

df = pd.read_csv('planilha.csv')
print(df)

# ======================== TRANSFORM ===========================

df.loc[df['vendas'] >= 1000, "bonus"] = 200.0
df['pagamento'] = df['salario'] + df['bonus']
print(df)

# =========================== LOAD =============================

df.to_csv('planilha.csv', index=False)
