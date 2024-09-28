import socket
import threading
import curses
from termcolor import colored
import time
import random

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

def wellcome():
    print(colored('ShulkwiSECComuintty مرحبا بك  في' ,'light_yellow'))
    print(colored('Make Things Ready for You\n','yellow'))
    time.sleep(1)
    logotxt = ["""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢀⠀⠀⠀⣰⡇⢀⡄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⣿⣰⡀⢠⣿⣇⣾⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣰⣿⣿⢇⣾⣿⣼⣿⢃⡞⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⢋⣾⣿⣿⣿⣯⣿⠇⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢟⣵⣿⣿⣿⣿⣿⣿⣯⡞⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣵⣿⣿⣿⣿⣿⣿⣿⣿⡿⡁⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣦⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡡⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
    ⠀⠀⢀⣀⣄⣀⡀⡀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡥⠀⠀⠀⠀⠀⠀
    ⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋
     ⣿⣿ 🪶 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀
    ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀
    ⠘⣿⠋⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣀⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡛⠃⠀⠀
    ⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀
    ⠀⠀⠀⠀⠀⢰⣾⣿⣿⣿⣿⣿⠟⠁⠉⠙⠻⠯⡛⠿⠛⠻⠿⠟⠛⠓⠀⠀
    ⠀⠜⡿⠳⡶⠻⣿⣿⣿⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⣠⣽⣧⣾⠛⠉⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠉⠟⠁⠘⠃

    ..... The quieter you become, the more you are able to hear .....
    """,
    """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣤⣤⣤⣀⣀⣀⣀⣀⣀⣀⣤⡤⠶⠶⠶⢶⣤⣤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠶⠾⠛⠛⠋⠉⠉⠉⠉⠉⢉⡉⠉⢙⣿⡿⠛⠉⠀⣀⡀⠀⠀⠀⠀⠉⠛⠷⣦⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠶⠛⠋⠉⠀⠀⢀⣠⣤⣄⣀⣀⣀⣤⣄⠈⠛⢀⡾⠋⠀⠀⠀⣾⡿⠃⠀⠀⠀⠀⠀⠀⠀⠘⢿⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠟⠋⠀⠀⠀⠀⠀⠀⢴⠟⣩⡿⢛⣉⠛⣿⣿⣿⣷⣶⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀⠀⠀⢀⣠⣤⣄⣿⡇⠺⣿⡇⣸⡟⠋⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷
⠀⠀⠀⠀⠀⠀⠀⢀⣴⠏⠀⠀⠀⠀⠀⠀⣠⣾⣿⢿⣟⠛⠻⣿⣛⣳⣶⣾⣿⣦⣾⣃⠄⠀⠀⣀⣠⣤⣴⣶⡶⠶⠶⠞⠛⠛⠻⣿⣶⣄⠀⢸⣿
⠀⠀⠀⠀⠀⠀⣠⡞⠁⠀⠀⠀⠀⠀⠀⠐⠛⠋⠀⠀⢿⣷⣦⣤⣭⣭⣷⣦⣴⣟⣉⣥⣶⠾⠟⠛⠋⠉⠁⠀⠀⠀⠀⢀⣴⣶⣿⡿⠟⠻⣷⣾⡟
⠀⠀⠀⠀⠀⣴⠏⠀⠀⠀⠀⠀⣠⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢉⣿⣿⠿⠟⢛⣩⣵⣶⠖⠀⢰⣞⣋⣥⣴⣶⣶⣾⣿⣿⡿⠋⠀⠀⠀⢹⡟⠀
⠀⠀⠀⢀⣾⠃⠀⠀⠀⠀⠀⣾⣿⣥⣤⡄⠀⠠⠖⢶⣶⡶⠆⠀⠀⠉⠉⠓⠛⠉⠉⢙⣿⣿⣿⡿⠛⢩⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡠⣿⠃⠀⠀⠀⠀⠀⠀⠘⣿⣿⣏⣀⣀⣠⣤⣦⣤⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⣻⣿⠃⠀⣠⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠰⠠⢿⣄⠀⠀⠀⠀⠀⠀⠐⠞⠛⢻⣿⠿⣿⣿⣿⠁⠀⠀⢠⣶⣧⣴⣿⣷⣴⣾⣿⡿⠃⠀⣰⣿⣿⣿⡿⢿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠐⠀⠻⠛⠉⠀⠀⠀⠰⡆⢀⣶⠀⠀⠀⠀⠸⠟⠋⠁⠀⠀⢠⣾⡿⠟⠉⠉⠉⡿⠟⠋⠀⠀⣰⣿⣿⣿⡏⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠄⠀⠀⠀⠀⠀⠀⠀⠀⢠⠟⠁⠀⠀⠀⠀⠀⠀⣾⣿⠟⠁⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡿⡿⠀⠀⠀⢺⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠂⠄⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠐⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠉⠙⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⡀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⣸⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣿⡇⠀⠀⢸⣷⠀⠀⣼⣿⠇⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⠀⠀⠘⠛⠀⢰⣿⠏⠀⠀⠀⠀⠀⠀⠀⢿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠘⣧⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⣿⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡄⠀⠀⠀⠀
⠀⠀⠆⠀⠀⠀⠀⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠙⣦⠀⠀⠀
⠀⠀⣿⠀⠀⠀⠀⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⣠⣤⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⡄⠀⠀⠀⠀⠀⢸⠃⠀⠀
⠐⠀⢙⣧⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⣄⠀⠘⣿⣿⣦⣴⣄⠀⠀⠀⠃⠀⠀
⠀⠰⢞⣿⣆⣾⠀⠁⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⢀⣴⣿⣿⣿⣿⣿⣿⣾⡆⠀⠠⠀⠀⠁⠀⠀⢹⡄⠀⣿⣿⣿⣿⣿⣄⣤⡄⠀⠀⠀
⠀⠈⡽⢽⣿⡇⠀⣀⣼⣿⠀⠀⠀⠀⠀⢀⣀⡀⠀⣾⣇⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡈⠀⢸⣇⢠⡄⠀⠀⢸⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⠀⢀⠀
⠀⠀⠀⠀⢻⣿⣾⣿⣿⣿⢀⣷⣴⣦⣴⣿⣿⣇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠘⣿⣌⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠬⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡛⢁⢻⣿⣿⣿⣿⣿⣿⣄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣹⣿⡴⠄⠀
⠀⢀⡀⡀⣼⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢡⠨⡏⠬⢟⠏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣍⣿⣿⣿⢖⡀
    
    ShulkwiSEC For Cyber Security Solutions/Service
    Stay Safe -_0
    """,
    """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣤⠶⣒⣛⣛⡲⠶⣶⣶⠤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⢻⣭⣶⣶⣶⣶⣶⣦⣽⣿⣿⣿⣷⣾⣥⣝⣶⣭⣗⣲⡕⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣨⣷⣺⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣵⣝⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⡫⢵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⡿⣿⣿⣞⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣟⣯⣾⣿⣿⣿⣿⣿⡍⠉⠙⠛⠟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⣿⣷⢸⣿⣿⣾⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢫⣾⣿⣿⣿⣿⣿⠋⠁⠀⠠⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⠟⢀⣿⠟⣘⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣏⣿⣿⣿⣿⣿⣿⣿⣇⠀⠠⡖⠒⣲⣶⣶⣶⣦⣤⣄⡛⠛⠛⢛⣁⣤⡽⠿⠋⠉⠉⠀⠙⠛⠒⠦⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡅⣼⣿⣿⣿⣿⣿⣿⣿⠗⠀⠱⡀⢿⣿⣤⣧⡼⢻⢻⣿⠟⠉⢻⠟⠁⡰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠈⢳⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⠓⠭⠿⠭⠄⡊⠤⠊⠎⢢⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⢱⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣄⡀⠀⠀⠀⠀⡀⢀⠀⠀⠀⠀⡜⢠⢠⢀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣾⡄
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣨⢅⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡶⠄⣀⣀⡀⠀⠀⡠⢊⣀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇
⠀⠀⠀⠀⠀⠀⠀⢀⡴⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⡘⠠⠋⢀⠤⢒⣒⣒⣒⠢⠤⢤⣄⣀⣀⣀⡀⠀⠀⣼⠁
⠀⠀⠀⠀⠀⠀⠀⣎⠾⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠱⢄⢘⣡⠔⠶⢴⣒⣢⣤⡤⠖⠛⡏⠉⠉⠉⢣⢀⡟⠀
⠀⠀⠀⠀⠀⠀⠸⣴⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠐⠀⠀⢀⠒⣭⠅⠀⠀⠀⠀⠰⠌⠁⠀⡀⣷⠀⠀⠀⠀⠛⠀⠀
⠀⠀⠀⠀⠀⢀⡼⣱⣿⣿⣿⣿⣿⣿⣿⡿⣻⣿⣿⣷⡦⠄⠀⠀⠀⠀⠈⠀⠈⠁⠀⠂⠀⠀⠀⠀⠈⠀⠀⢀⣾⣧⣿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣿⢃⢋⣽⣿⣿⣿⣿⣿⣿⠵⣿⡿⣿⣿⣶⡿⣃⣀⣤⣴⣇⣠⣾⡇⠀⠀⠀⠀⠀⠀⠀⢠⡗⣸⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣾⣿⢟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣶⣿⣿⣿⣿⣿⢿⣿⣿⢿⣿⡟⠀⠀⢀⡄⠀⠀⠀⢀⣾⣿⣿⣿⣿⣯⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣿⣿⣯⣶⢖⣸⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣃⣿⣭⣾⣿⣯⣤⣴⣾⣿⢇⢌⣾⡆⣼⣿⣿⣿⣿⣏⢃⠃⠀⠀⠀⠀⠀⠀
⠠⣫⠾⣻⣿⢿⣿⠫⠾⠿⠿⣿⡛⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣷⣄⡀⠀⠀⠀⠀⠀
⠐⠁⣼⠟⢡⣿⠿⣿⣿⣿⡿⢟⣡⢖⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣻⢹⣇⡀⠀⠀⠀⠀⠀
⠀⠐⠁⢀⠟⢁⣾⣿⠿⣿⣾⣿⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⣿⢓⣛⣿⣿⡿⢆⡀⠀⠀⠀
⠀⠀⠀⠊⢀⡞⠉⠀⣴⠟⣻⣷⣶⣶⣾⣭⣽⣿⣭⣵⡾⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣉⠿⣩⣣⣿⣷⡞⢟⠟⣿⢛⠆⠈⠂⠀⠀
⠀⠀⠀⠀⠈⠀⠀⠐⠁⣼⠟⢻⣿⣿⡿⠿⢿⣿⣿⣟⣟⣻⣿⣻⣿⣭⢇⡿⣛⢻⣿⣋⢿⢣⣿⣿⢿⣿⣿⡇⠀⠀⠀⠙⠈⠌⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠛⠋⠀⣀⣴⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣬⣾⣿⣟⣷⣿⣶⣿⠟⠁⠀⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠞⠛⠉⠀⠀⠀⠀⣼⠿⠋⠀⠉⢹⣿⡿⣿⣿⢿⣿⠏⠃⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠏⢠⡿⠁⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    Can YOu SEE ME. ?
    """,
    """
/ ___|| |__  _   _| | | ____      _(_) ___|| ____/ ___|
\___ \| '_ \| | | | | |/ /\ \ /\ / / \___ \|  _|| |    
 ___) | | | | |_| | |   <  \ V  V /| |___) | |__| |___ 
|____/|_| |_|\__,_|_|_|\_\  \_/\_/ |_|____/|_____\____|
                                                                                                                                                                                                                                                                                                              
    """
    ]
    logotxt = random.choice(logotxt)
    logo = logotxt.split('\n')
    for line in logo:
        print(colored(line, 'light_green'))
        time.sleep(0.1)
    time.sleep(4)


