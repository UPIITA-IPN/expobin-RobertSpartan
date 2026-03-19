import sys

def calcular_exponenciacion_modular(base, exponente, modulo):
    if modulo == 1:
        return 0
    if exponente < 0:
        base = pow(base, -1, modulo)
        exponente = -exponente
    resultado = 1
    base %= modulo
    while exponente > 0:
        if exponente & 1:
            resultado = (resultado * base) % modulo
        exponente >>= 1
        base = (base * base) % modulo
    return resultado

def main():
    if len(sys.argv) == 4:
        base = int(sys.argv[1])
        exponente = int(sys.argv[2])
        modulo = int(sys.argv[3])
    else:
        base = int(input('base: '))
        exponente = int(input('exponente: '))
        modulo = int(input('modulo: '))
    if modulo <= 0:
        print('El módulo debe ser mayor que 0')
        return
    print(calcular_exponenciacion_modular(base, exponente, modulo))

if __name__ == '__main__':
    main()
