import pygame#Culminating Project by james cai 2018 June 18th
import random#Setting the initial value
import sys
import os
pygame.init()
size = width,length=800,600
window = pygame.display.set_mode((size))
pygame.display.set_caption("CLICK!")
white = [225,225,225]
black = [0,0,0]
gery =[100,100,100]
green=[0,255,0]
purple = [153,50,204]
yellow = [255,185,15]
sword = pygame.image.load("sword.png")#load the image
sword1 = pygame.image.load("sword1.png")
sword = pygame.transform.scale(sword, (60, 60))
sword1 = pygame.transform.scale(sword1, (60, 60))
red = [255,0,0]
brown = [139,69,19]
color=[white,black,green,purple,gery,yellow,red,brown]#setting color

lv = [1]#setting the initial value of the player, also make the load/save function have value to work.
attack = [10]
gold_num = [0]
exp = [0]
Player_health = [300]
Item_list = [False,False,False,False,False,False,False,False,False,False]

def SWORD (sword_anime,sword,sword1):#The function that displaying a sword on the mouse cursor and also make the animation of the sword after the player click the left button.
    sword_pos = pygame.mouse.get_pos()
    if sword_anime == 0:
        window.blit(sword1, (sword_pos[0] - 37, sword_pos[1] - 37))
    else:
        window.blit(sword, (sword_pos[0] - 37, sword_pos[1] - 37))
    pygame.display.update()


save_num = [1]
def save(save_num,lv,attack,gold_num,exp,Player_health,Item_list):#The function that create a file and then save the player's different value in the file that can loading them after.
    f = open("save"+str(save_num[0]) ,"w")
    f.write("Gold:   "+str(gold_num[0])+" \n")
    f.write("exp:    "+str(exp[0])+" \n")
    f.write("attack: "+str(attack[0])+" \n")
    f.write("lv:     "+str(lv[0])+" \n")
    f.write("health: " + str(Player_health[0]) + " \n")
    for item in range(len(Item_list)):
        f.write(str(Item_list[item])+"\n")
    save_num[0] += 1


def file_name():#The function that search for all the save file in the folder that program located.
    file_dir = os.path.abspath('.')
    File_name = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            for i in range(99):
                if os.path.splitext(file)[0] == 'save' + str(i):
                    FN = os.path.join(root, file)
                    File_name.append(FN[len(FN)-5:])
        return File_name


def loadfile(i,File_name,lv,attack,gold_num,exp,Player_health,Item_list):#The function that can read the save file and load the value in the save file and replace them to the game.
    f = open(File_name[i], "r")
    f.seek(0, 0)
    gold_num[0] = int(f.readline(999)[8:])
    exp[0] = int(f.readline(999)[8:])
    attack[0] = int(f.readline(999)[8:])
    lv[0] = int(f.readline(999)[8:])
    Player_health[0] = int(f.readline(999)[8:])
    for ITEM in range(len(Item_list)):
        Item = f.readline(999)
        if Item == "True"+"\n":
            Item_list[ITEM] = True
        if Item == "False"+"\n":
            Item_list[ITEM] = False
    print("Load "+ File_name[i] + " success")


def load_save():#This function create a page that we can display the save file on it, and player can choose which file they want to load
    menu = False
    File_name = file_name()
    while menu == False:
        font1 = pygame.font.SysFont(None, 60)
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] >= 680 and mouse[0] <= 800:
                        if mouse[1] <= 600 and mouse[1] >= 550:
                            menu = True

        window.fill(color[1])
        file_y = 100
        count = 0
        for i in range(len(File_name)):
            display = font1.render(File_name[i],1,color[0])
            if (count+1)*150 >= width:
                file_y += 100
                count = 0
            file_x = count*200
            window.blit(display, (file_x,file_y ))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                mouse = pygame.mouse.get_pos()
                if mouse[0] >= file_x and mouse[0] <= file_x + 100:
                    if mouse[1] <= file_y + 50 and mouse[1] >= file_y:
                        loadfile(i,File_name,lv,attack,gold_num,exp,Player_health,Item_list)
                        menu = True
            count += 1
        load = font1.render("LOAD", 1, color[0])
        back = font1.render("back", 1, color[0])
        window.blit(load, (300, 20))
        window.blit(back, (700, 550))
        pygame.display.update()
        clock.tick(60)