def receive_messages(client_socket, chat_win, input_win):
    while True:
        try:
            message = client_socket.recv(1024).decode('UTF-8')
            if not message:
                break
            remote_ip, remote_port = client_socket.getpeername()
            
            # Split message into parts
            parts = message.split(': ', 1)
            sender_info = f"[{remote_ip}:{remote_port}]: "
            content = parts[1] if len(parts) > 1 else parts[0]
            
            # Display sender info in magenta
            chat_win.addstr(sender_info, curses.color_pair(2))
            
            # Display content (rest of the message) in default color
            chat_win.addstr(content + "\n", curses.color_pair(2))
            curses.color_pair(1)
            
            chat_win.refresh()
            input_win.refresh()
        except Exception as e:
            chat_win.addstr(f"Error receiving message: {e}\n", curses.color_pair(3))
            chat_win.refresh()
            input_win.refresh()
            break

def main(stdscr):
    curses.curs_set(1)  # Show the cursor
    stdscr.clear()
    stdscr.refresh()

    curses.start_color()
    curses.use_default_colors()

    # Define color pairs
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)    # Me (green text)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # Remote info (magenta text)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)      # Error (red text)

    height, width = stdscr.getmaxyx()

    chat_win = curses.newwin(height - 3, width, 0, 0)
    input_win = curses.newwin(3, width, height - 3, 0)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket, chat_win, input_win))
    receive_thread.daemon = True
    receive_thread.start()

    while True:
        input_win.clear()
        input_win.addstr("\n Message: ")
        input_win.refresh()
        curses.echo()
        message = input_win.getstr(1, 10).decode('UTF-8')
        curses.noecho()
        if message.strip() != "":
            if message == 'exit()' or message == 'quite()':
                exit(0)
            client_socket.send(message.encode('UTF-8'))
            
            # Display my message in green
            chat_win.addstr("Me: ", curses.color_pair(1))
            chat_win.addstr(message + "\n", curses.color_pair(1))
            curses.color_pair(0)
            
            chat_win.refresh()
            input_win.refresh()

if __name__ == "__main__":
    wellcome()
    try:
        curses.wrapper(main)
    except ConnectionError or ConnectionRefusedError:
        print(colored('Error: ', 'red') + colored('Next Time...! ,Server iS OFF nOW','light_green'))
    except Exception as error:
        print(colored('ERORR: ','red') + colored(error,'red'))