import datetime
import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser == "edge":
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)

    elif browser == "firefox":
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")      ## this will get the browser value from cmd line

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")         ### this will return the browser value to the setup() method

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
