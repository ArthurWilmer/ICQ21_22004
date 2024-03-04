import sympy as sp

# Defina a equação
# equacao = x**4 + 2*x**2 + 1 


# Definindo os símbolos
x = sp.symbols('x')

equacao = x**4 + 2*x**2 + 1

# Resolvendo a equação
solucoes = sp.solve(equacao, x)

# Verificando e exibindo as soluções

print("Sendo I o número imaginário, As soluções da equação são:")
for solucao in solucoes:
    print(solucao)

