import arcade
import time

print("\nVALORES MENOS QUE 500 PARA O TAMANHO DA TELA PODEM CORTAR O DESENEHO!!")

screen_width = int(input("\nDigite a largura da tela: "))  # Valor que define a largula da tela da imagem
screen_height = int(input("Digite a altura da tela: "))  # Valor que define a altura da tela da imagem

name_draw = str(input("\nDigite o nome do desenho: "))  # Define o nome do desenho
# Funçao que recedo os dados anteriores para formar a tela da imagem
arcade.open_window(screen_width, screen_height, "{}".format(name_draw))

# http://arcade.academy/arcade.color.html link que comtem os valores de cada cor no seguinte formato (cor1, cor2, cor3)
print("\nAcesse {} para ver as possiveis cores".format('http://arcade.academy/arcade.color.html'))

"""
Variavel que define o primerio valor do conjunto de cores para formar uma unica cor
"""
print("\nDigite a cor de fundo do desenho apenas os numeros: ")
cor_t1 = int(input("Digite o primeiro valor da cor: "))
if cor_t1 < 0 or cor_t1 > 255:
    print("\nValor para a cor 1 é invalido!! {}".format(cor_t1))
    cont = 0  # Contador do while
    while cor_t1 < 0 or cor_t1 > 255:
        cor_t1 = int(input("\nDigite novamente: "))
        if 0 < cor_t1 <= 255:
            print("\nValor correto! {}".format(cor_t1))
            break
    cont += 1

"""
Variavel que define o segundo valor do conjunto de cores para formar uma unica cor
"""
cor_t2 = int(input("Digite o segundo valor da cor: "))
if cor_t2 < 0 or cor_t2 > 255:
    print("\nValor para a cor 2 é invalido!! {}".format(cor_t2))
    cont = 0  # Contador do while
    while cor_t2 < 0 or cor_t2 > 255:
        cor_t2 = int(input("\nDigite novamente: "))
        if 0 < cor_t2 <= 255:
            print("\nValor correto! {}".format(cor_t2))
            break
    cont += 1

"""
Variavel que define o terceiro valor do conjunto de cores para formar uma unica cor
"""

cor_t3 = int(input("Digite o primeiro valor: "))
if cor_t3 < 0 or cor_t3 > 255:
    print("\nValor para a cor 3 é invalido!! {}".format(cor_t3))
    cont = 0  # Contador do while
    while cor_t3 < 0 or cor_t3 > 255:
        cor_t3 = int(input("\nDigite novamente: "))
        if 0 < cor_t3 <= 255:
            print("\nValor correto! {}".format(cor_t3))
            break
    cont += 1

# Funcao que recebo os 3 valores anterios para formar a cor da tela de fundo
arcade.set_background_color((cor_t1, cor_t2, cor_t3))

arcade.start_render()  # Inicia o processo de renderixação da tela, que deve ser feito antes dos comandos de desenhar

"""
Variavel que define a primeira cor do conjunto de cores para pintar o rosto do desenho
"""
cor_f1 = int(input("\nDigite o valor 1 para a cor da face: "))
if cor_f1 < 0 or cor_f1 > 255:
    print("\nValor para a cor 1 é invalido!! {}".format(cor_f1))
    cont = 0  # Contador do while
    while cor_f1 < 0 or cor_f1 > 255:
        cor_f1 = int(input("\nDigite novamente: "))
        if 0 < cor_f1 <= 255:
            print("\nValor correto! {}".format(cor_f1))
            break
    cont += 1

"""
Variavel que define a segunda cor do conjunto de cores para pintar o rosto do desenho
"""
cor_f2 = int(input("Digite o valor 2 para a cor da face: "))
if cor_f2 < 0 or cor_f2 > 255:
    print("\nValor para a cor 1 é invalido!! {}".format(cor_f2))
    cont = 0  # Contador do while
    while cor_f2 < 0 or cor_f2 > 255:
        cor_f2 = int(input("\nDigite novamente: "))
        if 0 < cor_f2 <= 255:
            print("\nValor correto! {}".format(cor_f2))
            break
    cont += 1

