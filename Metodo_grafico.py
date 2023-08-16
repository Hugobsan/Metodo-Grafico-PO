class Equacao:
    def __init__(self, a, b, c):
        #ax + by = c
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        return str(self.a) + "x + " + str(self.b) + "y = " + str(self.c)
class Ponto:
    def __init__(self, x, y, eq1, eq2):
        self.x = x
        self.y = y
        self.eq1 = eq1
        self.eq2 = eq2

    def calculaZ(self):
        global z
        return z.a*self.x + z.b*self.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
# Função que calcula ponto de interseção entre duas equações
def intersec(e1, e2):
    det = e1.a * e2.b - e2.a * e1.b  # Calcula o determinante

    if det == 0:
        return None  # As retas são paralelas ou coincidentes

    x = (e1.c * e2.b - e2.c * e1.b) / det
    y = (e1.a * e2.c - e2.a * e1.c) / det

    p = Ponto(x, y, e1, e2)
    return p

# Teste de crescimento
def testeCrecimento(z):
    print("\n")
    print("-- TESTE DE CRESCIMENTO --")
    print("Este teste verifica se, partindo da origem, o próximo ponto corta x1 (horizontal) ou x2 (vertical)")
    print("\n")

    #se a for maior que b o próximo ponto corta r1 e x1
    if(z.a > z.b):
        print("O próximo ponto corta x1!")
        print("Digite a equação da reta que corta o x1 dentro da área viável, no formato ax + by = c")
        a = int(input("Digite o valor de a: "))
        b = int(input("Digite o valor de b: "))
        c = int(input("Digite o valor de c: "))
        r1 = Equacao(a,b,c)

        print("Reta adicionada:", r1.__str__())

        p = intersec(x1, r1)
    else: #se não, corta r3 e x2
        print("O próximo ponto corta x2!")
        print("Digite a equação da reta que corta o x2 dentro da área viável, no formato ax + by = c")
        a = int(input("Digite o valor de a: "))
        b = int(input("Digite o valor de b: "))
        c = int(input("Digite o valor de c: "))
        r2 = Equacao(a,b,c)

        print("Reta adicionada:", r2.__str__())

        p = intersec(x2, r2)

    return p

# Teste de otimalidade
def testeOtimalidade():
    pontoAtual = vec_p[-2]
    pontoVizinho = vec_p[-1]

    print("\n")
    print("-- TESTE DE OTIMALIDADE --")
    print("Este teste verifica se o ponto atual",pontoAtual.__str__(),"é ótimo, ou se o ponto vizinho é melhor que o ponto atual")
    print("\n")

    #verifica se o penultimo é maior que último ponto em z
    if(pontoAtual.calculaZ() > pontoVizinho.calculaZ()):
        print("O ponto",pontoAtual.__str__(),"é ponto ótimo, e tem como valor ótimo Z =", pontoAtual.calculaZ())
        return pontoAtual
    else:
        print("O ponto vizinho", pontoVizinho.__str__(),"é melhor que o ponto atual", pontoAtual.__str__())
        print("Novo ponto atual:", pontoVizinho.__str__())
        add_vizinho()
        testeOtimalidade()
        return pontoVizinho

#adicionando vizinho
def add_vizinho():
    global vec_p
    #solicitando equação que corta a reta eq2 do ponto atual
    print("\n")
    print("Adicionando vizinho do ponto", vec_p[-1].__str__())
    print("Digite a equação da reta que corta a reta", vec_p[-1].eq2.__str__(), "dentro da área viável, no formato ax + by = c")
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    eq_v = Equacao(a,b,c)
    print("Reta adicionada:", eq_v.__str__())
    print("\n")
    v = intersec(vec_p[-1].eq2, eq_v)
    vec_p.append(v)
    print("Vizinho adicionado:", v.__str__())

#histórico de pontos
vec_p = []

#definindo eixos
x1 = Equacao(0,1,0)
x2 = Equacao(1,0,0)

print("\n")
print("---- Método Gráfico - Pesquisa Operacional ----")
print("\n")

#definindo equação de Z
print("Digite a equação de Maximização de Z, no formato ax + by:")
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
z = Equacao(a,b,0)
print("Z adicionado: Z =", z.a, "x +", z.b, "y")
print("\n")

# Definindo origem
Origem = intersec(x1, x2)
vec_p.append(Origem)
print("Definindo ponto de origem:", Origem.__str__())

# Realizando teste de crescimento
p = testeCrecimento(z)
vec_p.append(p)
print("\n")
print("Ponto atual:", vec_p[-1].__str__())

# Adicionando vizinho 1
add_vizinho()

# Teste de otimalidade (a partir daqui o programa é recursivo, e só para quando o ponto atual é ótimo)
testeOtimalidade()
