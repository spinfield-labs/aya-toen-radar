import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pandas as pd
from cmeta_advanced_f4 import compute_cmeta_advanced_f4

# Caminhos dos arquivos
input_file = '../radar/radar_mock_dataset.csv'
output_file = '../radar/radar_output_kprime.csv'

# Leitura dos dados
df = pd.read_csv(input_file)
results = []

# Processamento de cada texto
for index, row in df.iterrows():
    text = row['text']
    entry_id = row.get('thread_id', index)

    result = compute_cmeta_advanced_f4(text)
    result['id'] = entry_id
    result['original_text'] = text
    results.append(result)

# Criação do DataFrame com resultados
df_results = pd.DataFrame(results)
df_results.to_csv(output_file, index=False)
print(f"Radar executado com sucesso. Resultados salvos em: {output_file}")
