#!/usr/local/bin/python
import pygame
import sys
from pygame.locals import *
import random
from src.cdp.Personagens import Personagem
from src.cih import Impressao
from src.cih import JanelaMenu
from src.util.Build import (NavePerdidaBuilder, NaveFugaBuilder, NaveGrupoBuilder, NavePeaoBuilder, NavePersegueBuilder)
from src.util.Build import NaveJogadorBuilder
# from src.cgd import Path

# -------------------------------------------------------------------------------
# Name:        Nave Maluca 1.1
# Author:      Gislaine e Izabely
# Created:     09/29/2015
# Copyright:   (c) Gislaine  e Izabely 2015
# Licence:     GIZ
# -------------------------------------------------------------------------------


__author__ = 'Gislaine  e Izabely'

pygame.init()
pygame.font.init()

WIDTH = 1000
HEIGTH = 600
LIM_WIDTH = WIDTH - 65
LIM_HEIGTH = HEIGTH - 50

WHITE = (255, 255, 255)
FPS = 60

def start_controle_som():

    pygame.mixer.pre_init(44100, 32, 2, 4096)

    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

    # return pygame.mixer.Sound("MusicNave.wav")

def colisao_de_naves(nave, inimigos):

    area = nave.get_area()

    for inimigo in inimigos:
        if area.colliderect(inimigo.get_area()):
            return True

    return False


def colisao_tiro(nave, inimigos):

    if inimigos:

        for inimigo in inimigos:

            area = inimigo.get_area()

            for tiro in nave.armamento():

                if area.colliderect(tiro.get_area()):

                    tiro.colisao = True
                    tiro.ativo = False
                    inimigo.foiAtingido()

                    return True

    return False


def cria_inimigo(naves_inimigas, num_inimigos):

    if len(naves_inimigas) < num_inimigos:
        nave_criada = cria_nave_inimigo()

        if naves_inimigas:
            for inimigo in naves_inimigas:
                if not nave_criada.get_area().colliderect(inimigo.get_area):
                    naves_inimigas.append(nave_criada)
        else:
            naves_inimigas.append(nave_criada)

    return naves_inimigas


def get_evento_saida():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()


def get_evento_teclado(nave):

    tecla = pygame.key.get_pressed()

    if tecla[K_UP] or tecla[K_w]:

        if nave.getPosicaoY() > 0:
            nave.setPosicaoY(nave.getPosicaoY() - 25)

        nave.start_area()

    elif tecla[K_DOWN] or tecla[K_s]:

        if nave.getPosicaoY() < LIM_HEIGTH:
            nave.setPosicaoY(nave.getPosicaoY() + 25)

        nave.start_area()

    elif tecla[K_LEFT] or tecla[K_a]:

        if nave.getPosicaoX() > 0:
            nave.setPosicaoX(nave.getPosicaoX() - 25)

        nave.start_area()

    elif tecla[K_RIGHT] or tecla[K_d]:

        if nave.getPosicaoX() < LIM_WIDTH:
            nave.setPosicaoX(nave.getPosicaoX() + 25)

        nave.start_area()

    elif tecla[K_SPACE]:

        nave.atira()


def run(menu):

        relogio = pygame.time.Clock()
        loop_principal = True

        while loop_principal:
            mouse_posicao = pygame.mouse.get_pos()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    loop_principal = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    menu.mouse_visivel = False
                    menu.set_selecao_teclado(event.key)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in menu.itens:
                        if item.mouse_selecionado(mouse_posicao[0], mouse_posicao[1]):
                            menu.funcoes[item.text]()

            if pygame.mouse.get_rel() != (0, 0):
                menu.mouse_visivel = True
                menu.item_atual = None

            menu.set_visibilidade_mouse()

            for item in menu.itens:
                if menu.mouse_visivel:
                    menu.set_selecao_mouse(item, mouse_posicao[0], mouse_posicao[1])
                menu.tela.blit(item.label, (item.pos_x, item.pos_y))

            pygame.display.flip()

            relogio.tick(FPS)


def menu_fim():

    saida = Impressao.Impressao()

    tela = saida.imprime_texto_fim()
    menu_itens = ("Novo Jogo", "Sair")

    funcoes = {"Novo Jogo": jogar, "Sair": sys.exit}

    tam_fonte = 30
    fonte_nome = pygame.font.get_default_font()

    menu = JanelaMenu.JanelaMenu(tela, menu_itens, funcoes, fonte_nome, tam_fonte, WHITE)
    run(menu)


