"this class contain method fetch retrun the villa name"
from appium.webdriver.common.appiumby import AppiumBy

class VillaResultPage:
    def __init__(self,driver):
        self.driver = driver

    def getVillaName(self):#return the villa name on villa result page
        result = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="tv_title"]').text
        return result