"""
Variavel que define a terceira cor do conjunto de cores para pintar o rosto do desenho
"""
cor_f3 = int(input("Digite o valor 2 para a cor da face: "))
if cor_f3 < 0 or cor_f3 > 255:
    print("\nValor para a cor 1 é invalido!! {}".format(cor_f3))
    cont = 0  # Contador do while
    while cor_f3 < 0 or cor_f3 > 255:
        cor_f3 = int(input("\nDigite novamente: "))
        if 0 < cor_f3 <= 255:
            print("\nValor correto! {}".format(cor_f3))
            break
    cont += 1

# O valoes de x e y tem q ser iguais
print("\nOBS: Os dois valores a seguir tem que ser iguais!!")
time.sleep(3)  # Deley de 3 segundo, depois o codigo roda normalmente
# Valor que define a posicao do centro do rosto no eixo x
x = int(input("Digite o valor da posicão do circulo (no eixo horizontal): "))
# Valor que define a posicao do centro do rosto no eixo y
y = int(input("Digite o valor da posicão do circulo (no eixo vertical): "))
if x != y and y != x:  # Se os valores forem diferentes o formato do rosto ficara estranho
    cont = 0
    while x != y or y != x:
        print("Os valores são iguais digite novamente...")
        x = int(input("\nDigite o valor da posicão do circulo (no eixo horizontal): "))
        y = int(input("Digite o valor da posicão do circulo (no eixo vertical): "))
        if x == y and y == x:
            print("Valores validos!!")
            break
    cont += 1

radius = int(input("\nDigite o tamanho da largura do desenho: "))  # Defino o tamanho do raio do rosto
if radius > 200:  # Se o valor for maior que 200 nao ira caber na tela
    print("\nO rosto nao cabe na tela!!")
    cont = 0
    while radius > 200:
        radius = int(input("\nDigite o tamanho da largura do desenho novamente: "))
        if radius < 200:
            print("\nValor Correto!!")
            break
    cont += 1

"""
Funçao responsavel em formar uma circunferenia com os valore de x, y e radius e a cor com os valores cor_f1, 
cor_f2, cor_f3 
"""
arcade.draw_circle_filled(x, y, radius, (cor_f1, cor_f2, cor_f3))

# Draw the right eye
x = 370
y = 350
radius = 20
"""
Variavel que define a primeira cor do conjunto de cores para pintar o olho direito
"""
cor_a1 = int(input("\nDigite o valor 1 para a cor da face: "))
if cor_a1 < 0 or cor_a1 > 255:
    print("\nValor para a cor 1 é invalido!! {}".format(cor_a1))
    cont = 0  # Contador do while
    while cor_a1 < 0 or cor_a1 > 255:
        cor_a1 = int(input("\nDigite novamente: "))
        if 0 < cor_a1 <= 255:
            print("\nValor correto! {}".format(cor_a1))
            break
    cont += 1

"""
Variavel que define a segunda cor do conjunto de cores para pintar o olho direito
"""
cor_a2 = int(input("Digite o valor 2 para a cor da face: "))
if cor_a2 < 0 or cor_a2 > 255:
    print("\nValor para a cor 1 é invalido!! {}".format(cor_a2))
    cont = 0  # Contador do while
    while cor_a2 < 0 or cor_a2 > 255:
        cor_a2 = int(input("\nDigite novamente: "))
        if 0 < cor_a2 <= 255:
            print("\nValor correto! {}".format(cor_a2))
            break
    cont += 1

"""
Variavel que define a terceira cor do conjunto de cores para pintar o olho direito
"""
cor_a3 = int(input("Digite o valor 2 para a cor da face: "))
if cor_a3 < 0 or cor_a3 > 255:
    print("\nValor para a cor 1 é invalido!! {}".format(cor_a3))
    cont = 0  # Contador do while
    while cor_a3 < 0 or cor_a3 > 255:
        cor_a3 = int(input("\nDigite novamente: "))
        if 0 < cor_a3 <= 255:
            print("\nValor correto! {}".format(cor_a3))
            break
    cont += 1
arcade.draw_circle_filled(x, y, radius, (cor_a1, cor_a2, cor_a3))

