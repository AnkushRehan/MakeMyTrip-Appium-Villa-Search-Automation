'''is file me jo bhi code dale ge ya jo bhi function banaye ge unhe call ni krna prta , ye automatically run hoti ha file
thats why ham fixture is me bhi define kr skte ha taki sb testcase ko access ho '''
import allure
import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver


@pytest.hookimpl(hookwrapper=True) #take screen shot if the testcase falls in failure
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup") #add fixture name here

        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failed_Test_Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

#TODO: A FIXTURE FOR makemytrip app
@pytest.fixture(scope="function")
def setup():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'xiaomi-pad-6',
        'automationName':'uiautomator2',
        'appPackage': 'com.makemytrip',#get it from cmd prompt
        'appActivity': 'com.mmt.travel.app.home.ui.SplashActivitySale'#get it from cmd prompt
    }
    capabilities_options=UiAutomator2Options().load_capabilities(desired_caps)
    driver=webdriver.Remote("http://127.0.0.1:4723",options=capabilities_options)
    driver.implicitly_wait(10)
    yield driver#return the driver to pytest
    driver.quit()

