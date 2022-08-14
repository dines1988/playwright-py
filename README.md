# FOXTEL coding challenge
# How to run

1. Clone project and open in any IDE (VScode/PyCharm)
2. Run the below command from terminal
3. Create virtual environment
    python -m venv venv
4. Activate the virtual environment
    venv\Scripts\activate.bat
5. To download the dependencies in the virtual environment
    pip install -r requirements.txt
6. Run the following command to start the test
    python -m pytest --alluredir=allure-report --slowmo 3000 --screenshot on --capture=sys -s --browser firefox  ./tests
7. To view the allure test report
    allure serve allure-report

Refer to the below link for list of CLI arguments that can be passed
https://playwright.dev/python/docs/test-runners

Note: Refer to the below URL to make changes to the pytest_playwright.py in order to get attachements in the allure report
https://chowdera.com/2022/194/202207130516041664.html


## What is Playwright?

Playwright is a fairly new test automation framework from Microsoft.
It is open source, and it has bindings in TypeScript/JavaScript, Python, .NET, and Java.
Some of the nice features Playwright offers include:

* concise, readable calls
* easy out-of-the-box setup
* very fast execution times (compared to other browser automation tools)
* cross-browser and mobile emulation support
* automatic waiting
* screenshots and video capture
* built-in API calls

