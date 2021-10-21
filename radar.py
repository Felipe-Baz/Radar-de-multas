#declaração da função radar
def radar():

    #recebimento da velocidade
    velocidade = int(input("Qual a velocidade do veiculo:\n"))

    #verifica se houve infração
    if (velocidade > 80): #caso: veiculo acima da velocidade

        #calculo do valor da multa
        valor = float((velocidade - 80)*5)

        #imprime a mensagem de multa no console
        print("Você foi multado em R$ {:.2f}.".format(valor))

#main
if (__name__ == "__main__"):
    radar()