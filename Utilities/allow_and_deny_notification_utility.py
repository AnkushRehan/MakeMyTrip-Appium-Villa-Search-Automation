"this class contains methods related to notification window allow and deny button"
from appium.webdriver.common.appiumby import AppiumBy
class NOTIFICATION_WINDOW:
    def __init__(self, driver):
        self.driver = driver


    def allow_notification(self):
        self.driver.find_element(AppiumBy.ID,"com.android.permissioncontroller:id/permission_allow_button").click()

    def deny_notification(self):
        self.driver.find_element(AppiumBy.ID,"com.android.permissioncontroller:id/permission_deny_button").click()
