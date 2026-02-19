import pandas as pd

def process_data(df: pd.DataFrame):
    df["data_embarque"] = pd.to_datetime(df["data_embarque"])
    df["total_item"] = df["quantidade"] * df["valor_unitario"]

    fila_frete = df.sort_values(by="data_embarque")

    total_cliente = (
        df.groupby("cliente")["total_item"]
        .sum()
        .reset_index()
    )

    return fila_frete, total_cliente
