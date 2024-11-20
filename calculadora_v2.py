saida=""
def soma(a,b):
    return a+b
def subtracao(a,b):
    return a-b
def multiplica(a,b):
    return a*b
def divisao(a,b):
    if a==0 or b==0:
        print("Não foi possível realizar a divisão por 0")
    else:
     return a/b
def calculadora(a,b,simbolo):
    if simbolo=="+":
       resultado=soma(a,b)
    elif simbolo=="-":
        resultado=subtracao(a,b)
    elif simbolo=="*":
        resultado=multiplica(a,b)
    elif simbolo=="/":
        resultado=divisao(a,b)
    return resultado
while saida!="n":
    a=int(input("Entre com o primeiro valor: "))
    b=int(input("Entre com o segundo valor: "))
    simbolo=str(input("Entre com o simbolo da operação + | - | * | / : "))
    resultado=calculadora(a,b,simbolo)
    print(f"Resultado da operação: {resultado}")
    saida=input("Deseja continuar? S|N  :").lower()
print("Progama encerrado.")