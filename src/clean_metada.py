import json

# Ruta a tu notebook
notebook_path = "notebooks/MRP_StockOut_Prediction.ipynb"

# Leer el notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Limpiar metadatos problemáticos
if 'metadata' in notebook:
    # Eliminar widgets problemáticos
    if 'widgets' in notebook['metadata']:
        del notebook['metadata']['widgets']
    
    # Limpiar otros metadatos problemáticos
    if 'execution' in notebook['metadata']:
        del notebook['metadata']['execution']

# Guardar el notebook limpio
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print("Notebook limpiado exitosamente!")