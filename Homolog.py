import os
import time
from googlesearch import search
from tqdm import tqdm

def buscar_vagas(cargo, localizacao, site_filtro=""):
    # Se site_filtro estiver vazio, buscar em todos os sites definidos
    if site_filtro.strip() == "":
        consulta = f"{cargo} {localizacao} linkedin OR indeed OR glassdoor"
    else:
        consulta = f"{cargo} {localizacao} {site_filtro.strip()}"

    print(f"Buscando vagas para: {cargo} em {localizacao} no site {site_filtro or 'todos os sites'}...")

    resultados = []
    # Barra de progresso, iterando sobre os 20 resultados (reduzido)
    try:
        for url in tqdm(search(consulta, num_results=20), desc="Buscando vagas", total=20, ncols=100, unit="vagas"):
            if url.startswith("http"):
                resultados.append(url)
            time.sleep(5)  # Aumentando o tempo de espera para evitar bloqueio
    except Exception as e:
        print(f"Ocorreu um erro na busca: {e}")
    
    return resultados

def salvar_relatorio(cargo, localizacao, resultados):
    nome_arquivo = f"vagas_{cargo.replace(' ', '_')}_{localizacao.replace(' ', '_')}.txt"
    if resultados:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(f"Relatório de Vagas - {cargo} em {localizacao}\n")
            arquivo.write("=" * 50 + "\n\n")
            for i, url in enumerate(resultados, 1):
                arquivo.write(f"{i}. {url}\n")
        print(f"Relatório salvo em: {os.path.abspath(nome_arquivo)}")
    else:
        print("Nenhuma vaga encontrada para o critério informado.")

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
