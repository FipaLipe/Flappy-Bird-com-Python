# Bibliotecas
import pygame as pg
import os
import random

# Constantes
width = 500
height = 800

pipeImg = pg.transfor.scale_2x(pg.image.load(os.path.join('imgs', 'pipe.png')))
baseImg = pg.transfor.scale_2x(pg.image.load(os.path.join('imgs', 'base.png')))
bgImg = pg.transfor.scale_2x(pg.image.load(os.path.join('imgs', 'bg.png')))
birdImgs = [pg.transfor.scale_2x(pg.image.load(os.path.join('bird1', 'base.png'))),
            pg.transfor.scale_2x(pg.image.load(
                os.path.join('bird2', 'base.png'))),
            pg.transfor.scale_2x(pg.image.load(os.path.join('bird3', 'base.png'))), ]

pg.font.init()
pointsFont = pg.font.SysFont('arial', 50)
