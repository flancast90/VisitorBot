import pyautogui as py
import webbrowser as wb
import time

page = ""
num = 0

def main_menu():
    global page, num
    page = input("Enter the URL of the GitHub page with the visitor-badge you would like traffic on: ")
    num = int(input("How many views would you like? "))
    generate(page, num)

def generate(url, views):
    wb.open(url)
    for i in range(views):
         mainloop()
    py.hotkey('ctrl', 'w')

def mainloop():
    time.sleep(1)
    py.hotkey('ctrl', 'l')
    time.sleep(0.2)
    py.write(page)
    time.sleep(0.2)
    py.press('return')
    
main_menu()


