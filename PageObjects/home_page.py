"this class contains the elements related to home page like villas and hotel search methods "
from appium.webdriver.common.appiumby import AppiumBy
class HomePage:
    def __init__(self,driver):
        self.driver=driver
        self.click_villa_locator=(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text(\"Villas &\nHomestays\")')

    def selectVilla(self):#will select the villa option
        self.driver.find_element(*self.click_villa_locator).click()


    def selectHotel(self):#select the hotel option
        pass
