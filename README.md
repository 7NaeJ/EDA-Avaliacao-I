# EDA-Avaliacao-I
Primeira avaliação da disciplina EDA 2024.2

## Descrição do Projeto

O código desenvolvido para esta atividade realiza os seguintes procedimentos:

1. Abertura de um arquivo externo contendo placas de veículos desordenadas.
2. Verificação do formato das placas.
3. Leitura das placas.
4. Ordenação das placas.
5. Escrita das placas ordenadas em outro arquivo.
6. Geração de um arquivo de saída com as placas ordenadas.

O método de ordenação escolhido foi o **Radix Sort**, auxiliado pelo **Counting Sort** como sub-rotina. O Radix Sort possui complexidade de **O(n*k)**, onde:
- **n** é o número de elementos da lista.
- **k** é o número de caracteres de cada item.

Levando em consideração que a quantidade de dígitos da placa é fixa, o Radix Sort passa a ter complexidade **O(n)**, sendo mais eficiente que o Quick Sort ou Merge Sort.

## Composição do Código

### Main.py
Arquivo principal utilizado para testar o código que contém as classes e funções desenvolvidas. Ele é composto por uma função principal que realiza os seguintes passos:
- Recebe o arquivo que contém as placas desordenadas.
- Faz a leitura desse arquivo.
- Ordena as placas presentes no arquivo.
- Retorna uma saída com outro arquivo contendo as placas ordenadas.

Além disso, o arquivo **main.py** verifica se existem placas no arquivo aberto. Caso não haja, ele retornará uma mensagem informando o problema.

### Ord_placas.py
Arquivo que contém as classes e funções executadas pelo **main.py**. Composto pela classe **Placa** e funções de leitura, gravação e ordenação de placas.

#### Classe **Placa**
- Criada para receber a placa de um veículo.
- Contém o método `__init__`, que constrói a classe e recebe o parâmetro **placa** do tipo string, que será armazenado.
- Contém também o método `comp_placa`, que realiza o comparativo das placas de maneira lexicográfica.

#### Funções

- **Ler_placas**: 
  Função responsável por abrir e ler o arquivo contendo as placas desordenadas. Verifica se as placas possuem a quantidade certa de caracteres e se o arquivo contém quebras de linha, as quais devem ser removidas com a função `strip`.
  
- **Escrever_placas**:
  Função que escreve as placas no arquivo de saída.

- **Radix_sort**:
  Função que realiza a ordenação das placas utilizando o **Counting Sort** como sub-rotina para auxiliar na ordenação.

- **Ordenar_placas**:
  Função chamada no arquivo **main.py**, responsável por realizar todo o processo de leitura, ordenação e escrita das placas ordenadas.

## Fluxo do Processo

1. O código começa abrindo um arquivo `.piv` que contém as placas desordenadas.
2. O código então ordena as placas utilizando o algoritmo **Radix Sort**.
3. No final do processo, ele gera um arquivo `.piv` contendo as placas ordenadas.
