# Desafio Técnico – Automação de Processos (RPA + Python)
## Objetivo

Este projeto simula um processo de automação logística a partir de um arquivo CSV exportado de um ERP (ex.: Protheus).

O pipeline realiza:

Leitura de pedidos

Criação de fila de contratação de frete por data de embarque

Cálculo de total por cliente

Geração automática de relatório em Excel

Estrutura preparada para automação (execução agendada)

# Arquitetura do Projeto

O projeto foi estruturado seguindo separação de responsabilidades:
```powershell
desafioTecnico/
│
├── data/               # Arquivo CSV de entrada
├── output/             # Relatórios gerados
├── src/ 
│   ├── config.py       # Configurações e paths
│   ├── loader.py       # Camada de leitura de dados
│   ├── processor.py    # Regras de negócio
│   ├── report.py       # Geração de relatório
│   └── automation.py   # Simulação de agendamento
│
├── main.py             # Orquestrador do pipeline
├── requirements.txt
└── README.md
```
# Requisitos

Python 3.10+

pip

# Instalação Passo a Passo

## 1 Clonar o repositório
```bash
git clone https://github.com/WevertonAG/desafioTecnico
cd desafioTecnico
```

Ou baixar e extrair manualmente.

## 2 Criar ambiente virtual
```bash
python -m venv venv
```
Para ativar o venv:
Windows:
```bash
venv\Scripts\activate
```

Linux / Mac:
```bash
source venv/bin/activate
```
Se ativado corretamente, aparecerá (venv) no terminal.

## 3 Instalar dependências
```bash
pip install -r requirements.txt
```

# Dados de Entrada

O arquivo de entrada deve estar em:

data/pedidos.csv

Formato esperado:
```csv
pedido,cliente,data_embarque,produto,quantidade,valor_unitario
1001,Cliente A,2026-02-20,Produto X,10,50
```

# ▶️ Executando o Projeto

Para executar o pipeline completo:
```bash
python main.py
```

## Saída esperada no terminal:

Iniciando pipeline...
Pipeline finalizado com sucesso.

## Saída Gerada

O sistema gera automaticamente:

output/relatorio_fretes.xlsx


O arquivo contém:

Aba 1: Fila_Frete (ordenada por data de embarque)

Aba 2: Total_por_Cliente (agregado para análise em BI)

# Automação (Opcional)

Para simular execução agendada:<br>
```python
from src.automation import start_scheduler
start_scheduler()
```
elas estão comentadas no código basta tirar o comentário

Ou agendar via:

Agendador de Tarefas do Windows

Cron (Linux)

## Decisões Técnicas

Separação em camadas (Loader, Processor, Report)

Uso de ambiente virtual para isolamento

Organização modular para escalabilidade

Preparado para integração com Power BI

Código preparado para testes unitários futuros

## Autor

Desenvolvido como parte de avaliação técnica para vaga de Analista de TI por Weverton Guimarães.
