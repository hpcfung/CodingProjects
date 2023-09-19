import pyautogui, time, keyboard


if __name__ == "__main__":
    """
    Press q to record current mouse position
    266, 112
    1620, 1072
    """
    measuring = False

    if measuring:
        while True:  # making a loop
            if keyboard.is_pressed('q'):  # if key 'q' is pressed
                print(pyautogui.position())
                break  # finishing the loop
    else:
        time.sleep(4)
        pyautogui.moveTo(1620, 1072)


    # try:
    #     while True:
    #         pass
    # except KeyboardInterrupt:
    #     print(pyautogui.position())


    # print(pyautogui.size())
    # time.sleep(10)
    # print(pyautogui.position())

    # chrome button: x=520, y=1041
    # when F11: x=601, y=110
    # x=1283, y=1073