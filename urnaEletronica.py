print ('URNA ELETRONICA')
print ('1 - Joao')
print ('2 - Jose')
print ('3 - Jaco')
print ('4 - Jobe')
print ('5 - Voto Nulo')
print ('6 - Voto em Branco')

votosJoao = votosJose = votosJaco = votosJobe = votoNulo = votoBranco = 0
codigo = 1

    #    Verdadeiro      Verdadeiro
while (codigo >=1  and codigo <= 6):  #Verdadeiro
   codigo = int(input('Informe a opcao ou zero para encerrar: '))
   if (codigo >= 1 and codigo <= 6):
        if (codigo == 1):
            votosJoao += 1
        elif (codigo == 2):
            votosJose = votosJose + 1
        elif (codigo == 3):
            votosJaco += 1
        elif (codigo == 4):
            votosJobe += 1
        elif (codigo == 5):
            votoNulo += 1
        elif (codigo == 6):
            votoBranco += 1
print ('RESULTADO:')
print ('1 - Joao - votos' ,votosJoao)
print ('2 - Jose - votos',votosJose)
print ('3 - Jaco - votos',votosJaco)
print ('4 - Jobe - votos',votosJobe)
print ('5 - votos nulos',votoNulo)
print ('6 -  votos em branco',votoBranco)