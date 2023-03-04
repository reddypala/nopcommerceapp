import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def setup(request,browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.maximize_window()
    return driver

def pytest_addoption(parser):    # This will get the value from CLI/hook
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):        #This will return browser value to the setup method
    return request.config.getoption("--browser")

############### pytest html reports ##################

#It is a hook for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Appala Reddy Pala'

#It is hook for delete/Modify environment info to html report

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
