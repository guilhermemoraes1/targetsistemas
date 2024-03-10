def verifica_fibonacci(numero):
    a = 0
    b = 1

    while b < numero:
        temp = b
        b = a + b
        a = temp

    if b == numero:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

entrada = 8
resposta = verifica_fibonacci(entrada)
print(resposta)