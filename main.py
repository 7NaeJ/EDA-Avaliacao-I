from ord_placas import ler_placas, ordenar_placas

def main():    
    a_entrada = "PIVs-1000000.piv"    
    a_saida = "placas_ordenadas1M.piv"    
   
    placas = ler_placas(a_entrada)    
    
    if not placas:
        print("Erro: Não há placas válidas para ordenar.")
        return    

    ordenar_placas(a_entrada, a_saida)    
    
    print("Conteúdo do arquivo de saída (placas ordenadas):")
    with open(a_saida, 'r') as f:
        print(f.read())

if __name__ == "__main__":
    main()