# Draw the left eye
x = 230
y = 350
radius = 20
"""
Variavel que define a primeira cor do conjunto de cores para pintar o olho esquerdo
"""
cor_a1 = int(input("\nDigite o valor 1 para a cor da face: "))
if cor_a1 < 0 or cor_a1 > 255:
    print("\nValor para a cor 1 é invalido!! {}".format(cor_a1))
    cont = 0  # Contador do while
    while cor_a1 < 0 or cor_a1 > 255:
        cor_a1 = int(input("\nDigite novamente: "))
        if 0 < cor_a1 <= 255:
            print("\nValor correto! {}".format(cor_a1))
            break
    cont += 1

"""
Variavel que define a segunda cor do conjunto de cores para pintar o olho esquerdo
"""
cor_a2 = int(input("Digite o valor 2 para a cor da face: "))
if cor_a2 < 0 or cor_a2 > 255:
    print("\nValor para a cor 1 é invalido!! {}".format(cor_a2))
    cont = 0  # Contador do while
    while cor_a2 < 0 or cor_a2 > 255:
        cor_a2 = int(input("\nDigite novamente: "))
        if 0 < cor_a2 <= 255:
            print("\nValor correto! {}".format(cor_a2))
            break
    cont += 1

"""
Variavel que define a terceira cor do conjunto de cores para pintar o olho esquerdo
"""
cor_a3 = int(input("Digite o valor 2 para a cor da face: "))
if cor_a3 < 0 or cor_a3 > 255:
    print("\nValor para a cor 1 é invalido!! {}".format(cor_a3))
    cont = 0  # Contador do while
    while cor_a3 < 0 or cor_a3 > 255:
        cor_a3 = int(input("\nDigite novamente: "))
        if 0 < cor_a3 <= 255:
            print("\nValor correto! {}".format(cor_a3))
            break
    cont += 1
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Desenha o sorriso do desenho
x = 300
y = 280
widht = 120
height = 100
start_angle = 190
end_angle = 350
"""
Funcao que desenha a borda externa de um arco. Útil para desenhar linhas curvas, ela tambem recebe o valor da linha
do arco
"""
"""
Variavel que define a primeira cor do conjunto de cores para pintar o rosto do desenho
"""
cor_a1 = int(input("\nDigite o valor 1 para a cor da face: "))
if cor_a1 < 0 or cor_a1 > 255:
    print("\nValor para a cor 1 é invalido!! {}".format(cor_a1))
    cont = 0  # Contador do while
    while cor_a1 < 0 or cor_a1 > 255:
        cor_a1 = int(input("\nDigite novamente: "))
        if 0 < cor_a1 <= 255:
            print("\nValor correto! {}".format(cor_a1))
            break
    cont += 1

"""
Variavel que define a segunda cor do conjunto de cores para pintar o sorriso
"""
cor_a2 = int(input("Digite o valor 2 para a cor da face: "))
if cor_a2 < 0 or cor_a2 > 255:
    print("\nValor para a cor 1 é invalido!! {}".format(cor_a2))
    cont = 0  # Contador do while
    while cor_a2 < 0 or cor_a2 > 255:
        cor_a2 = int(input("\nDigite novamente: "))
        if 0 < cor_a2 <= 255:
            print("\nValor correto! {}".format(cor_a2))
            break
    cont += 1

"""
Variavel que define a terceira cor do conjunto de cores para pintar o sorriso do desenho
"""
cor_a3 = int(input("Digite o valor 2 para a cor da face: "))
if cor_a3 < 0 or cor_a3 > 255:
    print("\nValor para a cor 1 é invalido!! {}".format(cor_a3))
    cont = 0  # Contador do while
    while cor_a3 < 0 or cor_a3 > 255:
        cor_a3 = int(input("\nDigite novamente: "))
        if 0 < cor_a3 <= 255:
            print("\nValor correto! {}".format(cor_a3))
            break
    cont += 1
arcade.draw_arc_outline(x, y, widht, height, (cor_a1, cor_a2, cor_a3), start_angle, end_angle, 10)

arcade.finish_render()  # Função que finaliza o desenho e exibe o resultado

arcade.run()  # Função que mantem a janela aberta até que o botão 'fechar' seja pressionado
