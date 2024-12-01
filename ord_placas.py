class Placa:
    def __init__(self, placa: str):
        self.placa = placa
    
    def comp_placa(self, other):
        return self.placa < other.placa

def ler_placas(arquivo_desord: str):
    placas = []
    try:
        with open(arquivo_desord, 'r') as arquivo:
            for linha in arquivo:
                placa = linha.strip()                
               
                if placa and len(placa) == 7:  
                    placas.append(Placa(placa))
                elif placa:
                    print(f"Placa no formato incorreto: {placa}")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_desord}' não foi encontrado.")    
    
    if not placas:
        print("Nenhuma placa válida encontrada no arquivo.")    
    return placas

def escrever_placas(placas, arquivo_ord: str):
    with open(arquivo_ord, 'w') as arquivo:
        for placa in placas:
            arquivo.write(placa.placa + "\n")

def radix_sort(placas):    
    if not placas:
        return []
    
    max_length = len(placas[0].placa)
    
    for i in range(max_length - 1, -1, -1):        
        counting_sort(placas, i)
    return placas

def counting_sort(placas, pos):    
    count = [0] * 256
    output = [None] * len(placas)
    
    for placa in placas:
        count[ord(placa.placa[pos])] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    for placa in reversed(placas):
        index = ord(placa.placa[pos])
        output[count[index] - 1] = placa
        count[index] -= 1
    
    for i in range(len(placas)):
        placas[i] = output[i]

def ordenar_placas(arquivo_entrada, arquivo_saida):
    placas = ler_placas(arquivo_entrada)

    if placas:
        placas = radix_sort(placas)
        escrever_placas(placas, arquivo_saida)
    else:
        print("Não foi possível ordenar as placas devido à falta de placas válidas.")
        