#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
# ~ from alien import Alien
import game_functions as gf

def run_game():
    # 初始化游戏，创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption('Alien Invasion')
    
    #创建play按钮
    play_button = Button(ai_setting, screen, "Play")
    
    # 创建存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting, screen, stats)
    
    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_setting,screen)
    bullets = Group()
    aliens = Group()
    
    # 创建外星人群
    gf.create_fleet(ai_setting,screen,ship,aliens)
    
    # 开始游戏主循环
    while True:
        
        # 监视键盘和鼠标事件
        gf.check_event(ai_setting, screen, stats, sb, play_button, ship, 
            aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, stats, sb, ship, aliens, 
                bullets)
            gf.update_aliens(ai_setting, screen, stats, sb, ship, aliens, 
                bullets)
        
        gf.update_screen(ai_setting, screen, stats, sb, ship, aliens, 
            bullets, play_button)
       
run_game()
