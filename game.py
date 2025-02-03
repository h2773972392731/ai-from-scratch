import pygame
import random

# pip install pygame（可能会很慢）可以使用镜像网站：
# pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pygame 或者 pip install -i https://pypi.doubanio.com/simple/ pygame

# 初始化游戏
pygame.init()

# 设置游戏窗口
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("像素风格的伐木工游戏")

# 设置颜色
black = (0, 0, 0)
brown = (139, 69, 19)
green = (0, 128, 0)

# 设置游戏参数
score = 0
time_left = 30  # 游戏时长（秒）
tree_x = random.randint(50, screen_width - 100)
tree_y = screen_height
tree_speed = 5

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取玩家按键事件
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        # 如果玩家按下空格键，伐木工砍树
        if tree_x < screen_width // 2 < tree_x + 50:
            score += 1
            tree_x = random.randint(50, screen_width - 100)
            tree_y = screen_height
        else:
            score -= 1

    # 移动树
    tree_y -= tree_speed
    if tree_y < 0:
        tree_x = random.randint(50, screen_width - 100)
        tree_y = screen_height

    # 清空屏幕
    screen.fill(black)

    # 绘制树
    pygame.draw.rect(screen, brown, (tree_x, tree_y, 50, 100))

    # 绘制伐木工
    pygame.draw.rect(screen, green, (screen_width // 2 - 25, screen_height - 50, 50, 50))

    # 显示得分和剩余时间
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"得分: {score}", True, green)
    time_text = font.render(f"时间: {time_left} 秒", True, green)
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (screen_width - 150, 10))

    # 更新屏幕
    pygame.display.flip()

    # 游戏结束条件
    if time_left <= 0:
        running = False

    # 控制游戏时长
    pygame.time.delay(1000)  # 暂停1秒
    time_left -= 1

# 游戏结束
pygame.quit()