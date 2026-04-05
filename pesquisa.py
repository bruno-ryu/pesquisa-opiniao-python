excelente = 0
ruim = 0

total_entrevistados = 10  # use 10 para testes

for i in range(total_entrevistados):
    print(f"\nEntrevistado {i + 1}")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite a opção: "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1
    elif opiniao == 2:
        pass
    else:
        print("Opção inválida")

print("\n--- RESULTADO FINAL ---")
print("Quantidade de EXCELENTE:", excelente)
print("Quantidade de RUIM:", ruim)