def SHOP(attack,Gold,gold_num,cost_num):#The function that create the blacksmith shop page.
    sword_anime = 1
    game = False
    display = 0
    shop = pygame.image.load("SHOP.PNG")
    shop1 = pygame.image.load("SHOP1.PNG")
    blacksmith = False
    font = pygame.font.SysFont(None, 50)
    GOLD = pygame.font.SysFont(None,30)
    while game == False:
        clock = pygame.time.Clock()
        for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                         sys.exit()
                     if event.type == pygame.KEYDOWN:
                         if event.key == pygame.K_ESCAPE:
                             game = True
                     if event.type == pygame.MOUSEBUTTONDOWN:
                         sword_anime = 0
                         mouse = pygame.mouse.get_pos()
                         if pygame.mouse.get_pressed() == (1, 0, 0):
                             if mouse[0] >= 80 and mouse[0] <= 720:
                                 if mouse[1] <= 530 and mouse[1] >= 50:
                                     if gold_num >= cost_num:
                                         blacksmith = True
                                         if Item_list[9] == True:#There make the player's damage and the gold cost increase.
                                             attack[0] += 2
                                         else:
                                            attack[0] += 1
                                         gold_num[0] -= cost_num[0]
                                         cost_num[0] += 1

                                         if Item_list[8] == True:
                                             if cost_num[0] >= 10:
                                                cost_num[0] = 10
                             if mouse[0] >= 680 and mouse[0] <= 800:
                                 if mouse[1] <= 600 and mouse[1] >= 550:
                                     game = True
                     if event.type == pygame.MOUSEBUTTONUP:
                         sword_anime = 1
        window.fill(color[7])
        if blacksmith == True:
            window.blit(shop1, (80, 50))
            display += 1
        else:
            window.blit(shop, (80, 50))
        if display % 10 == 0:
            blacksmith = False
        window.blit(Gold, (0, 100))
        window.blit(GOLD.render(str(gold_num[0]), 1, color[0]), (50, 100))
        window.blit(font.render("SHOP", 1, color[1]),(350,0))
        window.blit(font.render("back", 1, color[0]), (690, 550))
        window.blit(Gold, (455, 155))
        window.blit(font.render("x"+str(cost_num[0]),1,color[1]),(500,155))
        SWORD(sword_anime, sword, sword1)
        pygame.display.update()
        clock.tick(60)


