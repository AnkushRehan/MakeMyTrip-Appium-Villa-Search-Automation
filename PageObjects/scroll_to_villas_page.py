"this class contain method which find the villa during scroll"
from appium.webdriver.common.appiumby import AppiumBy
import time

class ScrollToVilla:
    def __init__(self,driver):
        self.driver=driver

    def find_villa(self,no_of_scroll,villaName,width,height):#identify the villa on villa search results screen
        for i in range(no_of_scroll):
            villa =self.driver.find_elements(AppiumBy.XPATH,f'//android.widget.TextView[@resource-id="tvHotelName" and @text="[icon]  {villaName}"]')  # here change the villah if not in the result list.
            if villa:#uper find_elements use kiya ha to jo ham villa ka name beje ge wo ager ek ya 2 huye to unki list resturn hogi and index 0 pr jo villa hoga matched us pr click ho jaye ga
                villa[0].click()
                print("Villa clicked!")
                break
            self.driver.execute_script("mobile: swipeGesture", {
                "left": int(width * 0.10),
                "top": int(height * 0.20),
                "width": int(width * 0.80),
                "height": int(height * 0.60),
                "direction": "up",
                "percent": 0.75,
                "speed": 1000
            })
            time.sleep(3)