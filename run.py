import os
import csv
import re

"""
Código gerado com Claude Code Sonnet 4.5
"""
def extrair_info_routeros(caminho_arquivo):
    """
    Extrai informações do arquivo de configuração RouterOS.
    
    Returns:
        dict com 'nome_arquivo', 'versao_routeros', 'modelo_router'
    """
    nome_arquivo = os.path.basename(caminho_arquivo)
    versao_routeros = ""
    modelo_router = ""
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            # Ler as primeiras 5 linhas
            for _ in range(5):
                linha = f.readline()
                
                # Extrair versão do RouterOS
                if 'by RouterOS' in linha:
                    match = re.search(r'RouterOS\s+([\d.]+)', linha)
                    if match:
                        versao_routeros = match.group(1)
                
                # Extrair modelo
                if '# model =' in linha:
                    modelo_router = linha.split('=')[1].strip()
        
    except Exception as e:
        print(f"Erro ao processar {nome_arquivo}: {e}")
    
    return {
        'nome_arquivo': nome_arquivo,
        'versao_routeros': versao_routeros,
        'modelo_router': modelo_router
    }

def processar_arquivos(diretorio, arquivo_saida='routers_info.csv'):
    """
    Processa todos os arquivos do diretório e salva em CSV.
    """
    dados = []
    
    # Processar cada arquivo
    for arquivo in os.listdir(diretorio):
        caminho_completo = os.path.join(diretorio, arquivo)
        
        # Processar apenas arquivos (não diretórios)
        if os.path.isfile(caminho_completo):
            print(f"Processando: {arquivo}")
            info = extrair_info_routeros(caminho_completo)
            dados.append(info)
    
    # Salvar em CSV
    if dados:
        with open(arquivo_saida, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['nome_arquivo', 'versao_routeros', 'modelo_router'])
            writer.writeheader()
            writer.writerows(dados)
        
        print(f"\n✓ Dados salvos em: {arquivo_saida}")
        print(f"Total de arquivos processados: {len(dados)}")
    else:
        print("Nenhum arquivo encontrado!")

# Uso
def main():
    # Altere para o seu diretório
    diretorio_arquivos = "./rsc"  # diretório atual, ou especifique o caminho
    
    processar_arquivos(diretorio_arquivos, 'routers_info.csv')

if __name__ == "__main__":
	main()