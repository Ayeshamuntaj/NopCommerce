import os.path
from datetime import datetime

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture()
def setup(browser):
    if browser =='edge':
        driver=webdriver.Edge()
    else:
        driver=webdriver.Chrome()
    return driver
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#hooks to generate html reports
def pytest_configure(config):
    config.metadata["projectname"] = "nopcommerce"
    config.metadata["Tester"] = "Ayesha"


#remove info
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Python",None)
    metadata.pop("Platform",None)
    metadata['Tester'] = "Ayesha"
    metadata["projectname"] = "nopcommerce"

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
 config.option.htmlpath=os.path.abspath(os.curdir)+"//reports//"+ datetime.now().strftime("%m-%d-%Y-%H-%M-%S")+".html"