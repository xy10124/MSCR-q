import pyautogui,time,easygui
print("日志:")
print("使用说明:请提前将要刷的文字复制到剪贴板中。输入完次数和间隔的秒数后三秒后会开始刷屏，请提前请在三秒内进入MC中。")
count = 0
b=0
easygui.msgbox("使用说明:请提前将要刷的文字复制到剪贴板中。输入完次数和间隔的秒数后三秒后会开始刷屏，请提前请在三秒内进入MC中。如果没有效果，您把打开聊天的按键改成T。")
a = easygui.enterbox(msg="请输入刷屏的次数:", title="MC聊天机器人", default="", strip=True, image=None, root=None)
b = easygui.enterbox(msg="请输入间隔的秒数:", title="MC聊天机器人", default="", strip=True, image=None, root=None)
easygui.msgbox("将在三秒后开始刷屏。")
a=int(a)
b=float(b)
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("0")
while (count < a):
        time.sleep(b)
        pyautogui.press('t')
        pyautogui.keyDown('Ctrl')    
        pyautogui.press('V')    
        pyautogui.keyUp('Ctrl')
        pyautogui.press('Enter')
        count = count + 1
        print("已完成"+str(count)+"次")
print("已全部完成，程序已退出.")