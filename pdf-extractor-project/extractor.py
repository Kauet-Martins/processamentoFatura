import fitz  # PyMuPDF
import re

def extract_data_from_pdf(pdf_path):
    """Extrai a Unidade Consumidora e o Valor Total de um PDF."""
    doc = fitz.open(pdf_path)
    unidade_consumidora, valor_total = None, None
    linhas = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        linhas.extend(page.get_text("text").split("\n"))

    for i, linha in enumerate(linhas):
        if "UNIDADE CONSUMIDORA" in linha.upper():
            partes = re.findall(r"\d+", linha)
            if partes:
                unidade_consumidora = partes[0].lstrip("0")
            elif i + 1 < len(linhas):
                partes = re.findall(r"\d+", linhas[i + 1])
                if partes:
                    unidade_consumidora = partes[0].lstrip("0")

    for i, linha in enumerate(linhas):
        if re.search(r"\bTOTAL\s*A\s*PAGAR\b", linha, re.IGNORECASE):
            for j in range(i, min(i + 3, len(linhas))):
                match_valor = re.search(r"(\d{1,3}(\.\d{3})*,\d{2})", linhas[j])
                if match_valor:
                    valor_total = match_valor.group(1).replace(".", "").replace(",", ".")
                    break  

    return unidade_consumidora, valor_total
