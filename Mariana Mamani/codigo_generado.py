def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def imprimir_primos(hasta):
    print(f"Números primos del 1 al {hasta}:")
    for numero in range(1, hasta + 1):
        if es_primo(numero):
            print(numero, end=" ")

if __name__ == "__main__":
    imprimir_primos(100)
