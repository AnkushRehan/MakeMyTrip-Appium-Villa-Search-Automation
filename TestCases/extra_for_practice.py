"""RAW CODE OF MAKEMYTRIP APP """
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time
from selenium.common import NoSuchElementException

def testSearch_Villas(setup):#here we pass the fixture in test
    driver=setup#assign driver return from fixture in driver variable
    time.sleep(10)
    driver.find_element(AppiumBy.ID,"com.makemytrip:id/skip").click()#click to skip login
    driver.find_element(AppiumBy.ID,"com.android.permissioncontroller:id/permission_deny_button").click()#deny notification
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text(\"Villas &\nHomestays\")').click()#click on villa icon
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"location_box\")").click()#click on seach box
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.View\").instance(8)").click()##click to add values
    driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText").send_keys("Delhi")#send_values
    time.sleep(3)
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"hotel_auto_suggest_ui_column_7\").instance(0)").click()#click on result
    driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='CHECK-IN']").click()#checkin click
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="2 DEC 2026 Tap to select").click()#click on 24
    driver.find_element(by=AppiumBy.XPATH, value="//c[@content-desc=\"3 DEC 2026 Tap to select\"]").click()#click on 25
    driver.find_element(by=AppiumBy.ID, value="com.makemytrip:id/btnDone").click()#done date click
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"GUESTS\")").click()#guest clk
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"room_and_guest_bottom_sheet_content_box\")").click()#click on done guest
    time.sleep(3)
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"search_cta\")").click()#search villas
    time.sleep(3)
    #use drag and drop method to drag the offers down
    driver.execute_script("mobile: dragGesture",{"startX":914.0,"startY":1776.0,"endX":872,"endY":1887.9,"speed":1000})
    time.sleep(3)

    #todo : now do swipe up 5 times until you villas matches with target  villa
    deviceScreen=driver.get_window_size() #get the device display size so that we can swipe
    width=deviceScreen['width']#here we write key and fetch the width
    height=deviceScreen['height'] #here we write the key and fetch the height
    for i in range(5):
        villa = driver.find_elements(
            AppiumBy.XPATH,'//android.widget.TextView[@resource-id="tvHotelName" and @text="[icon]  White Rose Near Delhi Airport"]')#here change the villah if not in the result list.
        if villa:
            villa[0].click()
            print("Villa clicked!")
            break
        driver.execute_script("mobile: swipeGesture", {
            "left": int(width * 0.10),
            "top": int(height * 0.20),
            "width": int(width * 0.80),
            "height": int(height * 0.60),
            "direction": "up",
            "percent": 0.75,
            "speed": 1000
        })
    time.sleep(4)

    #TODO:APPLY dragGesture so that the popup will drop down from main result page
    driver.execute_script("mobile: dragGesture",{"startX":918.0,"startY":2144.8,"endX":942.5,"endY":2879.8,"speed":1000})
    time.sleep(3)
    result=driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@resource-id="tv_title"]').text#fetch the text of search result
    print(result)