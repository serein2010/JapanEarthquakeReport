import time
import os
import json
import datetime
import pygame
import pygame.locals
import ctypes

# 初始化 pygame
pygame.init()

# 屏幕大小
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 200

# 颜色
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# 加载顶部图片
top_image = pygame.image.load('core/img/top.png')  # 请确保图片路径正确

# 字体
font = pygame.font.SysFont('Microsoft YaHei', 36, bold=True)  # 字体加粗

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("core/sound/warning.wav")
    pygame.mixer.music.play()

def create_alert_window(location, magnitude):
    global stop_detection
    # 再次初始化 pygame
    pygame.init()
    # 获取屏幕信息
    infoObject = pygame.display.Info()
    # 计算窗口在屏幕正中间的位置
    x = (infoObject.current_w - SCREEN_WIDTH) // 2
    y = (infoObject.current_h - SCREEN_HEIGHT) // 2

    # 创建屏幕并设置位置
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
    pygame.display.set_caption("地震警报")
    ctypes.windll.user32.SetWindowPos(pygame.display.get_wm_info()['window'], -1, x, y, 0, 0, 0x0001 | 0x0002)

    # 显示顶部图片
    screen.blit(top_image, (0, 0))

    # 背景蓝色
    screen.fill(BLUE)

    # 显示文本
    if location:  # 检查 location 是否为空
        location_text = font.render(f"震源：{location}", True, YELLOW)
        screen.blit(location_text, (50, 70))
    if magnitude:  # 检查 magnitude 是否为空
        magnitude_text = font.render(f"震级：{magnitude}", True, YELLOW)
        screen.blit(magnitude_text, (50, 120))
    title = font.render(f"紧急地震速报", True, WHITE)
    screen.blit(title, (100,0))
    cut = font.render(f"——————————————————————", True, WHITE)
    screen.blit(cut, (0,25))

    # 创建右下角的退出按钮
    exit_button = pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 50, 100, 50)
    pygame.draw.rect(screen, RED, exit_button)
    exit_text = font.render("退出", True, BLUE)
    screen.blit(exit_text, (SCREEN_WIDTH - 80, SCREEN_HEIGHT - 40))

    # 刷新屏幕
    pygame.display.flip()

    # 主循环
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    running = False
                    stop_detection = False  # 允许重新检测

    pygame.display.quit()  # 正确关闭显示

stop_detection = False

while True:
    if os.path.exists('data/json/eq.json'):
        with open('data/json/eq.json', 'r', encoding="UTF-8") as f:
            data = json.load(f)
            origin_time_str = data['OriginTime']  # 假设 OriginTime 是日期字符串
            origin_time_str = origin_time_str.split(' ')[0]  # 去除时间部分，只保留日期
            origin_time = datetime.datetime.strptime(origin_time_str, '%Y/%m/%d')  # 按照日期格式解析
            current_date = datetime.date.today()
            if origin_time.date() == current_date and data['Magunitude'] > 3:  # 修正键名
                print("检测完成")  # 输出检测完成
                location = data['Hypocenter']
                magnitude = data['Magunitude']
                play_sound()
                create_alert_window(location, magnitude)
                stop_detection = True
    else:
        stop_detection = False  # 如果文件不存在，也允许重新检测
    time.sleep(3)