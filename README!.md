# MakeMyTrip Android App – Villa Search Automation

**Created by:** Ankush  
**Project Type:** Independent QA Automation Practice Project  
**Application Under Test:** Official MakeMyTrip Android Application  
**Automated Functionality:** Villa Search Flow  
**Automation Stack:** Python, Appium, Pytest and Page Object Model (POM)

---

## 1. Project Overview

This project demonstrates automation practice performed on the official MakeMyTrip Android application. The scope of the project is the **Villa Search flow**.

The automation starts from launching the application and handling the welcome and notification screens. It then selects the Villa option, reads search locations from an Excel workbook, enters the location, selects check-in and check-out dates, enters guest details, searches for villas, scrolls through the results and validates the displayed villa name against the expected result.

The project follows the **Page Object Model (POM)** design pattern. Reusable actions and supporting functionality are kept in utility modules, while Pytest is used to execute and parameterize the test.

> This is an independent QA automation practice project. MakeMyTrip is the application under test; this project does not claim to be developed, owned or officially endorsed by MakeMyTrip.

## 2. Tools and Technologies

| Tool / Technology | Purpose |
|---|---|
| Python | Programming language used to write automation scripts |
| PyCharm IDE | Writing, maintaining and running the Python project |
| Node.js and npm | Runtime and package manager used to install and run Appium |
| Appium Server | Receives automation commands and communicates with the Android device |
| Appium Inspector | Inspects application screens and identifies element locators |
| Appium Python Client | Connects Python test code to the Appium Server |
| UiAutomator2 | Appium automation driver for Android |
| Android Debug Bridge (ADB) | Communicates with Android devices and retrieves app/device information |
| Pytest | Test execution, fixtures and parameterization |
| Microsoft Excel | Stores location-based test data |
| openpyxl | Reads test data from Excel workbooks |
| Allure | Creates detailed test execution reports and supports attachments |
| pytest-html | Optional plugin for generating a standalone HTML test report |
| Python `time` module | Adds delays where required in the test flow |
| Python `logging` module | Supports execution logging |

## 3. Python Packages and Modules

Install the third-party packages used by the project:

```bash
pip install Appium-Python-Client pytest selenium openpyxl allure-pytest pytest-html
```

The project uses:

- `appium`: Appium WebDriver connection and Android automation.
- `AppiumBy`: Locates Android elements using strategies such as ID, XPath, accessibility ID and UiAutomator.
- `pytest`: Test functions, fixtures and `@pytest.mark.parametrize`.
- `openpyxl`: Opens Excel workbooks and reads worksheet data.
- `allure-pytest`: Integrates Allure with Pytest and supports screenshot attachments.
- `pytest-html`: Generates an HTML report from a Pytest run.
- `time`: Provides sleep/delay functionality.
- `logging`: Python's built-in logging functionality.
- `selenium`: WebDriver functionality used through the Appium/Selenium client libraries.

`time` and `logging` are part of Python's standard library, so they do not need to be installed separately.

## 4. Project Structure

```text
MakeMyTrip-Appium-Automation/
│
├── configurationFile/
│
├── Excel/
│   └── locations.xlsx
│
├── Logs/
│
├── PageObjects/
│   ├── __init__.py
│   ├── home_page.py
│   ├── scroll_to_villas_page.py
│   ├── search_villa_page.py
│   ├── villa_result_page.py
│   └── welcome_page.py
│
├── TestCases/
│   ├── __init__.py
│   ├── conftest.py
│   ├── extra_for_practice.py
│   └── test_Villa_search_flow.py
│
├── Utilities/
│   ├── __init__.py
│   ├── allow_and_deny_notification_utility.py
│   ├── configFile_Reader_utility.py
│   ├── dataFetcherExcel_utility.py
│   ├── dragDown_popup_utility.py
│   ├── generatingLogs_utility.py
│   └── get_screen_ratio_utility.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── pytest.ini
```

### Folder and file descriptions

#### `PageObjects/`

Contains page classes that represent application screens and their actions.

- `welcome_page.py`: Handles the welcome/login screen, such as skipping the welcome screen.
- `home_page.py`: Handles selecting the Villa option from the home screen.
- `search_villa_page.py`: Handles villa location search, date selection, guest selection and the search action.
- `scroll_to_villas_page.py`: Contains scrolling functionality used to locate the target villa in the results.
- `villa_result_page.py`: Retrieves the villa name displayed on the results screen.

#### `TestCases/`

Contains Pytest test scripts and shared fixtures.

