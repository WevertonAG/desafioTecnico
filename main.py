from src.loader import load_data
from src.processor import process_data
from src.report import generate_report
#from src.automation import start_scheduler

def run_pipeline():
    print("Iniciando pipeline...")
    df = load_data()
    fila, total = process_data(df)
    generate_report(fila, total)  
    #start_scheduler()
    print("Pipeline finalizado com sucesso.")

if __name__ == "__main__":
    run_pipeline()
