# -*- coding: utf-8 -*-
import pandas as pd
from io import StringIO
import seaborn as sns
import matplotlib.pyplot as plt

# Os dados CSV fornecidos, agora com os cabeçalhos simplificados para evitar erros
csv_data = """Q6	Q8	Q9	Q10	Q11	Q12
2	2	2	3	2	4
3	2	2	2	2	4
3	2	2	3	2	4
2	2	2	2	2	2
3	1	1	2	2	2
3	3	2	3	2	4
1	2	2	2	2	4
3	2	2	3	1	4
3	3	2	3	2	4
2	2	2	2	1	4
3	3	2	2	2	4
0	3	1	3	2	3
2	3	1	1	1	2
3	3	2	3	1	4
3	2	2	3	2	3
2	3	1	2	2	1
3	2	2	2	2	4
2	2	1	2	2	4
3	1	1	1	2	3
2	2	2	2	2	4
2	2	1	2	2	4
3	3	1	2	2	2
0	2	3	2	1	2
3	3	2	2	2	3
3	2	1	2	2	2
3	2	1	2	2	4
3	2	1	2	2	4
1	2	2	2	2	3
2	1	2	2	2	4
0	3	1	2	1	4
3	2	2	2	2	4
2	3	2	2	1	4
3	2	2	3	2	4
2	2	2	3	2	3
2	2	2	3	2	3
2	2	2	3	2	3
2	2	2	3	2	3
"""

# Define as colunas que serao analisadas
cols_to_analyze = ['Q6', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12']

# Carrega os dados da string CSV
# A codificacao cp1252 é usada para evitar erros de leitura, já que o texto foi corrigido
df = pd.read_csv(StringIO(csv_data), encoding='cp1252', sep='\t')

# Filtra as respostas com valor 0 na Questao Q6, seguindo a metodologia
df_filtered = df[df['Q6'] != 0].copy()

# Converte as colunas relevantes para o tipo numerico
for col in cols_to_analyze:
    df_filtered[col] = pd.to_numeric(df_filtered[col])

# Calcula a matriz de correlacao de Spearman
corr_matrix = df_filtered[cols_to_analyze].corr(method='spearman')

# Cria a matriz de calor (heatmap)
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='viridis', fmt=".2f", linewidths=.5)
plt.title('')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()

# Salva a figura em um arquivo PNG
plt.savefig('matriz_correlacao_spearman_2.png')

# Print the correlation matrix for a text-based output
print("\nMatriz de Correlacao de Spearman:")
print(corr_matrix)