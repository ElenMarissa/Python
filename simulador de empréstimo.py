while True:
    print("-------------------------------")
    print("  Seja bem-vindo(a) ao Mybank  ")
    print("    SIMULADOR DE INVESTIMENTO    ")
    print("-------------------------------")

    print ("Titulos disponiveis:")
    print ("1 - Tesouro Prefixado 2024")
    print ("2 - Tesouro Prefixado 2026")

    cliente = str(input("Qual titulo você gostaria de fazer uma simulação?: "))
    if cliente == '1':
        investimento = float(input("Qual o valor que você quer investir?: "))
        invmes = float(input("Se você for investir todo o mês, qual o valor?: "))

    # calculo do valor total investido
        aporte = 32
        mult = invmes * aporte
        totalinv = mult + investimento

    # calculo do valor bruto
        rent = totalinv / investimento
        valor = totalinv * (rent / 100)
        valorbruto = valor + totalinv

    # calculo I.R:
    #Até 180 dias: 22,5%
    #De 181 a 360 dias: 20%
    #De 361 a 720 dias: 17,5%
    #A partir de 721 dias: 15%
        IR = (valorbruto - totalinv) * 0.15
    
    # calculo B3:
    # 3% de emolumentos
        B3 = (valorbruto - totalinv) * 0.03
    
    # calculo valor líquido
        valorliquido = valorbruto - (IR + B3)

    else:   
        investimento = float(input("Qual o valor que você quer investir?: "))
        invmes = float(input("Se você for investir todo o mês, qual o valor?: "))
        aporte = 50
        mult = invmes * aporte
        totalinv = mult + investimento
        rent = totalinv / investimento
        valor = totalinv * (rent / 100)
        valorbruto = valor + totalinv
        IR = (valorbruto - totalinv) * 0.15
        B3 = (valorbruto - totalinv) * 0.05
        valorliquido = valorbruto - (IR + B3)

    print("-------------------------------")
    print("   RESULTADO DA SIMULAÇÃO      ")
    print("-------------------------------")
    print("Valor inicial investido: ", investimento)
    print("Aportes de",invmes,"por",aporte,"meses")
    print("Valor total investido ",totalinv)
    print("-------------------------------")
    print("Valor Bruto: ",valorbruto)
    print("I.R.:", IR)
    print("Taxa da B3:", B3)
    print("Valor Líquido: ",valorliquido)
    print("-------------------------------")

    recomecar = str(input("Deseja realizar outra simulação? s/n: "))
    if recomecar == 'n':
        break
print("Programa encerrado")