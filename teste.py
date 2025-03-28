import os
import time
from googlesearch import search
from tqdm import tqdm

def buscar_vagas(cargo, localizacao, site_filtro=""):
    if site_filtro.strip() == "":
        consulta = f"{cargo} {localizacao} linkedin OR indeed OR glassdoor"
    else:
        consulta = f"{cargo} {localizacao} {site_filtro.strip()}"

    print(f"Buscando vagas para: {cargo} em {localizacao} no site {site_filtro or 'todos os sites'}...")

    resultados = []
    try:
        for url in tqdm(search(consulta, num_results=50), desc="Buscando vagas", total=50, ncols=100, unit="vagas"):
            if url.startswith("http"):
                resultados.append(url)
            time.sleep(5)
    except Exception as e:
        print(f"Ocorreu um erro na busca: {e}")
    
    return resultados

def carregar_links_existentes(nome_base):
    """Carrega os links do primeiro relatório encontrado."""
    versao = 1
    nome_arquivo = f"{nome_base}_v{versao}.txt"
    links_existentes = set()
    
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                if linha.startswith("http"):
                    links_existentes.add(linha.strip())
    
    return links_existentes

def salvar_relatorio(cargo, localizacao, resultados):
    nome_base = f"vagas_{cargo.replace(' ', '_')}_{localizacao.replace(' ', '_')}"
    links_existentes = carregar_links_existentes(nome_base)
    
    novos_links = [url for url in resultados if url not in links_existentes]
    
    if not novos_links:
        print("Nenhum novo link encontrado. Relatório não será gerado.")
        return
    
    # Certificar-se de que a pasta 'relatorios' existe
    pasta_relatorios = "relatorios"
    if not os.path.exists(pasta_relatorios):
        os.makedirs(pasta_relatorios)

    versao = 1
    while os.path.exists(f"{pasta_relatorios}/{nome_base}_v{versao}.txt"):
        versao += 1
    
    nome_arquivo = f"{pasta_relatorios}/{nome_base}_v{versao}.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Relatório de Vagas - {cargo} em {localizacao} (Versão {versao})\n")
        arquivo.write("=" * 50 + "\n\n")
        for i, url in enumerate(novos_links, 1):
            arquivo.write(f"{i}. {url}\n")
    
    print(f"Novo relatório salvo em: {os.path.abspath(nome_arquivo)}")

def main():
    cargo = input("Digite o cargo, palavra-chave ou empresa: ")
    localizacao = input("Digite a cidade, estado, região ou remoto: ")
    site_filtro = input("Digite o nome do site para busca (deixe em branco para buscar em todos): ")
    
    resultados = buscar_vagas(cargo, localizacao, site_filtro)
    if resultados:
        salvar_relatorio(cargo, localizacao, resultados)
    else:
        print("Nenhuma vaga encontrada.")

if __name__ == "__main__":
    main()
