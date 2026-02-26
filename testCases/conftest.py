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
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser",
                     default="chrome",help="browser to use : chrome or edge or gecko")
                                          ## this will get the browser value from cmd line

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")         ### this will return the browser value to the setup() method

########### pytest HTML Report ################

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"

# Modify environment metadata (pytest-html hook)
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):

    metadata["Project Name"] = "TutorialsNinja_dummy_project"
    metadata["Module Name"] = "CustRegistration"
    metadata["Tester"] = "Kiran"

    # Remove unwanted fields
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