def store1(attack, Gold, gold_num,cost_num):#This function create a store page that have different item that player can buy to help them kill the monster.
    STORE = False
    Shop = pygame.image.load("S.png")#load the clips
    Items1 = pygame.image.load("p1.png")
    Items2 = pygame.image.load("p2.png")
    Items3 = pygame.image.load("p3.png")
    Items4 = pygame.image.load("p4.png")
    Items5 = pygame.image.load("p5.png")
    Items6 = pygame.image.load("p6.png")
    Items7 = pygame.image.load("p7.png")
    Items8 = pygame.image.load("p8.png")
    Items9 = pygame.image.load("p9.png")
    Items10 = pygame.image.load("p10.png")
    Shop = pygame.transform.scale(Shop, (800, 600))
    sword_anime = 1
    Price = False
    while STORE == False:
        font1 = pygame.font.SysFont(None, 40)
        font2 = pygame.font.SysFont(None, 60)
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    STORE = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                sword_anime = 0
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] >= 10 and mouse[0] <= 110:
                        if mouse[1] <= 600 and mouse[1] >= 425:
                            SHOP(attack, Gold, gold_num,cost_num)
                    if mouse[0] >= 660 and mouse[0] <= 790:
                        if mouse[1] <= 405 and mouse[1] >= 220:
                            STORE = True
                    if Item_list[0] != True:#there player can choose the different item on the store page.
                        if mouse[0] >= 200 and mouse[0] <= 250:#item1
                            if mouse[1] >= 30 and mouse[1] <= 80:
                                Price = True
                                Price_num1 = 400
                                Item = 0
                                Price_num = font1.render(":"+str(Price_num1), 1, color[0])
                                describe = font1.render("Get more gold every time you kill a monster." , 1, color[1])
                    if Item_list[1] != True:
                        if mouse[0] >= 350 and mouse[0] <= 400:#item2
                            if mouse[1] >= 30 and mouse[1] <= 80:
                                Price = True
                                Price_num1 = 900
                                Item = 1
                                Price_num = font1.render(":" + str(Price_num1), 1, color[0])
                                describe = font1.render("Double your damage(Can buy repeatedly)", 1, color[1])
                    if Item_list[2] != True:
                        if mouse[0] >= 500 and mouse[0] <= 550:#item3
                            if mouse[1] >= 30 and mouse[1] <= 80:
                                Price = True
                                Price_num1 = 321
                                Item = 2
                                Price_num = font1.render(":" + str(Price_num1), 1, color[0])
                                describe = font1.render("Restore 3 health everytime you kill a monster.", 1, color[1])
                    if Item_list[3] != True:
                        if mouse[0] >= 200 and mouse[0] <= 250:#item4
                            if mouse[1] >= 120 and mouse[1] <= 170:
                                Price = True
                                Price_num1 = 315
                                Item = 3
                                Price_num = font1.render(":" + str(Price_num1), 1, color[0])
                                describe = font1.render("Attack automatically.", 1, color[1])
                    if Item_list[4] != True:
                        if mouse[0] >= 350 and mouse[0] <= 400:#item5
                            if mouse[1] >= 120 and mouse[1] <= 170:
                                Price = True
                                Price_num1 = 500
                                Item = 4
                                Price_num = font1.render(":" + str(Price_num1), 1, color[0])
                                describe = font1.render("Take less damage from monster.", 1, color[1])
                    if Item_list[5] != True:
                        if mouse[0] >= 500 and mouse[0] <= 550:#item6
                            if mouse[1] >= 120 and mouse[1] <= 170:
                                Price = True
                                Price_num1 = 322
                                Item = 5
                                Price_num = font1.render(":" + str(Price_num1), 1, color[0])
                                describe = font1.render("Gain more Exp.", 1, color[1])
                    if Item_list[6] != True:
                        if mouse[0] >= 200 and mouse[0] <= 250:#item7
                            if mouse[1] >= 220 and mouse[1] <= 270:
                                Price = True
                                Price_num1 = 300
                                Item = 6
                                Price_num = font1.render(":" + str(Price_num1), 1, color[0])
                                describe = font1.render("Increase maximum health and fill health bar.", 1, color[1])
                    if Item_list[7] != True:
                        if mouse[0] >= 350 and mouse[0] <= 400:#item8
                            if mouse[1] >= 220 and mouse[1] <= 270:
                                Price = True
                                Price_num1 = 112
                                Item = 7
                                Price_num = font1.render(":" + str(Price_num1), 1, color[0])
                                describe = font1.render("Gain some Exp every time you upgrade.", 1, color[1])
                    if Item_list[8] != True:
                        if mouse[0] >= 200 and mouse[0] <= 250:#item9
                            if mouse[1] >= 320 and mouse[1] <= 370:
                                Price = True
                                Price_num1 = 150
                                Item = 8
                                Price_num = font1.render(":" + str(Price_num1), 1, color[0])
                                describe = font1.render("Blacksmith's price cost 10 Gold max.", 1, color[1])
                    if Item_list[9] != True:
                        if mouse[0] >= 350 and mouse[0] <= 400:#item10
                            if mouse[1] >= 320 and mouse[1] <= 370:
                                Price = True
                                Price_num1 = 250
                                Item = 9
                                Price_num = font1.render(":" + str(Price_num1), 1, color[0])
                                describe = font1.render("Attack increase more from Blacksmith.", 1, color[1])
                    if Price == True:
                        if mouse[0] >= 600 and mouse[0] <= 720:
                            if mouse[1] >= 450 and mouse[1] <= 500:
                                if Item_list[Item] == False:
                                    if gold_num[0] > Price_num1:
                                        Item_list[Item] = True
                                        gold_num[0] -= Price_num1
            if event.type == pygame.MOUSEBUTTONUP:
                sword_anime = 1

        window.blit(Shop,(0,0))
        if Item_list[0] != True:#the item will not be display on the screen after the player buy them.
            window.blit(Items1, (200, 30))
        if Item_list[1] != True:
            window.blit(Items2, (350, 30))
        if Item_list[2] != True:
            window.blit(Items3, (500, 30))
        if Item_list[3] != True:
            window.blit(Items4, (200, 120))
        if Item_list[4] != True:
            window.blit(Items5, (350, 120))
        if Item_list[5] != True:
            window.blit(Items6, (500, 120))
        if Item_list[6] != True:
            window.blit(Items7, (200, 220))
        if Item_list[7] != True:
            window.blit(Items8, (350, 220))
        if Item_list[8] != True:
            window.blit(Items9, (200, 320))
        if Item_list[9] != True:
            window.blit(Items10, (350, 320))
        gold = font1.render(str(gold_num[0]), 1, color[0])
        window.blit(Gold, (0, 100))
        window.blit(gold, (50, 100))
        if Price == True:#draw the different information of item on the screen.
            window.blit(Gold,(200,450))
            window.blit(Price_num,(250,450))
            pygame.draw.rect(window, color[5], (600, 450, 120, 50))
            pygame.draw.rect(window, color[7], (600, 450, 120, 50),8)
            window.blit(font2.render("BUY", 1, color[1]),(618, 460))
            window.blit(describe,(170,520))
        count = 0
        count += 1
        SWORD(sword_anime, sword, sword1)
        pygame.display.update()
        clock.tick(60)


