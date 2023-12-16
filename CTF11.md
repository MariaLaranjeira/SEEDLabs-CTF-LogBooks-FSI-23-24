Através da leitura do enunciado, retiraram-se as seguintes conclusões a utilizar na eleboração do ataque:
- p = primo próximo de 2^512
- q = primo próximo de 2^513
- n = p*q
- ed % (p-1)(q-1) = 1, o que resolvido em ordem a d, resulta em: d = pow(e, -1, ((p-1)*(q-1)))

De modo a encontrar p e q utilizou-se o algoritmo aconselhado no enunciado, o algoritmo de Miller-Rabin:

```python
def isPrime(n):
    if n!=int(n):
        return False
    n=int(n)
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
        
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
  
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True
```

Posteriormente, elaborou-se a função search. A função começa por definir os pontos de partida para p e q. O p começa em 2**512 e o q começa em 2**513. Se estes números forem pares, são incrementados em 1 para garantir que se começa com um número ímpar, já que todos os números primos, exceto o 2, são ímpares. A função então itera sobre os números ímpares começando por p. Para cada p, a função primeiro verifica se p é primo usando a função is_Prime. Se p for primo, a função verifica se p é um divisor de n. Isso é feito calculando n % p. Se o resultado for 0, isso significa que p é um divisor de n. Então, q é calculado diretamente como n // p. Após encontrar um q candidato, a função verifica se q é maior ou igual a 2**513 e se é um número primo. Se estas condições forem verdadeiras, então foram encontrados os fatores p e q que se procurava e a função retorna p e q. Se a função terminar sem encontrar esses fatores, é retornado None, None.


```python
def search(n):
    p_start = 2**512
    q_start = 2**513

    if p_start % 2 == 0:  # Make sure we start from an odd number
        p_start += 1
    if q_start % 2 == 0:
        q_start += 1

    for p in range(p_start, 2**513, 2):  # Iterate over odd numbers
        if not isPrime(p):
            continue

        if n % p == 0:  # If p is a divisor of n
            q = n // p
            if q >= q_start and isPrime(q):
                return p, q

    return None, None
```

Por fim, calculou-se d usando a fórmula já mencionada e descodificou-se o ciphertext usando a função dec já fornecida. Como o ciphertext é dado em base hexadecimal, utilizou-se unhexlify no ciphertext para ser decifrado. Deu-se print ao resultado da descodificação e obteve-se a flag.

NOTA: O código completo usado neste ataque pode ser encontrado na pasta Code.


