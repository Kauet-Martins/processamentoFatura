import openpyxl

def carregar_planilha(caminho_planilha):
    """Carrega a planilha Excel e retorna a planilha e índice da coluna UC."""
    wb = openpyxl.load_workbook(caminho_planilha)
    ws = wb.active

    cabecalho = [cell.value.strip() if cell.value else "" for cell in ws[1]]
    try:
        indice_coluna_uc = cabecalho.index("UNIDADE CONSUMIDORA")
    except ValueError:
        raise Exception("Coluna 'Unidade Consumidora' não encontrada na planilha.")

    return wb, ws, indice_coluna_uc