- `conftest.py`: Creates the Appium driver, configures the implicit wait, yields the driver to tests and performs teardown. It can also contain Pytest hooks, such as attaching a screenshot when a test fails.
- `test_Villa_search_flow.py`: Contains the end-to-end Villa Search test flow and assertion.
- `extra_for_practice.py`: Contains additional practice code, if retained in the repository.

#### `Utilities/`

Contains reusable helper methods.

- `allow_and_deny_notification_utility.py`: Handles Android notification permission Allow and Deny actions.
- `configFile_Reader_utility.py`: Reads values from the project configuration file.
- `dataFetcherExcel_utility.py`: Reads test data from an Excel worksheet using `openpyxl`.
- `dragDown_popup_utility.py`: Contains popup drag/swipe helper methods.
- `generatingLogs_utility.py`: Supports execution logging.
- `get_screen_ratio_utility.py`: Gets the device screen width and height for swipe calculations.

#### `Excel/`

Contains the Excel workbook used to store location test data.

#### `Logs/`

Stores log output generated during test execution.

#### `configurationFile/`

Contains configuration files used by the project.

## 5. Automation Flow

The Villa Search test follows this sequence:

1. Start the MakeMyTrip Android application through the Appium session.
2. Skip the welcome/login screen.
3. Handle the Android notification permission popup.
4. Select the Villa option from the home screen.
5. Fetch location data from the Excel workbook.
6. Enter the location and select an autocomplete suggestion.
7. Select check-in and check-out dates.
8. Enter guest details.
9. Start the Villa search.
10. Handle the popup displayed on the results screen.
11. Scroll through the results to locate the target villa.
12. Fetch the displayed villa name.
13. Compare the actual villa name with the expected villa name using a Pytest assertion.

## 6. Excel Data-Driven Testing

The project uses Microsoft Excel to maintain the locations used by the Villa Search test.

**Workbook:** `Excel/locations.xlsx`  
**Worksheet:** `locations_sheet`

Example locations used in this project:

| Search location | Expected villa name |
|---|---|
| Delhi | White Rose Near Delhi Airport |
| Amritsar | HolidayVilla Amritsar \| Luxury Rooms & Suites |

The Excel reader uses `openpyxl` to open the workbook, read worksheet cells and return the data to the test script. Pytest's `@pytest.mark.parametrize` decorator then runs the test once for each supplied location.

### Excel reader logic used in the project

```python
import openpyxl

def getData(path, sheet_name):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheet_name]

    max_rows = sheet.max_row
    max_cols = sheet.max_column

    alldata = []

    for rows in range(2, max_rows + 1):
        for cols in range(1, max_cols + 1):
            data = sheet.cell(row=rows, column=cols).value
            alldata.append(data)

    return alldata
```

This implementation starts reading from row 2, assuming row 1 contains column headings. It appends cell values row by row to a list.

## 7. Configuration When Running on Another Computer

When cloning and running this project on another system, update the device details, application information, Excel path, test data and expected villa names according to that environment.

### A. Connect and identify the Android device

Enable Developer Options and USB debugging on the Android device. Connect it to the computer and run:

```bash
adb devices
```

If more than one device is connected, note the required device serial number.

### B. Find the app package and current app activity

To find the currently focused app package and activity:

```bash
adb shell dumpsys window | findstr mCurrentFocus
```

### C. Find the app's launcher activity

Use the following command, replacing the placeholders with the actual device serial number and application package:

```bash
adb -s <device_serial_number> shell cmd package resolve-activity --brief -a android.intent.action.MAIN -c android.intent.category.LAUNCHER <app_package>
```

For example, replace:

- `<device_serial_number>` with the serial shown by `adb devices`.
- `<app_package>` with the package name of the installed application.

Use the package and activity values obtained for the target device/application in the desired capabilities in `TestCases/conftest.py`.

### D. Update device capabilities

Review the desired capabilities in `conftest.py`, including:

- `platformName`
- `deviceName`
- `automationName`
- `appPackage`
- `appActivity`

The device name, package and activity may differ between systems and devices.

### E. Update the Excel file path

The test script must point to the workbook location on the computer where the project is running.

For example:

```python
data = excelReader.getData(
    "D:/Your_Project/MakeMyTrip-Appium-Automation/Excel/locations.xlsx",
    "locations_sheet"
)
```

Update the path and worksheet name if they are different in your copy of the project.

### F. Change locations and expected villa names

Delhi and Amritsar are example locations used in this project. You can replace them with any locations you want to test, subject to the villas available in the application.

When changing the locations:

1. Update the location values in `Excel/locations.xlsx`.
2. Search the application and identify a villa that should be present for each location.
3. Update the expected villa names in the test script.
4. Update the location-to-expected-villa mapping used by the assertion.
5. Run the test and confirm that the actual result matches the expected value.

Example assertion mapping:

