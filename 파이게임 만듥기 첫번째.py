import pygame
import random
############################################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥피하기") # 게임 이름

# FPS
clock = pygame.time.Clock()
############################################################################################################

# 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 폰트 등)





#움직이는 속도
speed=0.6

#백그라운드
background=pygame.image.load("C:/Users/aaaa/Desktop/python_project_by_Nado-main/nadoProject1/pygame_basic/wallpaper.jpg")

#캐릭터
character=pygame.image.load("C:/Users/aaaa/Desktop/python_project_by_Nado-main/nadoProject1/pygame_basic/character.png")
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_xpos=(screen_width/2)-(character_width/2)
character_ypos=screen_height-character_height

#좌표
to_x=0
to_y=0
#똥
dung=pygame.image.load("C:/Users/aaaa/Desktop/python_project_by_Nado-main/nadoProject1/pygame_basic/dung.png")
dung_size=dung.get_rect().size
dung_width=dung_size[0]
dung_height=dung_size[1]
dung_xpos=random.randint(0,screen_width-dung_width)
dung_ypos=0

# 이벤트 루프
running = True 
while running:
    dt = clock.tick(30) 

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():   
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_RIGHT :
                to_x+=speed
            elif event.key == pygame.K_LEFT:
                to_x-=speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의        
    character_xpos += to_x*dt

    dung_ypos+=10

    # 4. 충돌 처리
    if character_xpos<0 :
        character_xpos=0
    elif character_xpos>screen_width -character_width:
        character_xpos=screen_width - character_width


    if dung_ypos>screen_height :
        dung_ypos=0
        dung_xpos=random.randint(0,screen_width-dung_width)

    character_rect=character.get_rect()
    character_rect.left=character_xpos
    character_rect.top=character_ypos

    dung_rect=dung.get_rect()
    dung_rect.left=dung_xpos
    dung_rect.top=dung_ypos

    if character_rect.colliderect(dung_rect) :
        print("죽었습니다")
        running =False

    # 5. 화면에 그리기

    screen.blit(background,(0,0))
    screen.blit(character,(character_xpos,character_ypos))
    screen.blit(dung,(dung_xpos,dung_ypos))
    pygame.display.update() 


pygame.quit()