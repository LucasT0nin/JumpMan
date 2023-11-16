#Lucas Tonin Leite
#Tia: 32089759


import pygame
from pygame.locals import *
import random

class MeuObjeto(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((random.randint(50, 70), 20))
        self.image.fill((0, random.randint(0, 255), random.randint(0, 255)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Tuba(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_right = pygame.transform.scale(pygame.image.load('./sprites/tubarao_02.png'), (192, 96))
        self.image_left = pygame.transform.scale(pygame.image.load('./sprites/tubarao_01.png'), (192, 96))
        self.image_right1 = pygame.transform.scale(pygame.image.load('./sprites/tubarao_04.png'), (98,194))
        self.image_left1 = pygame.transform.scale(pygame.image.load('./sprites/tubarao_03.png'), (98,194))
        self.image = self.image_right  # Inicia com a imagem para a direita
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = random.choice([-3, 3])
        self.speed_y = random.choice([-3, 3])
        self.last_speed_y = self.speed_y
        self.last_speed_x = self.speed_x

    def update(self):
        self.rect.y += self.speed_y
        if self.speed_y > 0:
            self.image = self.image_right1
        elif self.speed_y < 0:
            self.image = self.image_left1
        if self.speed_y != self.last_speed_y:
            self.last_speed_y = self.speed_y
        if self.rect.top > 525 or self.rect.bottom < 2:
            self.speed_y *= -1


    def update_horizontal(self):
        self.rect.x += self.speed_x
        if self.speed_x > 0:
            self.image = self.image_right
        elif self.speed_x < 0:
            self.image = self.image_left
        if self.speed_x != self.last_speed_x:
            self.last_speed_x = self.speed_x 
        if self.rect.right > pygame.display.get_surface().get_width() or self.rect.left < 0:
            self.speed_x *= -1


class Gaivota(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_right = pygame.transform.scale(pygame.image.load('./sprites/gaivota_01.png'), (100,60))
        self.image_left = pygame.transform.scale(pygame.image.load('./sprites/gaivota_02.png'), (100,60))
        self.image_right1 = pygame.transform.scale(pygame.image.load('./sprites/gaivota_01.png'), (100,60))
        self.image_left1 = pygame.transform.scale(pygame.image.load('./sprites/gaivota_04.png'), (100,60))
        self.image = self.image_right  # Inicia com a imagem para a direita
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = random.choice([-3, 3])
        self.speed_y = random.choice([-3, 3])
        self.last_speed_y = self.speed_y
        self.last_speed_x = self.speed_x

    def update(self):
        self.rect.x += self.speed_x
        if self.speed_x > 0:
            self.image = self.image_right
        elif self.speed_x < 0:
            self.image = self.image_left
        if self.speed_x != self.last_speed_x:
            self.last_speed_x = self.speed_x 
        if self.rect.right > pygame.display.get_surface().get_width() or self.rect.left < 0:
            self.speed_x *= -1

def exibir_menu(janela):
    fundo_menu = pygame.image.load("./sprites/P600.png").convert()
    fonte = pygame.font.Font(None, 36)
    cor_p = (0, 0, 0)
    estado = True
    executando_menu = True
    jogador_imagem = pygame.image.load('./sprites/menino_02.png')
    jogador_imagem = pygame.transform.scale(jogador_imagem, (50, 80))
    jogadora_imagem = pygame.image.load('./sprites/menina_02.png')
    jogadora_imagem = pygame.transform.scale(jogadora_imagem, (50, 80))
    while executando_menu:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    fase1(janela, estado)
                    return True
            if event.type == KEYDOWN:
                if event.key == pygame.K_t:
                    if estado == False:
                        estado = True
                    else:
                        estado = False
        


        janela.blit(fundo_menu, (0, 0))
        texto = fonte.render("Pressione ESPAÇO para iniciar", True, cor_p)
        texto1 = fonte.render("Pressione T para alterar o personagem", True, cor_p)
        janela.blit(texto, (120, 90))
        janela.blit(texto1, (90, 170))
        if estado == True:
            janela.blit(jogador_imagem, (300, 459))
        else:
            janela.blit(jogadora_imagem, (300, 459)) 
            
        pygame.display.update()

def fase1(janela, estado):
    fundo = pygame.image.load("./sprites/P600.png")
    pygame.mixer.init()
    jogador_imagem = pygame.image.load('./sprites/menino_02.png')
    jogador_imagem = pygame.transform.scale(jogador_imagem, (50, 80))
    corac = pygame.image.load('./sprites/coracao.png')
    cc = pygame.image.load('./sprites/cc.png')
    coracao = pygame.transform.scale(corac, (60, 40))
    cca = pygame.transform.scale(cc, (60, 40))
    modo_ataque = False
    #sons
    som = pygame.mixer.Sound('./sons/mordi.wav') 
    pulo = pygame.mixer.Sound('./sons/pulo.wav') 
    shark = pygame.mixer.Sound('./sons/shark.wav') 
    pulo.set_volume(0.1)
    #imagens
    img_parado = pygame.image.load('./sprites/menino_02.png')
    parado = pygame.transform.scale(img_parado, (50, 80))
    jogador_esquerda = pygame.image.load('./sprites/menino_01.png')
    esquerda = pygame.transform.scale(jogador_esquerda, (50, 80))
    jogador_esquerda_pulo = pygame.image.load('./sprites/menino_04.png')
    esquerda_pulo = pygame.transform.scale(jogador_esquerda_pulo, (50, 80))
    jogador_direita = pygame.image.load('./sprites/menino_03.png')
    direita = pygame.transform.scale(jogador_direita, (50, 80))
    jogador_direita_pulo = pygame.image.load('./sprites/menino_05.png')
    direita_pulo = pygame.transform.scale(jogador_direita_pulo, (50, 80))
    ps = pygame.image.load("./sprites/P_S600.png")
    p = pygame.image.load("./sprites/P600.png")
    psp = pygame.image.load("./sprites/P_SP600.png")
    pygame.init()
    largura, altura = 600, 600
    janela = pygame.display.set_mode((largura, altura))
    atual = 0
    gravidade = 5
    primeiro_tuba = True
    vida = 3
    jump_count = 11
    velocidade_horizontal = 4
    pulando = False
    inicio = True
    tempo_dano = pygame.time.get_ticks()
    grupo_sprites = pygame.sprite.Group()  
    retangulos = []  
    tubas = pygame.sprite.Group()
    tempo_criacao_retangulo = pygame.time.get_ticks() 
    intervalo_criacao_retangulo = 700 
    jogador_x = 250
    jogador_y = 0
    score = 0
    start_time = pygame.time.get_ticks() 

    jogadora_esquerda = pygame.image.load('./sprites/menina_01.png')
    esquerdaa = pygame.transform.scale(jogadora_esquerda, (50, 80))
    jogadora_direita = pygame.image.load('./sprites/menina_03.png')
    diretaa = pygame.transform.scale(jogadora_direita, (50, 80))
    jogadora_frente = pygame.image.load('./sprites/menina_02.png')
    frentee = pygame.transform.scale(jogadora_frente, (50, 80))


    executar = True
    while executar:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if not any(keys) and estado == True:
            jogador_imagem = parado
        else:
            jogador_imagem = frentee
        if jogador_y > 520:
            jogador_y = 520
        if jogador_y < 0:
            jogador_y = 0
        if keys[K_LEFT] and jogador_x > 0:
            if estado == True:
                jogador_x -= velocidade_horizontal
                jogador_imagem = esquerda
                if pulando:
                    jogador_imagem = esquerda_pulo
                    if pygame.mixer.get_busy() == False:
                        pulo.play()
            else:
                jogador_x -= velocidade_horizontal
                jogador_imagem = esquerdaa
                if pulando:
                    jogador_imagem = esquerdaa
                    if pygame.mixer.get_busy() == False:
                        pulo.play()

            
        if keys[K_RIGHT] and jogador_x < 550:
            if estado == True:
                jogador_x += velocidade_horizontal
                jogador_imagem = direita
                if pulando:
                    jogador_imagem = direita_pulo
                    if pygame.mixer.get_busy() == False:
                        pulo.play()
            else:
                jogador_x += velocidade_horizontal
                jogador_imagem = diretaa
                if pulando:
                    jogador_imagem = diretaa
                    if pygame.mixer.get_busy() == False:
                        pulo.play()
        if keys[K_UP]:
            pulando = True
        if pulando:
            if jump_count >= -11:
                neg = 1
                if jump_count < 0:
                    neg = -1
                jogador_y -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
            else:
                pulando = False
                jump_count = 11

        jogador_y += gravidade + 5

        if primeiro_tuba == True:
            nova_tuba = Tuba(5, 500)
            grupo_sprites.add(nova_tuba)
            tubas.add(nova_tuba)
            primeiro_tuba = False

        if inicio:
            novo_retangulo = MeuObjeto(225, 25)
            grupo_sprites.add(novo_retangulo)
            retangulos.append(novo_retangulo)
        inicio = False

        # Verifique a colisão o tubarão
        for tuba in tubas:
            if tuba.rect.colliderect(pygame.Rect(jogador_x + 10, jogador_y + 30, 35, 44)) and modo_ataque == False:
                vida -= 1
                fundo = ps
                if vida != 0:
                    jogador_y = 100
                    tempo_dano = pygame.time.get_ticks()
                    som.play()
            if tuba.rect.colliderect(pygame.Rect(jogador_x + 10, jogador_y + 30, 30, 35)) and modo_ataque == True:
                vida -= 1
                fundo = ps
                modo_ataque = False
                for tuba in tubas:
                    tuba.rect.y = 520
                if vida != 0:
                    jogador_y = 100
                    tempo_dano = pygame.time.get_ticks()
                    som.play()


        # Verifique a colisão com cada retângulo na lista
        for retangulo in retangulos:
            if retangulo.rect.colliderect(pygame.Rect(jogador_x + 10, jogador_y + 30, 40, 49)):
                jogador_y = retangulo.rect.y - 76

        tempo_atual_dano = pygame.time.get_ticks()
        tempo = pygame.time.get_ticks()

        if jogador_y > 520:
            fundo = ps
            vida -= 1
            tempo_dano = pygame.time.get_ticks()
            if vida != 0:
                jogador_y = 100
                tempo_dano = pygame.time.get_ticks()
                # fundo = psp
                # pygame.time.delay(2000)

        if tempo_atual_dano - tempo_dano >= 2500:
            fundo = p

        if tempo - tempo_atual_dano >= 500:
            jogador_y = 100
            # pygame.time.delay(2000)

        # Verifique se é hora de criar um novo retângulo
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - tempo_criacao_retangulo >= intervalo_criacao_retangulo:
            if atual == 0:
                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(5, 75), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)

                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(155, 225), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)

                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(305, 375), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)

                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(455, 525), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)



                tempo_criacao_retangulo = tempo_atual
                atual = 1
            elif atual == 1:
                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(5, 125), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)

                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(205, 325), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)

                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(405, 525), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)


                tempo_criacao_retangulo = tempo_atual
                atual = 0

        for retangulo in retangulos:
            tempo_atual = pygame.time.get_ticks()  # Tempo atual
            retangulo.rect.y += 5

            # Remova os retângulos que atingiram a parte inferior da tela
            if retangulo.rect.y > altura:
                retangulos.remove(retangulo)

        retangulos = [retangulo for retangulo in retangulos if retangulo.rect.y < 600]

        # if tempo_inicial - 2000 > 0:
        #     fase2(janela)
        current_time = pygame.time.get_ticks()
        WHITE = (255, 255, 255)
        elapsed_time = (current_time - start_time) // 1000 
        score = elapsed_time 
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        if score > 20:
            fase2(janela,vida,score,estado1)
        
        if random.randint(0, 1000) < 2 and modo_ataque == False:
            Tempo_ataque = tempo_atual
            modo_ataque = True
            shark.play()
            

        if modo_ataque == False:
            for tuba in tubas:
                tuba.update_horizontal()
        if modo_ataque == True:
            for tuba in tubas:
                tubas.update()
            print(tuba.rect.y)
            if tempo_atual - Tempo_ataque >= 5000 and tuba.rect.y > 500:
                modo_ataque = False

        janela.fill((255, 255, 255))
        janela.blit(fundo, (0, 0))

        if vida == 3:
            janela.blit(coracao, (0, 0))
            janela.blit(coracao, (40, 0))
            janela.blit(coracao, (80, 0))
        elif vida == 2:
            janela.blit(coracao, (0, 0))
            janela.blit(coracao, (40, 0))
            janela.blit(cca, (80, 0))
        elif vida == 1:
            janela.blit(coracao, (0, 0))
            janela.blit(cca, (40, 0))
            janela.blit(cca, (80, 0))
        else:
            exibir_menu(janela)

        largura += 1
        estado1 = estado
        janela.blit(score_text, (495, 0))
        janela.blit(jogador_imagem, (jogador_x, jogador_y))
        grupo_sprites.draw(janela)
        clock = pygame.time.Clock()
        pygame.display.update()
        clock.tick(120)

