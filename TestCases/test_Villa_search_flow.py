"""it contains the flow of villa search in make-my-trip app"""
import allure
#TODO: IMPORT ALL PAGE OBJECT and appium classes RELATED TO THE TEST CASE
import pytest
from PageObjects.welcome_page import WelcomePage
from PageObjects.home_page import HomePage
from PageObjects.search_villa_page import VillaSearch
from PageObjects.scroll_to_villas_page import ScrollToVilla
from PageObjects.villa_result_page import VillaResultPage
from Utilities.allow_and_deny_notification_utility import NOTIFICATION_WINDOW
from Utilities import dataFetcherExcel_utility #to fetch the data from excel file
from Utilities.get_screen_ratio_utility import get_screen_ratio
from Utilities import dragDown_popup_utility
import time
# TODO:use excel data fetcher to fetch the data from excel sheet
excelReader = dataFetcherExcel_utility  # it will fetch the data from excel sheet
data = excelReader.getData("D:/study/automation/PHASE 5/Appium - Mobile App Automation in Python/liveProject/Excel/locations.xlsx",
    "locations_sheet")

amritsar_villa="HolidayVilla Amritsar| Luxury Rooms & Suites"
delhi_villa="White Rose Near Delhi Airport"

#testcase which shows the flow to search the villa and validate the ER with AR in make-my-trip App"
@pytest.mark.parametrize("locations",data)
def testSearch_Villas(locations,setup):#here we pass the fixture in test
    driver=setup#assign driver return from fixture in driver variable
    #TODO:SKIP THE LOGIN SCREEN:
    skip_welcome_screen=WelcomePage(driver)#send driver to welcome page class
    skip_welcome_screen.SkipLogin()
    #TODO: DENY THE NOTIFICATION ON HOME SCREEN
    deny_notification=NOTIFICATION_WINDOW(driver)#pass driver
    deny_notification.deny_notification()#call denynotification method
    #TODO:SELECT VILLA FROM HOME PAGE
    select_villa_option=HomePage(driver)
    select_villa_option.selectVilla() #click on villa option
    #TODO:SEARCH  VILLA USING DATA FROM EXCEL:
    search_villa=VillaSearch(driver)
    search_villa.searchVilla(locations)#pass the villa locations as data set
    #TODO:ADD CHECKIN AND CHECK DATE WITH MONTH(SHORT AND IN CAPITAL) AND YEAR
    search_villa.checkIn(2,3,"DEC",2026)
    #TODO:OPEN GUEST ENTRY AND CLICK GUEST ENTRY BUTTON
    search_villa.guestEntry()
    #TODO:NOW get THE VILLA RESULTS:
    search_villa.getVillas()
    #TODO:USE LITTLE DROPDOWN UTILITY TO DROP THE POPUP DURING VILLA RESULTS SCREEN
    time.sleep(3)
    drag_popup=dragDown_popup_utility
    drag_popup.low_dragDown_popup(driver)
    time.sleep(3)
    #TODO: NOW USE IF ELSE SO THAT WE CAN SCROLL TO TARGET VILLA
    height,width=get_screen_ratio(driver)
    find_villa = ScrollToVilla(driver)#initilize the scrolltovilla class
    if locations=="Delhi":
        find_villa.find_villa(5,delhi_villa,width,height)
    elif locations=="Amritsar":
        find_villa.find_villa(5,amritsar_villa,width,height)
    #TODO:DRAG DOWN the popup USING HEAVY POPUP UTILITY
    time.sleep(3)
    drag_popup.heavy_dragDown_popup(driver)
    time.sleep(3)
    #TODO:FETCH THE TITLE OF HOTEL FROM RESULT VILLA PAGE:
    result=VillaResultPage(driver)
    villa_name=result.getVillaName()
    print(villa_name)
    #TODO:TAKE SCREENSHOT AND SAVED IN HTML REPORT -> ALLURE REPORT
    allure.attach(driver.get_screenshot_as_png(),#will take screenshot of passed data sets/testcases
                  name="villas",
                  attachment_type=allure.attachment_type.PNG)
    #TODO: ADD ASSERTION TO VALIDATE THE A-R WITH E-R
    if locations=="Delhi":
        expected_result=(f'[icon]  {delhi_villa}')
    elif locations=="Amritsar":
        expected_result=(f'[icon]  {amritsar_villa}')
    assert villa_name == expected_result,"not matched"
    print("matched with actual result")