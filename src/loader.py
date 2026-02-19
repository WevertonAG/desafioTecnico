import pandas as pd
from .config import DATA_PATH

def load_data():
    try:
        df = pd.read_csv(DATA_PATH)
        return df
    except Exception as e:
        raise RuntimeError(f"Erro ao carregar dados: {e}")
