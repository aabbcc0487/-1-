import pygame

# 初始化 Pygame
pygame.init()

# 設定視窗大小
width, height = 640, 480

# 創建視窗
screen = pygame.display.set_mode((width, height))

# 載入圖片
player_image = pygame.image.load('player.png')

# 程式主迴圈
running = True
while running:
    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 畫出圖片
    screen.blit(player_image, (0, 0))

    # 更新視窗
    pygame.display.flip()

# 關閉 Pygame
pygame.quit()
"""
import pygame

# 初始化 Pygame 库
pygame.init()

# 设置游戏窗口大小
width, height = 640, 480

# 创建游戏窗口
screen = pygame.display.set_mode((width, height))

# 设置游戏标题
pygame.display.set_caption("My RPG Game")

# 加载游戏资源
player_image = pygame.image.load("player.png").convert_alpha()
monster_image = pygame.image.load("monster.png").convert_alpha()

# 设置游戏循环
clock = pygame.time.Clock()

# 设置游戏状态
game_over = False

# 定义玩家的初始位置
player_x, player_y = 50, 50

# 定义怪物的初始位置
monster_x, monster_y = 400, 300

# 定义玩家攻击力和怪物生命值
player_damage = 10
monster_health = 50

# 游戏循环
while not game_over:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 玩家攻击怪物
                damage = player_damage
                monster_health -= damage
                print(f"你攻擊了史萊姆，造成了 {damage} 點傷害")
                if monster_health <= 0:
                    print("你擊敗了史萊姆！")
                    game_over = True

    # 渲染游戏场景
    screen.fill((255, 255, 255))
    screen.blit(player_image, (player_x, player_y))
    screen.blit(monster_image, (monster_x, monster_y))

    # 更新游戏显示
    pygame.display.update()

    # 设置游戏帧率
    clock.tick(60)

# 退出 Pygame 库
pygame.quit()
"""