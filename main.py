from pygame import *
import sys

init()

window = display.set_mode((1280,720))




raio_x = 140
timer = 0
nuvem_x=800
nuvem_y=100
velocidade_nuvem=3
running = True
velocidade_nuvem2=-4
clock=time.Clock()


Kratos = image.load("Kratos.png")
Kratos = transform.scale(Kratos, (150,160))

kratostexto = font.Font("GODOFWAR.ttf", 40)

mixer.music.load("Homens queimem a vila.mp3")
mixer.music.play(-1)



background_color = (150,150,150)
while running:
    clock.tick(60)
    key_pressed = key.get_pressed()

    for ev in event.get():
        if ev.type == QUIT:
            quit()
            running = False
            sys.exit()
        if ev.type == KEYDOWN:
            key_pressed = ev.key
            if key_pressed == K_SPACE:
                background_color = (245,178,64)
    


    dt = clock.get_time()/1000
    keys = key.get_pressed()


    if keys[K_d]:
        raio_x = raio_x + 100 *dt

    if keys[K_a]:
        raio_x = raio_x - 100 *dt


    window.fill(background_color)

    draw.rect(window, (72, 157, 37), (0,600,1280,220))
    draw.rect(window, (15, 15, 15), (350, 360,200,240))
    draw.circle(window, (245, 231, 37), (raio_x,130), 60)
    draw.polygon(window, (246, 41, 0), ((350,360),(550,360),(450,200)))
    draw.rect(window, (99, 13, 83), (370, 460,50,70))
    draw.rect(window, (121, 77, 27), (450, 430,75,170))
    draw.circle(window, (0,0,0), (470,520), 7)
    draw.line(window, (255, 242, 81), (raio_x - 60,130), (raio_x - 120,130), 10)
    draw.line(window, (255, 242, 81), (raio_x +60 ,130), (raio_x + 120,130), 10)
    draw.line(window, (255, 242, 81), (raio_x,190), (raio_x,250), 10)
    draw.line(window, (255, 242, 81), (raio_x,70), (raio_x,10), 10)
    draw.rect(window, (101, 67, 33), (1000, 240, 80, 400))
    draw.circle(window, (0, 128, 0), (1040,300), 100)

    nuvem_x += velocidade_nuvem

    if nuvem_x > 1350:
        nuvem_x = -350


    draw.circle(window, (255,255,255), (nuvem_x,nuvem_y),(70))
    draw.circle(window, (255,255,255), (nuvem_x+100,nuvem_y),(70))
    draw.circle(window, (255,255,255), (nuvem_x+200,nuvem_y),(70))
    draw.circle(window, (255,255,255), (nuvem_x+300,nuvem_y),(70))

    window.blit(Kratos, (600,450))


    textoaqui = kratostexto.render("HOMENS, QUEIMEM A VILA", True, (0,0,0))
    window.blit(textoaqui, (570,400))

    display.update()
