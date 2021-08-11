from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser =='chrome':
        driver=webdriver.Chrome(executable_path='C:\Program Files\Driver\chromedriver.exe')
        print("Launching Chrome browser")
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path="C:\Program Files\Driver\geckodriver.exe")
        print("Launching firefox browser")
    else:
        driver = webdriver.Chrome(executable_path='C:\Program Files\Driver\iedriver.exe')
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

####py test html report#####

#it is hook for adding environtment info into HTML report
def pytest_configure(config):
    config._metadata['Project Name']='Sampleswebsite'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester Name'] = 'battun'

#it is hook for delete/modify environtment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)