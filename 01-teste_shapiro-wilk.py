# -*- coding: utf-8 -*-
import pandas as pd
from io import StringIO
from scipy.stats import shapiro
import warnings

# Ignorar avisos que podem ocorrer em amostras pequenas
warnings.filterwarnings('ignore')

# Os dados numéricos das respostas das questões
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
df = pd.read_csv(StringIO(csv_data), sep='\t')

# Converte as colunas relevantes para o tipo numérico
for col in cols_to_analyze:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Filtra as respostas com valor 0 na Questão Q6 para a análise de normalidade
df_filtered_q6 = df[df['Q6'] != 0].copy()

# Realiza o Teste de Shapiro-Wilk para cada coluna
print("Resultados do Teste de Shapiro-Wilk:")
for col in cols_to_analyze:
    stat, p_value = shapiro(df_filtered_q6[col])
    conclusion = "Nao Normal" if p_value <= 0.05 else "Normal"

    print(f"Questao {col}: W-statistic={stat:.3f}, p-valor={p_value:.3f} -> Conclusao: {conclusion}")

