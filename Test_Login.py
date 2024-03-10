import pytest
from Data import data
from Locators import locator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class TestLogin:
    @pytest.fixture()
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)
        yield
        self.driver.quit()

    def test_Login(self, boot):
        try:
            self.driver.get(data.WebData().url)
            self.driver.maximize_window()
            self.driver.find_element(by=By.XPATH, value=locator.WebLocators().expandLocator).click()
            self.driver.find_element(by=By.ID, value=locator.WebLocators().nameLocator).send_keys(data.WebData().name)
            self.driver.find_element(by=By.ID, value=locator.WebLocators().birthFromDateLocator).send_keys(data.WebData().birthFromDate)
            self.driver.find_element(by=By.XPATH, value=locator.WebLocators().seeResultsLocator).click()

            '''
                self.driver.find_element(by=By.XPATH, value=locator.WebLocators().birthToDateLocator).send_keys(data.WebData().birthToDate)
                self.driver.find_element(by=By.XPATH, value=locator.WebLocators().birthdayLocator).send_keys(data.WebData().birthday)
                self.driver.find_element(by=By.XPATH, value=locator.WebLocators().awardsLocator).click()
                self.driver.find_element(by=By.XPATH, value=locator.WebLocators().pageTopicLocator).click()
                self.driver.find_element(by=By.XPATH, value=locator.WebLocators().seeResultsLocator).click()
                self.driver.find_element(by=By.XPATH, value=locator.WebLocators().selectDropdownLocator).click()
                self.driver.find_element(by=By.XPATH, value=locator.WebLocators().chooseValueLocator).click()
                self.driver.find_element(by=By.XPATH, value=locator.WebLocators().subTopicLocator).send_keys(data.WebData().subTopic)
                self.driver.find_element(by=By.XPATH, value=locator.WebLocators().deathFromDateLocator).send_keys(data.WebData().deathFromDate)
                self.driver.find_element(by=By.XPATH, value=locator.WebLocators().deathToDateLocator).send_keys(data.WebData().deathToDate)
                self.driver.find_element(by=By.XPATH, value=locator.WebLocators().genderLocator).click()
                self.driver.find_element(by=By.XPATH, value=locator.WebLocators().creditsLocator).send_keys(data.WebData().credits)
                self.driver.find_element(by=By.XPATH, value=locator.WebLocators().adultLocator).click()
                '''

            if self.driver.current_url == data.WebData().dashboardUrl:
                print("Successfully LoggedIn")

        except NoSuchElementException as e:
            print("Error!")






