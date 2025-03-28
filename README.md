# Bot de Busca de Vagas

Creator: Bruno Alencar  
Date: 27/03/2025 

## Bibliotecas Utilizadas

time,
googlesearch,
tqdm,

## O que o bot faz?

Este bot automatiza a busca por vagas de emprego em diferentes sites de recrutamento, como LinkedIn, Indeed e Glassdoor. Ele funciona da seguinte maneira:

1. **Entrada do usuário**:
   - O usuário informa o cargo desejado.
   - O usuário informa a localização.
   - Opcionalmente, o usuário pode informar um site específico para busca.

2. **Busca no Google**:
   - O bot realiza uma pesquisa no Google utilizando os termos fornecidos pelo usuário.
   - Se nenhum site específico for informado, ele pesquisa em LinkedIn, Indeed e Glassdoor.
   - A biblioteca `googlesearch` retorna até 50 resultados.

3. **Filtragem e salvamento**:
   - O bot verifica se os links encontrados já foram salvos anteriormente.
   - Apenas os novos links são incluídos em um novo relatório.
   - O relatório é salvo em um arquivo de texto no formato `vagas_cargo_localizacao_vX.txt`.

4. **Saída**:
   - O bot informa ao usuário se encontrou novas vagas e exibe o caminho do arquivo salvo.
   - Se nenhuma nova vaga for encontrada, ele não gera um novo relatório.

## Como executar?

Basta rodar o script Python. Ele solicitará as informações necessárias e, ao final, salvará um relatório com os links das vagas encontradas

python script.py


© 2025 BGASoftwares. Todos os direitos reservados
