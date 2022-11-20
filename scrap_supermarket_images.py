import pyautogui
import time


# https://www.section.io/engineering-education/introduction-to-automation-pyautogui/

# https://pywinauto.readthedocs.io/en/latest/

pyautogui.mouseInfo()



x_coordinates = [412, 532, 592, 772, 832,892,  952  ]
supermarket_names = ['CT_supermarkets__11_14_2022', 'Hua_Lian_supermarket_11_14_2022', 'HL_supermarket_11_14_2022', 'SF_supermarket_11_14_2022', 'SkyFoods', 'Hong_Kong_Supermarket', 'Nature_farm_supermarket']
for i in range(3):
    print(x_coordinates[i])
    # the small icon
    pyautogui.click(x=x_coordinates[i], y=112, duration=0.1)
    time.sleep(3)
    # click to see the post
    pyautogui.click(x=898, y=586, duration=0.1)
    time.sleep(8)
    # click on the discount image so that I can do control + save
    pyautogui.click(x=898, y=586, duration=1)
    time.sleep(8)
    pyautogui.hotkey('ctrl', 's')

    pyautogui.write(supermarket_names[i])
    time.sleep(2)

    # save button
    pyautogui.click(x=1248, y=787, duration=0.1)

    pyautogui.hotkey('alt', 'f4')
    pyautogui.hotkey('alt', 'f4')
    pyautogui.hotkey('alt', 'f4')




# the small icon
pyautogui.click(x=412, y=112, duration=0.1)
time.sleep(3)
# click to see the post
pyautogui.click(x=898, y=586, duration=0.1)
time.sleep(3)
# click on the discount image so that I can do control + save
pyautogui.click(x=898, y=586, duration=0.1)
time.sleep(3)
pyautogui.hotkey('ctrl', 's')
#pyautogui.click(x=900, y=596, duration=0.1)

pyautogui.write('SF_Supermarket_11_14_2022')
time.sleep(2)

pyautogui.click(x=1248, y=787, duration=0.1)





# the msmall icon
pyautogui.click(x=689, y=126, duration=0.1)
time.sleep(3)
pyautogui.click(x=898, y=586, duration=0.1)

time.sleep(3)
pyautogui.click(x=898, y=586, duration=0.1)
time.sleep(3)
pyautogui.hotkey('ctrl', 's')
#pyautogui.click(x=900, y=596, duration=0.1)

pyautogui.write('SF_Supermarket_11_14_2022')
time.sleep(2)

pyautogui.click(x=1248, y=787, duration=0.1)






# insert words
pyautogui.write('SF_Supermarket_11_14_2022')
pyautogui.click(x=1417, y=768, duration=0.1)









pyautogui.moveTo(247,382)

pyautogui.rightClick(x=266, y=391, duration=0.1)
pyautogui.click(x=351, y=572, duration=0.1)


pyautogui.click(x=909, y=564, duration=0.1)

time.sleep(2)







pyautogui.write('Chrome')


pyautogui.write('Chrome')
pyautogui.press('enter')



time.sleep(2)
pyautogui.moveTo(69,750)


pyautogui.click(69,750,duration=1)
pyautogui.write('Chrome')
pyautogui.moveTo(478,363,duration=1)
pyautogui.click(478,363,duration=1)
pyautogui.moveTo(177,58,duration=1)
pyautogui.click(177,58,duration=1)
pyautogui.write('https://www.youtube.com/')
pyautogui.press('enter')
pyautogui.moveTo(458,135,duration=2)
pyautogui.click(458,135,duration=2)
pyautogui.write('perfect strangers')
pyautogui.press('Enter')
pyautogui.moveTo(763,222,duration=3)
pyautogui.click(763,222,duration=3)
pyautogui.moveTo(1253,27,duration=3)
Chrome