def GAMEOVER():#gameover page.
    game = False
    window.fill(color[1])
    font1 = pygame.font.SysFont(None, 60)
    while game == False:
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        gameover = font1.render("YOU DEAD", 1, color[0])
        window.blit(gameover,(270,300))
        pygame.display.update()
        clock.tick(60)


def StartMenu():# The startMenu page which have three buttom - start,load and exit-.
     game = False
     start_size = 50
     exit_size = 50
     load_size = 50
     while game == False:
         exit = pygame.font.SysFont(None, exit_size)
         start = pygame.font.SysFont(None, start_size)
         load = pygame.font.SysFont(None,  load_size)
         font1 = pygame.font.SysFont(None, 150)
         clock = pygame.time.Clock()
         for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                      sys.exit()
                  if event.type == pygame.MOUSEBUTTONDOWN:
                      if pygame.mouse.get_pressed() == (1, 0, 0):
                          if mouse[0] >= 300 and mouse[0] <= 500:
                              if mouse[1] >= 300 and mouse[1] <= 350:
                                  game = True
                          if mouse[0] >= 300 and mouse[0] <= 500:
                              if mouse[1] >= 375 and mouse[1] <= 425:
                                  load_save()
                          if mouse[0] >= 300 and mouse[0] <= 500:
                              if mouse[1] >= 450 and mouse[1] <= 500:
                                  sys.exit()
         start_size = 50
         load_size = 50
         exit_size = 50
         mouse = pygame.mouse.get_pos()
         if mouse[0]>= 300 and mouse[0]<= 500:#the size of buttom will change after you put mouse on it
              if mouse[1] >= 300 and mouse[1] <= 350:
                      start_size = 75
         if mouse[0]>= 300 and mouse[0]<= 500:
              if mouse[1] >= 375 and mouse[1] <= 425:
                      load_size = 75
         if mouse[0]>= 300 and mouse[0]<= 500:
              if mouse[1] >= 450 and mouse[1] <= 500:
                      exit_size = 75
         menu_title = font1.render("CILCK!", 1, color[0])
         menu_start = start.render("START", 1, color[0])
         menu_load = load.render("LOAD", 1, color[0])
         menu_exit = exit.render("EXIT", 1, color[0])
         window.fill(color[1])
         window.blit(menu_title, (225,100))
         window.blit(menu_start, (320, 300))
         window.blit(menu_load, (320, 375))
         window.blit(menu_exit, (320, 450))
         pygame.display.update()
         clock.tick(60)