```python
if locations == "Delhi":
    expected_result = delhi_villa

elif locations == "Amritsar":
    expected_result = amritsar_villa

else:
    pytest.fail(f"No expected result configured for {locations}")

assert villa_name == expected_result, "Villa name not matched"
```

If you add another location, add its expected villa name and corresponding condition. The expected villa name must match the result displayed by the application. Search results can change, so verify the target villa before execution.

### G. Verify element locators

Application UI elements and locators may change with application updates, Android versions or device layouts. Use Appium Inspector to inspect the current screen and update locators when necessary.

## 8. Setup and Installation

### Prerequisites

Install and configure:

1. Python
2. Node.js and npm
3. Appium Server
4. Appium UiAutomator2 driver
5. Appium Inspector
6. PyCharm IDE (or another Python IDE)
7. Android SDK and ADB
8. Java/JDK as required by the Android SDK and UiAutomator2 setup

### Step 1: Open the project directory in the terminal

Change directory to the folder where the project is cloned. For example:

```bash
cd /d "D:\Your_Project\MakeMyTrip-Appium-Automation"
```

Replace the example path with your actual project path.

### Step 2: Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 3: Install Appium Server

```bash
npm install -g appium
```

### Step 4: Install the UiAutomator2 driver

```bash
appium driver install uiautomator2
```

### Step 5: Start Appium Server

```bash
appium
```

Keep the Appium Server running while executing the tests.

### Step 6: Verify the Android device

Open another terminal and run:

```bash
adb devices
```

Make sure the device is listed and authorized.

## 9. Test Execution Commands

Run these commands from the project root directory unless the command specifies another path.

### A. Run the Villa Search test with Pytest

```bash
python -m pytest TestCases/test_Villa_search_flow.py -s -v
```

- `python -m pytest`: Runs Pytest using the selected Python interpreter.
- `-s`: Displays print output in the terminal.
- `-v`: Displays verbose test execution details.

### B. Generate an Allure report

First, execute the test and store Allure result files:

```bash
python -m pytest TestCases/test_Villa_search_flow.py -s --alluredir=TestCases/allure-report/allure_raw_data
```

Generate the HTML report:

```bash
allure generate TestCases/allure-report/allure_raw_data -o TestCases/allure-report/my_allure_report --clean
```

Open the generated report:

```bash
allure open TestCases/allure-report/my_allure_report
```

Alternatively, use `allure serve` to generate and open a report from the results directory:

```bash
allure serve TestCases/allure-report/allure_raw_data
```

Allure Commandline and a compatible Java installation must be configured separately. The `allure-pytest` Python package alone does not install the Allure Commandline tool.

### C. Generate a simple HTML report using pytest-html

If you do not want to generate an Allure report, you can generate a standard Pytest HTML report instead:

```bash
python -m pytest TestCases/test_Villa_search_flow.py -s -v --html=TestCases/my_report.html --self-contained-html
```

This creates an HTML report at `TestCases/my_report.html`.

The `pytest-html` package must be installed for this command.

## 10. Attach a Screenshot for a Failed Test in Allure

The following Pytest hook can be placed in `TestCases/conftest.py`. It attaches a screenshot to the Allure result when the test call phase fails.

```python
import pytest
import allure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup")  # Use the actual fixture name here

        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failed_Test_Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
```

**Important:** The fixture lookup name (`"setup"` in this example) must match the actual fixture name used by the test. The driver session must still be active when the screenshot is captured. The hook attaches screenshots to Allure results; it does not itself create the final HTML report.

## 11. Important Notes

- Start the Appium Server before running the test.
- Connect and authorize the Android device.
- Update device capabilities, app package and app activity for the target environment.
- Update the Excel workbook path when running from another computer.
- Update the Excel locations and expected villa names when changing test data.
- Recheck element locators with Appium Inspector if the app UI changes.
- Allure and pytest-html are alternative reporting options; install the relevant packages and tools before using their commands.
- Generated reports and temporary execution files can be recreated and generally do not need to be committed to Git.

## 12. Project Objective

The objective of this project is to gain practical experience in Android mobile application automation using Python and Appium.

The project demonstrates:

- Page Object Model (POM)
- Pytest test execution and fixtures
- Excel-based Data-Driven Testing
- Reusable utility methods
- Android element inspection using Appium Inspector
- Appium Server and UiAutomator2 integration
- Actual-versus-expected result validation using assertions
- Logging
- Allure reporting and failed-test screenshot attachments
- Optional Pytest HTML reporting

---

**Author:** Ankush  
**Application Under Test:** MakeMyTrip Android App  
**Automated Feature:** Villa Search  
**Project Category:** QA Automation Practice
