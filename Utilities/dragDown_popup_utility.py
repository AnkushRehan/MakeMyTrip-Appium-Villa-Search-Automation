'''this utility helps to drop down the popup occur on screen'''
def low_dragDown_popup(driver):#little drag down to bottom
    driver.execute_script("mobile: dragGesture",{"startX": 914.0, "startY": 1776.0, "endX": 872, "endY": 1887.9, "speed": 1000})


def heavy_dragDown_popup(driver):#heavy drag and down up to bottom screen
    driver.execute_script("mobile: dragGesture",{"startX":918.0,"startY":2144.8,"endX":942.5,"endY":2879.8,"speed":1000})