def GAME(lv,attack,gold_num,exp,Player_health,Item_list):#The main game loop
     quit = False
     health = 100
     health_max = health
     Player_health_max = 300
     exp_bar = 100
     background = pygame.image.load("background.jpg")
     background = pygame.transform.scale(background, (800, 600))
     monster1_1 = pygame.image.load("monster1-1.png")#load and transfer the image to the right size.
     monster1_2 = pygame.image.load("monster1-2.png")
     monster2_1 = pygame.image.load("monster2-1.png")
     monster2_2 = pygame.image.load("monster2-2.png")
     monster3_1 = pygame.image.load("monster3_1.png")
     monster3_2 = pygame.image.load("monster3_2.png")
     monster4_1 = pygame.image.load("monster4_1.png")
     monster4_2 = pygame.image.load("monster4_2.png")
     monster5_1 = pygame.image.load("monster5_1.png")
     monster5_2 = pygame.image.load("monster5_2.png")
     monster1_1 = pygame.transform.scale(monster1_1, (300, 300))
     monster1_2 = pygame.transform.scale(monster1_2, (300, 300))
     monster2_1 = pygame.transform.scale(monster2_1, (300, 300))
     monster2_2 = pygame.transform.scale(monster2_2, (300, 300))
     monster3_1 = pygame.transform.scale(monster3_1, (300, 300))
     monster3_2 = pygame.transform.scale(monster3_2, (300, 300))
     monster4_1 = pygame.transform.scale(monster4_1, (300, 300))
     monster4_2 = pygame.transform.scale(monster4_2, (300, 300))
     monster5_1 = pygame.transform.scale(monster5_1, (300, 300))
     monster5_2 = pygame.transform.scale(monster5_2, (300, 300))
     monster_list = [[monster1_1,monster1_2],[monster2_1,monster2_2],[monster3_1,monster3_2],[monster4_1,monster4_2],[monster5_1,monster5_2]]#adding all the clip in a list which can using them easier.

     monster_display1 = monster_list[0][1]#set the initial monster
     monster_display2 = monster_list[0][0]
     monster = 0
     Gold = pygame.image.load("Gold.png")
     Gold = pygame.transform.scale(Gold, (40, 40))
     monster_touch = monster_display1.get_rect()
     monster_touch = monster_touch.move(250, 200)
     hint = False
     display = 0
     GOLD = pygame.font.SysFont(None, 30)
     character = pygame.font.SysFont(None, 50)
     cost_num = [1]
     sword_anime = 1
     attack_time = 0
     Item7 = False
     while quit == False:
         clock = pygame.time.Clock()
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 sys.exit()
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE:
                     StartMenu()
             if event.type == pygame.MOUSEBUTTONDOWN:
                 if pygame.mouse.get_pressed() == (1, 0, 0):
                     sword_anime = 0
                     mouse = pygame.mouse.get_pos()
                     if mouse[0] >= monster_touch.left and mouse[0] <= monster_touch.right:#Detect if monster get click.
                         if mouse[1] <= monster_touch.bottom and mouse[1] >= monster_touch.top:
                             if Item_list[1] == True:
                                 attack[0] = attack[0]*2
                                 Item_list[1] = False
                             health -= attack[0]#decrease the monster's health
                             hint = True
                     if mouse[0] >= 680 and mouse[0] <= 800:
                         if mouse[1] <= 600 and mouse[1] >= 540:
                             store1(attack, Gold, gold_num, cost_num)

                     if mouse[0] >= 0 and mouse[0] <= 130:
                         if mouse[1] <= 600 and mouse[1] >= 540:
                             save(save_num, lv, attack, gold_num, exp,Player_health,Item_list)
             if event.type == pygame.MOUSEBUTTONUP:
                 sword_anime = 1
         if exp[0] >= exp_bar:#level up
             health_max = health_max * 1.5
             lv[0] += 1
             if Item_list[7] == True:#Item that can let player gain Exp after level up.
                 exp[0] = random.randint(30,60)
             else:
                exp[0] = 0
             attack[0] += 5

         if health < 0:#when the monster get killed
             attack_time = 0
             health = health_max
             if Item_list[5] == True:
                exp[0] += 40
             else:
                exp[0] += 20
             if Item_list[0] == True:
                gold_num[0] += random.randint(5,20)*lv[0]
             else:
                gold_num[0] += random.randint(1,10)*lv[0]
             if Item_list[2] == True:
                 if Player_health[0] <= Player_health_max:
                    Player_health[0] += 3
             monster_change = random.randint(1,5)
             while monster_change == monster:# generate a number that choose another monster's clip to display.
                 monster_change = random.randint(1, 5)
             monster = monster_change
             if monster == 1:
                 monster_display1 = monster_list[0][1]
                 monster_display2 = monster_list[0][0]
             if monster == 2:
                 monster_display1 = monster_list[1][1]
                 monster_display2 = monster_list[1][0]
             if monster == 3:
                 monster_display1 = monster_list[2][1]
                 monster_display2 = monster_list[2][0]
             if monster == 4:
                 monster_display1 = monster_list[3][0]
                 monster_display2 = monster_list[3][1]
             if monster == 5:
                 monster_display1 = monster_list[4][1]
                 monster_display2 = monster_list[4][0]

         window.blit(background,(0,0))

         if Item_list[6] == True and Item7 == False:#Item that can increase player's max health
             Player_health_max += 100
             Player_health[0] = Player_health_max
             Item7 = True
         if Item_list[6] == False:#let the item event only happend once.
             Player_health_max = 300
             Item7 = False

         if health <= (health_max*(2/3)) and health >= (health_max/3):#make the color of health different when the health decrease
             pygame.draw.rect(window, color[5], (300, 150, 200-((health_max - health)/(health_max/200)), 20))#make the monster's health display on the screen according to a certain proportion
         if health <= (health_max/3):
             pygame.draw.rect(window, color[6], (300, 150, 200-((health_max - health)/(health_max/200)), 20))
         if health >= health_max*(2/3):
             pygame.draw.rect(window, color[2], (300, 150, 200-((health_max - health)/(health_max/200)), 20))
         pygame.draw.rect(window, color[0], (300, 150, 200, 20), 4)

         if Player_health[0] <= (Player_health_max*(2/3)) and Player_health[0] >= (Player_health_max/3):#make the color of health different when the health decrease
             pygame.draw.rect(window, color[5], (0, 50, Player_health[0], 12))
         if Player_health[0] <= (Player_health_max/3):
             pygame.draw.rect(window, color[6], (0, 50, Player_health[0], 12))
         if Player_health[0] >= Player_health_max*(2/3):
             pygame.draw.rect(window, color[2], (0, 50, Player_health[0], 12))
         pygame.draw.rect(window, color[0], (0, 50, Player_health_max, 12), 4)

         pygame.draw.rect(window, color[3], (0, 70, exp[0], 10))
         pygame.draw.rect(window, color[4], (0, 70, exp_bar, 10), 2)
         if hint == True:#display the animation when the monster get hint.
             attack_value = character.render("-"+str(attack[0]), 1, color[6])
             window.blit(monster_display1, (250, 200))
             window.blit(attack_value, (mouse[0] + display, mouse[1] - 30 - display))
             display += 1
         else:
             window.blit(monster_display2, (250, 200))
         if display %10 == 0:#the time that animetion displaying.
             hint = False
             display = 0

         attack_time += 1
         if Item_list[3] == True:#item that can Attack automatically.
             if attack_time % 30 == 0:
                 health -= attack[0]
         if attack_time%300== 0:#item that let player get less damage from monster.
             if Item_list[4] == True:
                 Player_health[0] -= 15
             else:
                Player_health[0] -= 30
             window.fill(color[6])
         if Player_health[0]<= 0:
             GAMEOVER()

         store = character.render("SHOP", 1, color[0])
         SAVE = character.render("SAVE", 1, color[1])
         pygame.draw.rect(window, color[4], (680, 540, 130, 60))
         pygame.draw.rect(window, color[5], (0, 540, 130, 60))
         window.blit(store, (690, 550))
         window.blit(SAVE, (0, 550))
         lv1 = character.render("LV:"+str(lv[0]), 1, color[0])
         window.blit(lv1, (0, 10))
         gold = GOLD.render(str(gold_num[0]), 1, color[0])
         window.blit(Gold, (0, 200))
         window.blit(gold, (50, 200))



         SWORD(sword_anime, sword, sword1)

         pygame.display.update()
         clock.tick(60)



StartMenu()
GAME(lv,attack,gold_num,exp,Player_health,Item_list)
pygame.quit()


