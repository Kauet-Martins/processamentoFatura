# 📊 Projeto de Automação de Processamento de Faturas

Este projeto tem como objetivo automatizar a extração de informações de faturas em PDF e preenchê-las em uma planilha Excel.

## 🚀 Funcionalidades
- Extração automática de **Unidade Consumidora** e **Valor Total a Pagar** de arquivos PDF.
- Comparação e inserção dos dados na planilha conforme a Unidade Consumidora.
- Suporte a múltiplos arquivos PDF.

## 🛠️ Requisitos
Certifique-se de ter instalado:

- Python 3.8+
- Bibliotecas necessárias:
  ```bash
  pip install pymupdf openpyxl
  ```

## 📂 Estrutura do Projeto
```
📁 projeto-faturas
│── 📂 pdfs/  # Pasta contendo os arquivos PDF
│── 📂 data/  # Pasta para armazenar a planilha
│── 📜 extractor.py  # Módulo para extração de dados do PDF
│── 📜 spreadsheet.py  # Módulo para manipulação da planilha
│── 📜 main.py  # Arquivo principal para executar o script
│── 📜 .env  # Configuração de variáveis de ambiente
│── 📜 README.md  # Documentação do projeto
```

## 📌 Como Usar
1. Coloque os arquivos PDF na pasta `pdfs/`.
2. Configure o caminho da planilha em `.env`:
   ```env
   PASTA_PDFS=./pdfs
   PLANILHA=./data/planilha.xlsx
   ```
3. Execute o script:
   ```bash
   python main.py
   ```

## 🛡️ Segurança
- **NÃO** armazene informações sensíveis no código.
- Utilize `.gitignore` para ignorar arquivos como `.env` e planilhas locais.
- Faça backup da planilha antes de executar o script.

## 🤝 Contribuição
Pull Requests são bem-vindos! Siga o padrão de código e adicione documentação quando necessário.

## 📜 Licença
Este projeto está sob a licença MIT.

