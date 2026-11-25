"function  helps to get the screen height and width "
def get_screen_ratio(driver):
    deviceScreen = driver.get_window_size()  # get the device display size so that we can swipe
    width = deviceScreen['width']  # here we write key and fetch the width
    height = deviceScreen['height']  # here we write the key and fetch the height
    return width,height


"""how to call in testcase ?
-just call the function and fetch the height and width as shown bellow 
height,width=get_screen_ration(driver)#pass the driver to utility
height=height
width=width
"""
