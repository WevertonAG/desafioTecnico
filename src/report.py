import pandas as pd
from .config import OUTPUT_FILE, OUTPUT_DIR

def generate_report(fila_frete, total_cliente):
    OUTPUT_DIR.mkdir(exist_ok=True)

    with pd.ExcelWriter(OUTPUT_FILE) as writer:
        fila_frete.to_excel(writer, sheet_name="Fila_Frete", index=False)
        total_cliente.to_excel(writer, sheet_name="Total_por_Cliente", index=False)