def fase2(janela,vida_antio, score_max,estado):
    estado = estado
    fundo = pygame.image.load("./sprites/P600.png")
    pygame.mixer.init()
    jogador_imagem = pygame.image.load('./sprites/menino_02.png')
    jogador_imagem = pygame.transform.scale(jogador_imagem, (50, 80))
    corac = pygame.image.load('./sprites/coracao.png')
    cc = pygame.image.load('./sprites/cc.png')
    coracao = pygame.transform.scale(corac, (60, 40))
    cca = pygame.transform.scale(cc, (60, 40))
    modo_ataque = False
    #sons
    som = pygame.mixer.Sound('./sons/mordi.wav') 
    pulo = pygame.mixer.Sound('./sons/pulo.wav') 
    shark = pygame.mixer.Sound('./sons/shark.wav') 
    pulo.set_volume(0.1)
    #imagens
    img_parado = pygame.image.load('./sprites/menino_02.png')
    parado = pygame.transform.scale(img_parado, (50, 80))
    jogador_esquerda = pygame.image.load('./sprites/menino_01.png')
    esquerda = pygame.transform.scale(jogador_esquerda, (50, 80))
    jogador_esquerda_pulo = pygame.image.load('./sprites/menino_04.png')
    esquerda_pulo = pygame.transform.scale(jogador_esquerda_pulo, (50, 80))
    jogador_direita = pygame.image.load('./sprites/menino_03.png')
    direita = pygame.transform.scale(jogador_direita, (50, 80))
    jogador_direita_pulo = pygame.image.load('./sprites/menino_05.png')
    direita_pulo = pygame.transform.scale(jogador_direita_pulo, (50, 80))
    ps = pygame.image.load("./sprites/P_S600.png")
    p = pygame.image.load("./sprites/P600.png")
    psp = pygame.image.load("./sprites/P_SP600.png")
    pygame.init()
    largura, altura = 600, 600
    janela = pygame.display.set_mode((largura, altura))
    atual = 0
    gravidade = 5
    primeiro_tuba = True
    vida = vida_antio
    jump_count = 11
    velocidade_horizontal = 4
    pulando = False
    inicio = True
    tempo_dano = pygame.time.get_ticks()
    grupo_sprites = pygame.sprite.Group()  
    retangulos = []  
    tubas = pygame.sprite.Group()
    gaivotas = pygame.sprite.Group()
    tempo_criacao_retangulo = pygame.time.get_ticks() 
    intervalo_criacao_retangulo = 700 
    jogador_x = 250
    jogador_y = 0
    score = 0
    start_time = pygame.time.get_ticks() 
    primeiro_gaivota = True
    jogadora_esquerda = pygame.image.load('./sprites/menina_01.png')
    esquerdaa = pygame.transform.scale(jogadora_esquerda, (50, 80))
    jogadora_direita = pygame.image.load('./sprites/menina_03.png')
    diretaa = pygame.transform.scale(jogadora_direita, (50, 80))
    jogadora_frente = pygame.image.load('./sprites/menina_02.png')
    frentee = pygame.transform.scale(jogadora_frente, (50, 80))


    executar = True
    while executar:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if not any(keys) and estado == True:
            jogador_imagem = parado
        else:
            jogador_imagem = frentee
        if jogador_y > 520:
            jogador_y = 520
        if jogador_y < 0:
            jogador_y = 0
        if keys[K_LEFT] and jogador_x > 0:
            if estado == True:
                jogador_x -= velocidade_horizontal
                jogador_imagem = esquerda
                if pulando:
                    jogador_imagem = esquerda_pulo
                    if pygame.mixer.get_busy() == False:
                        pulo.play()
            else:
                jogador_x -= velocidade_horizontal
                jogador_imagem = esquerdaa
                if pulando:
                    jogador_imagem = esquerdaa
                    if pygame.mixer.get_busy() == False:
                        pulo.play()

            
        if keys[K_RIGHT] and jogador_x < 550:
            if estado == True:
                jogador_x += velocidade_horizontal
                jogador_imagem = direita
                if pulando:
                    jogador_imagem = direita_pulo
                    if pygame.mixer.get_busy() == False:
                        pulo.play()
            else:
                jogador_x += velocidade_horizontal
                jogador_imagem = diretaa
                if pulando:
                    jogador_imagem = diretaa
                    if pygame.mixer.get_busy() == False:
                        pulo.play()
        if keys[K_UP]:
            pulando = True
        if pulando:
            if jump_count >= -11:
                neg = 1
                if jump_count < 0:
                    neg = -1
                jogador_y -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
            else:
                pulando = False
                jump_count = 11

        jogador_y += gravidade + 5

        if primeiro_tuba == True:
            nova_tuba = Tuba(5, 500)
            grupo_sprites.add(nova_tuba)
            tubas.add(nova_tuba)
            primeiro_tuba = False

        if primeiro_gaivota == True:
            nova_gaivota = Gaivota(400, 10)  # Suponha que você tenha uma classe Gaivota para criar novas gaivotas
            grupo_sprites.add(nova_gaivota)  # Adicionando a nova gaivota ao grupo de sprites
            gaivotas.add(nova_gaivota)  # Adicionando a nova gaivota ao grupo específico de gaivotas
            primeiro_gaivota = False

        if inicio:
            novo_retangulo = MeuObjeto(225, 25)
            grupo_sprites.add(novo_retangulo)
            retangulos.append(novo_retangulo)
        inicio = False

    #         tubas = pygame.sprite.Group()
    # gaivoto = pygame.sprite.Group()

        # Verifique a colisão o tubarão
        for tuba in tubas:
            if tuba.rect.colliderect(pygame.Rect(jogador_x + 10, jogador_y + 30, 35, 44)) and modo_ataque == False:
                vida -= 1
                fundo = ps
                if vida != 0:
                    jogador_y = 100
                    tempo_dano = pygame.time.get_ticks()
                    som.play()
            if tuba.rect.colliderect(pygame.Rect(jogador_x + 10, jogador_y + 30, 30, 35)) and modo_ataque == True:
                vida -= 1
                fundo = ps
                modo_ataque = False
                for tuba in tubas:
                    tuba.rect.y = 520
                if vida != 0:
                    jogador_y = 100
                    tempo_dano = pygame.time.get_ticks()
                    som.play()


        for gaivota in gaivotas:
            if gaivota.rect.colliderect(pygame.Rect(jogador_x + 10, jogador_y + 30, 35, 44)) and modo_ataque == False:
                vida -= 1
                fundo = ps
                if vida != 0:
                    jogador_y = 100
                    tempo_dano = pygame.time.get_ticks()
                    som.play()
            

        # Verifique a colisão com cada retângulo na lista
        for retangulo in retangulos:
            if retangulo.rect.colliderect(pygame.Rect(jogador_x + 10, jogador_y + 30, 40, 49)):
                jogador_y = retangulo.rect.y - 76

        tempo_atual_dano = pygame.time.get_ticks()
        tempo = pygame.time.get_ticks()

        if jogador_y > 520:
            fundo = ps
            vida -= 1
            tempo_dano = pygame.time.get_ticks()
            if vida != 0:
                jogador_y = 100
                tempo_dano = pygame.time.get_ticks()
                # fundo = psp
                # pygame.time.delay(2000)

        if tempo_atual_dano - tempo_dano >= 2500:
            fundo = p

        if tempo - tempo_atual_dano >= 500:
            jogador_y = 100
            # pygame.time.delay(2000)

        # Verifique se é hora de criar um novo retângulo
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - tempo_criacao_retangulo >= intervalo_criacao_retangulo:
            if atual == 0:
                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(5, 75), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)

                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(155, 225), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)

                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(305, 375), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)

                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(455, 525), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)



                tempo_criacao_retangulo = tempo_atual
                atual = 1
            elif atual == 1:
                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(5, 125), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)

                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(205, 325), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)

                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(405, 525), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)


                tempo_criacao_retangulo = tempo_atual
                atual = 0

        for retangulo in retangulos:
            tempo_atual = pygame.time.get_ticks()  # Tempo atual
            retangulo.rect.y += 5

            # Remova os retângulos que atingiram a parte inferior da tela
            if retangulo.rect.y > altura:
                retangulos.remove(retangulo)

        retangulos = [retangulo for retangulo in retangulos if retangulo.rect.y < 600]

        # if tempo_inicial - 2000 > 0:
        #     fase2(janela)
        current_time = pygame.time.get_ticks()
        WHITE = (255, 255, 255)
        elapsed_time = (current_time - start_time) // 1000 
        score = elapsed_time + score_max
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        if score > 40:
            fase3(janela,vida,score,estado)
        
        if random.randint(0, 1000) < 2 and modo_ataque == False:
            Tempo_ataque = tempo_atual
            modo_ataque = True
            shark.play()
            

        if modo_ataque == False:
            for tuba in tubas:
                tuba.update_horizontal()
        if modo_ataque == True:
            for tuba in tubas:
                tubas.update()
            print(tuba.rect.y)
            if tempo_atual - Tempo_ataque >= 5000 and tuba.rect.y > 500:
                modo_ataque = False

        gaivotas.update()
        janela.fill((255, 255, 255))
        janela.blit(fundo, (0, 0))

        if vida == 3:
            janela.blit(coracao, (0, 0))
            janela.blit(coracao, (40, 0))
            janela.blit(coracao, (80, 0))
        elif vida == 2:
            janela.blit(coracao, (0, 0))
            janela.blit(coracao, (40, 0))
            janela.blit(cca, (80, 0))
        elif vida == 1:
            janela.blit(coracao, (0, 0))
            janela.blit(cca, (40, 0))
            janela.blit(cca, (80, 0))
        else:
            exibir_menu(janela)

        largura += 1
        janela.blit(score_text, (495, 0))
        janela.blit(jogador_imagem, (jogador_x, jogador_y))
        grupo_sprites.draw(janela)
        clock = pygame.time.Clock()
        pygame.display.update()
        clock.tick(120)

