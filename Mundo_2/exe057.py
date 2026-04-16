sexo = str (input('Qual é o seu sexo [F/M/NB]: ')).upper().strip()
s = ('F','M','NB','N-B','FEMININO', 'MASCULINO', 'NÃO-BINÁRIO','NAO-BINARIO')
while sexo not in s:
    print ('Opção inválida. Por favor, informe novamente.')
    sexo = str(input('Qual é o seu sexo [F/M/NB]: ')).upper().strip()
print (f'Sexo {sexo} registado com sucesso.')