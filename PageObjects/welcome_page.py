'''this class skip the login screen  and directly reach to the main screen'''
from appium.webdriver.common.appiumby import AppiumBy
class WelcomePage:
    def __init__(self, driver):#pass the driver from testcase during this class initialization with obj
        self.driver=driver
        self.skip_button_locator=(AppiumBy.ID, "com.makemytrip:id/skip")

    def SkipLogin(self):#skip the login screen
        self.driver.find_element(*self.skip_button_locator).click()  # click to skip login



