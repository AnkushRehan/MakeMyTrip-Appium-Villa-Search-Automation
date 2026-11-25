'''class contains methods related to search the villa'''
from appium.webdriver.common.appiumby import AppiumBy
import time

class VillaSearch:#search the villa in location we send it
    def __init__(self,driver):
        self.driver=driver
        self.searchbox_locator=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId(\"location_box\")')
        self.select_first_result=()

    def searchVilla(self,villa_name):#search the villa location
        self.driver.find_element(*self.searchbox_locator).click()  # click on search box
        self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().className(\"android.view.View\").instance(8)").click()  ##click to add values
        self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText").send_keys(villa_name)  # send_values
        time.sleep(5)
        self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().resourceId(\"hotel_auto_suggest_ui_column_7\").instance(0)").click()  # click on result

    def checkIn(self,checkin_date,checkout_date,month,year):#set the checkin and check out date
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='CHECK-IN']").click()  # checkin click
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=f"{checkin_date} {month} {year} Tap to select").click()  # click on 24
        self.driver.find_element(by=AppiumBy.XPATH,value=f"//c[@content-desc=\"{checkout_date} {month} {year} Tap to select\"]").click()  # click on 25
        self.driver.find_element(by=AppiumBy.ID, value="com.makemytrip:id/btnDone").click()  # done date click

    def guestEntry(self):
        self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().text(\"GUESTS\")").click()  # guest clk
        self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().resourceId(\"room_and_guest_bottom_sheet_content_box\")").click()  # click on done guest

    def getVillas(self):
        self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"search_cta\")").click()  # search villas