def fase3(janela, vida_antio, score_max, estado):
    estado = estado
    fundo = pygame.image.load("./sprites/P600.png")
    pygame.mixer.init()
    jogador_imagem = pygame.image.load('./sprites/menino_02.png')
    jogador_imagem = pygame.transform.scale(jogador_imagem, (50, 80))
    corac = pygame.image.load('./sprites/coracao.png')
    cc = pygame.image.load('./sprites/cc.png')
    coracao = pygame.transform.scale(corac, (60, 40))
    cca = pygame.transform.scale(cc, (60, 40))
    modo_ataque = False
    #sons
    som = pygame.mixer.Sound('./sons/mordi.wav') 
    pulo = pygame.mixer.Sound('./sons/pulo.wav') 
    shark = pygame.mixer.Sound('./sons/shark.wav') 
    pulo.set_volume(0.1)
    #imagens
    img_parado = pygame.image.load('./sprites/menino_02.png')
    parado = pygame.transform.scale(img_parado, (50, 80))
    jogador_esquerda = pygame.image.load('./sprites/menino_01.png')
    esquerda = pygame.transform.scale(jogador_esquerda, (50, 80))
    jogador_esquerda_pulo = pygame.image.load('./sprites/menino_04.png')
    esquerda_pulo = pygame.transform.scale(jogador_esquerda_pulo, (50, 80))
    jogador_direita = pygame.image.load('./sprites/menino_03.png')
    direita = pygame.transform.scale(jogador_direita, (50, 80))
    jogador_direita_pulo = pygame.image.load('./sprites/menino_05.png')
    direita_pulo = pygame.transform.scale(jogador_direita_pulo, (50, 80))
    ps = pygame.image.load("./sprites/P_S600.png")
    p = pygame.image.load("./sprites/P600.png")
    psp = pygame.image.load("./sprites/P_SP600.png")
    pygame.init()
    largura, altura = 600, 600
    janela = pygame.display.set_mode((largura, altura))
    atual = 0
    gravidade = 5
    primeiro_tuba = True
    vida = vida_antio
    jump_count = 11
    velocidade_horizontal = 4
    pulando = False
    inicio = True
    tempo_dano = pygame.time.get_ticks()
    grupo_sprites = pygame.sprite.Group()  
    retangulos = []  
    tubas = pygame.sprite.Group()
    gaivotas = pygame.sprite.Group()
    tempo_criacao_retangulo = pygame.time.get_ticks() 
    intervalo_criacao_retangulo = 700 
    jogador_x = 250
    jogador_y = 0
    score = 0
    start_time = pygame.time.get_ticks() 
    primeiro_gaivota = True
    jogadora_esquerda = pygame.image.load('./sprites/menina_01.png')
    esquerdaa = pygame.transform.scale(jogadora_esquerda, (50, 80))
    jogadora_direita = pygame.image.load('./sprites/menina_03.png')
    diretaa = pygame.transform.scale(jogadora_direita, (50, 80))
    jogadora_frente = pygame.image.load('./sprites/menina_02.png')
    frentee = pygame.transform.scale(jogadora_frente, (50, 80))


    executar = True
    while executar:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if not any(keys) and estado == True:
            jogador_imagem = parado
        else:
            jogador_imagem = frentee
        if jogador_y > 520:
            jogador_y = 520
        if jogador_y < 0:
            jogador_y = 0
        if keys[K_LEFT] and jogador_x > 0:
            if estado == True:
                jogador_x -= velocidade_horizontal
                jogador_imagem = esquerda
                if pulando:
                    jogador_imagem = esquerda_pulo
                    if pygame.mixer.get_busy() == False:
                        pulo.play()
            else:
                jogador_x -= velocidade_horizontal
                jogador_imagem = esquerdaa
                if pulando:
                    jogador_imagem = esquerdaa
                    if pygame.mixer.get_busy() == False:
                        pulo.play()

            
        if keys[K_RIGHT] and jogador_x < 550:
            if estado == True:
                jogador_x += velocidade_horizontal
                jogador_imagem = direita
                if pulando:
                    jogador_imagem = direita_pulo
                    if pygame.mixer.get_busy() == False:
                        pulo.play()
            else:
                jogador_x += velocidade_horizontal
                jogador_imagem = diretaa
                if pulando:
                    jogador_imagem = diretaa
                    if pygame.mixer.get_busy() == False:
                        pulo.play()
        if keys[K_UP]:
            pulando = True
        if pulando:
            if jump_count >= -11:
                neg = 1
                if jump_count < 0:
                    neg = -1
                jogador_y -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
            else:
                pulando = False
                jump_count = 11

        jogador_y += gravidade + 5

        if primeiro_tuba == True:
            nova_tuba = Tuba(5, 500)
            grupo_sprites.add(nova_tuba)
            tubas.add(nova_tuba)
            primeiro_tuba = False

        if primeiro_gaivota == True:
            nova_gaivota = Gaivota(400, 10)  # Suponha que você tenha uma classe Gaivota para criar novas gaivotas
            grupo_sprites.add(nova_gaivota)  # Adicionando a nova gaivota ao grupo de sprites
            gaivotas.add(nova_gaivota)  # Adicionando a nova gaivota ao grupo específico de gaivotas
            primeiro_gaivota = False

        if inicio:
            novo_retangulo = MeuObjeto(225, 25)
            grupo_sprites.add(novo_retangulo)
            retangulos.append(novo_retangulo)
        inicio = False

        # Verifique a colisão o tubarão
        for tuba in tubas:
            if tuba.rect.colliderect(pygame.Rect(jogador_x + 10, jogador_y + 30, 35, 44)) and modo_ataque == False:
                vida -= 1
                fundo = ps
                if vida != 0:
                    jogador_y = 100
                    tempo_dano = pygame.time.get_ticks()
                    som.play()
            if tuba.rect.colliderect(pygame.Rect(jogador_x + 10, jogador_y + 30, 30, 35)) and modo_ataque == True:
                vida -= 1
                fundo = ps
                modo_ataque = False
                for tuba in tubas:
                    tuba.rect.y = 520
                if vida != 0:
                    jogador_y = 100
                    tempo_dano = pygame.time.get_ticks()
                    som.play()


        for gaivota in gaivotas:
            if gaivota.rect.colliderect(pygame.Rect(jogador_x + 10, jogador_y + 30, 35, 44)) and modo_ataque == False:
                vida -= 1
                fundo = ps
                if vida != 0:
                    jogador_y = 100
                    tempo_dano = pygame.time.get_ticks()
                    som.play()
            

        # Verifique a colisão com cada retângulo na lista
        for retangulo in retangulos:
            if retangulo.rect.colliderect(pygame.Rect(jogador_x + 10, jogador_y + 30, 40, 49)):
                jogador_y = retangulo.rect.y - 76

        tempo_atual_dano = pygame.time.get_ticks()
        tempo = pygame.time.get_ticks()

        if jogador_y > 520:
            fundo = ps
            vida -= 1
            tempo_dano = pygame.time.get_ticks()
            if vida != 0:
                jogador_y = 100
                tempo_dano = pygame.time.get_ticks()


        if tempo_atual_dano - tempo_dano >= 2500:
            fundo = p

        if tempo - tempo_atual_dano >= 500:
            jogador_y = 100

        # Verifique se é hora de criar um novo retângulo
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - tempo_criacao_retangulo >= intervalo_criacao_retangulo:
            if atual == 0:
                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(5, 175), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)

                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(155, 325), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)

                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(405, 525), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)

                tempo_criacao_retangulo = tempo_atual
                atual = 1
            elif atual == 1:
                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(5, 225), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)

                if random.randint(0, 100) < 90:
                    novo_retangulo = MeuObjeto(random.randint(305, 525), 0)
                    grupo_sprites.add(novo_retangulo)
                    retangulos.append(novo_retangulo)



                tempo_criacao_retangulo = tempo_atual
                atual = 0

        for retangulo in retangulos:
            tempo_atual = pygame.time.get_ticks()  # Tempo atual
            retangulo.rect.y += 5

            # Remova os retângulos que atingiram a parte inferior da tela
            if retangulo.rect.y > altura:
                retangulos.remove(retangulo)

        retangulos = [retangulo for retangulo in retangulos if retangulo.rect.y < 600]

        current_time = pygame.time.get_ticks()
        WHITE = (255, 255, 255)
        elapsed_time = (current_time - start_time) // 1000 
        score = elapsed_time + score_max
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        if random.randint(0, 1000) < 2 and modo_ataque == False:
            Tempo_ataque = tempo_atual
            modo_ataque = True
            shark.play()
            

        if modo_ataque == False:
            for tuba in tubas:
                tuba.update_horizontal()
        if modo_ataque == True:
            for tuba in tubas:
                tubas.update()
            print(tuba.rect.y)
            if tempo_atual - Tempo_ataque >= 5000 and tuba.rect.y > 500:
                modo_ataque = False

        gaivotas.update()
        janela.fill((255, 255, 255))
        janela.blit(fundo, (0, 0))

        if vida == 3:
            janela.blit(coracao, (0, 0))
            janela.blit(coracao, (40, 0))
            janela.blit(coracao, (80, 0))
        elif vida == 2:
            janela.blit(coracao, (0, 0))
            janela.blit(coracao, (40, 0))
            janela.blit(cca, (80, 0))
        elif vida == 1:
            janela.blit(coracao, (0, 0))
            janela.blit(cca, (40, 0))
            janela.blit(cca, (80, 0))
        else:
            exibir_menu(janela)

        largura += 1
        janela.blit(score_text, (495, 0))
        janela.blit(jogador_imagem, (jogador_x, jogador_y))
        grupo_sprites.draw(janela)
        clock = pygame.time.Clock()
        pygame.display.update()
        clock.tick(120)

def main():
    largura, altura = 600, 600
    janela = pygame.display.set_mode((largura, altura))

    pygame.init()
    pygame.mixer.init()

    executando = True
    no_menu = True

    while executando:
        if no_menu:
            no_menu = exibir_menu(janela)
        else:
            no_menu = iniciar_jogo(janela)

if __name__ == "__main__":
    main()

    pygame.quit()
