
import pandas as pd
from cmeta_advanced_f4 import compute_cmeta_advanced_f4 as compute_cmeta_advanced

# Caminho do dataset de entrada e saída
input_file = '../radar/radar_mock_dataset.csv'
output_file = '../radar/radar_output_kprime.csv'

# Leitura do dataset
df = pd.read_csv(input_file)

# Inicialização da lista de resultados
results = []

# Extração dos textos e IDs
texts = df['original_text'].tolist()
ids = df['id'].tolist()

# Processamento de cada texto
for entry_id, text in zip(ids, texts):
    cmeta_value = compute_cmeta_advanced(text)
    result = {
        'id': entry_id,
        'original_text': text,
        'C_meta': cmeta_value
    }
    results.append(result)

# Criação do novo DataFrame e exportação para CSV
output_df = pd.DataFrame(results)
output_df.to_csv(output_file, index=False)

print("Radar executado com sucesso. Resultados salvos em:", output_file)