def menu_instrucao():

    saida = Impressao.Impressao()

    tela = saida.imprime_instrucao()
    menu_itens = ("Voltar", "Iniciar")

    funcs = {"Voltar": menu_inicial, "Iniciar": jogar}

    tam_fonte = 30
    font_name = pygame.font.get_default_font()

    menu = JanelaMenu.JanelaMenu(tela, menu_itens, funcs, font_name, tam_fonte, WHITE)
    run(menu)


def menu_inicial():

    saida = Impressao.Impressao()
    tela = saida.start_tela_menu()

    menu_itens = ("Iniciar Jogo", "Instruções", "Sair")

    funcs = {"Iniciar Jogo": jogar, "Sair": sys.exit, "Instruções": menu_instrucao}

    tam_fonte = 30
    font_name = pygame.font.get_default_font()

    menu = JanelaMenu.JanelaMenu(tela, menu_itens, funcs, font_name, tam_fonte, WHITE)

    run(menu)


def move_tiro(nave):

    if nave.armamento():
        for tiro in nave.armamento():
            tiro.atira()


def remove_tiro(nave):
    if nave.armamento():
        for tiro in nave.armamento():
            if tiro.colisao or not tiro.ativo:
                nave.removeTiro(tiro)


def jogar():

    pygame.init()
    pygame.font.init()
    saida = Impressao.Impressao()
    nave = cria_nave()
    colisao = False
    num_inimigos = 10
    naves_inimigas = []
    relogio = pygame.time.Clock()

    while True:

        get_evento_saida()

        if not colisao:
            naves_inimigas = cria_inimigo(naves_inimigas, num_inimigos)
            get_evento_teclado(nave)
            carregar()
            colisao = colisao_de_naves(nave, naves_inimigas)
            move_nave_inimiga(naves_inimigas)
            move_tiro(nave)

            for m in nave.armamento():
                saida.telao.blit(m.figura(), (m.getPosicaoX(), m.getPosicaoY()))

            remove_naves_inimigas(naves_inimigas)
            remove_tiro(nave)

            for n in naves_inimigas:
                saida.telao.blit(n.figura(), (n.getPosicaoX(), n.getPosicaoY()))

            saida.telao.blit(nave.figura(), (nave.getPosicaoX(), nave.getPosicaoY()))
            explosao = colisao_tiro(nave, naves_inimigas)

            if explosao:
                remove_tiro(nave)
                remove_naves_inimigas(naves_inimigas)

        else:
            menu_fim()

        pygame.display.update()
        relogio.tick(FPS)


def toca_musica(som):
    som.set_volume(0.1)
    som.play()


def move_nave_inimiga(naves_inimigas):
    if naves_inimigas:
        for inimigo in naves_inimigas:
            inimigo.move()


def remove_naves_inimigas(naves_inimigas):
    if naves_inimigas:
        for inimigo in naves_inimigas:
            if inimigo.getPosicaoY() > HEIGTH or inimigo.atingido():
                naves_inimigas.remove(inimigo)


def carregar():

    Impressao.Impressao()


def cria_nave():
    # nome = "Bulhufinha"
    # imagemID = Path.getPath() + 'Imagem/TieFighter_archigraphs.png'
    # imagemNave = Path.getPath() + 'Imagem/TieFighter_archigraphs.png'
    naveEscolhida = NaveJogadorBuilder.NaveJogadorBuilder()

    n = Personagem.Personagem.criandoNave(naveEscolhida)
    n.setPosicaoX(LIM_WIDTH / 2)
    n.setPosicaoY(LIM_HEIGTH)
    n.start_area()

    return n


def cria_nave_inimigo():

    aleatorio = random.randint(0, 20)

    if 0 <= aleatorio <= 3:
        naveEscolhida = NavePersegueBuilder.NavePersegueBuilder()
    elif 4 <= aleatorio <= 8:
        naveEscolhida = NavePeaoBuilder.NavePeaoBuilder()
    elif 9 <= aleatorio <= 11:
        naveEscolhida = NavePerdidaBuilder.NavePerdidaBuilder()
    elif 10 <= aleatorio <= 17:
        naveEscolhida = NaveGrupoBuilder.NaveGrupoBuilder()
    else:
        naveEscolhida = NaveFugaBuilder.NaveFugaBuilder()

    n = Personagem.Personagem.criandoNave(naveEscolhida)
    n.setPosicaoX(random.randrange(LIM_WIDTH - 20))
    n.setPosicaoY(0)
    n.start_area()

    return n
