import os
import time
from googlesearch import search
from tqdm import tqdm  # Importa a barra de progresso

def buscar_vagas(cargo, localizacao):
    consulta = f"{cargo} site:linkedin.com/jobs OR site:indeed.com OR site:glassdoor.com {localizacao}"
    print(f"Buscando vagas para: {cargo} em {localizacao}...")
    
    resultados = []
    # Barra de progresso, iterando sobre os 50 resultados
    for url in tqdm(search(consulta, num_results=50), desc="Buscando vagas", total=50, ncols=100, unit="vagas"):
        resultados.append(url)
        time.sleep(2)  # Evita bloqueios temporários
    
    return resultados

def salvar_relatorio(cargo, localizacao, resultados):
    nome_arquivo = f"vagas_{cargo.replace(' ', '_')}_{localizacao.replace(' ', '_')}.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Relatório de Vagas - {cargo} em {localizacao}\n")
        arquivo.write("=" * 50 + "\n\n")
        for i, url in enumerate(resultados, 1):
            arquivo.write(f"{i}. {url}\n")
    print(f"Relatório salvo em: {os.path.abspath(nome_arquivo)}")

def main():
    cargo = input("Digite o cargo, palavra-chave ou empresa: ")
    localizacao = input("Digite a cidade, estado, região ou remoto: ")
    
    resultados = buscar_vagas(cargo, localizacao)
    if resultados:
        salvar_relatorio(cargo, localizacao, resultados)
    else:
        print("Nenhuma vaga encontrada.")

if __name__ == "__main__":
    main()
