from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time


class DownloadM:

    done = []
    robot_on = True

    def __init__(self, movie):
        self.movie = movie
        self.driverstart()

    def driverstart(self):
        chromedriver = "C:/Webdriver/chromedriver"
        download_path = "E:\Bur\Python\Web scraper\Milestone_Project\Milestone\Running_scrapy\Downloads"
        options = webdriver.ChromeOptions()
        preferences = {
            'download.default_directory': download_path,
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
        }
        options.add_experimental_option('prefs', preferences)
        self.driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
        if self.movie not in self.done:
            self.dwnld_start()
        else:
            print(self.movie, ' already downloaded')
            self.driver.quit()

    def dwnld_start(self):
        global in_download
        driver = self.driver
        driver.maximize_window()
        driver.get("https://yts.mx/browse-movies")
        assert "YTS" in driver.title

        no_redirect(driver, None)

        driver.implicitly_wait(3)
        searching = driver.find_element_by_xpath('//*[@id="main-search-fields"]/input')
        searching.clear()
        searching.send_keys(self.movie)
        searching.send_keys(Keys.RETURN)

        my_path = "/html/body/div[4]/div[4]/div/section/div/div/div/a"
        self.refresh_one(driver, my_path)

        # This condition ensures that the movie is there
        if self.robot_on:
            try:
                my_path = "//*[@id='movie-poster']/a"
                self.refresh_one(driver, my_path)

                my_path = "//*[@id='movie-content']/div[1]/div[3]/div/div[2]/div[1]/a[1]"
                self.refresh_one(driver, my_path)

            except ElementNotInteractableException:
                driver.refresh()
                print('Refresh - Element Not Interactable')
                driver.get(driver.current_url)

                my_path = "//*[@id='movie-poster']/a"
                self.refresh_one(driver, my_path)

                my_path = "//*[@id='movie-content']/div[1]/div[3]/div/div[2]/div[1]/a[1]"
                self.refresh_one(driver, my_path)

            self.done.append(self.movie)
            time.sleep(5)
            driver.quit()

        else:
            driver.quit()

    # This module refreshes the page
    def refresh_one(self, driver, my_path):
        try:
            getting_in = driver.find_element_by_xpath(my_path)
            no_redirect(driver, getting_in)
        except NoSuchElementException:
            driver.refresh()
            print('Refresh - No Such Element')
            driver.get(driver.current_url)

            # Here we are asserting whether the movie exists or not
            element = driver.find_element_by_class_name('browse-content')
            if element.text != '0 YIFY Movies found':
                getting_in = driver.find_element_by_xpath(my_path)
                no_redirect(driver, getting_in)
            else:
                print(f"I couldn't be found {self.movie}")
                self.robot_on = False

        return driver, self.robot_on


# This function gets rid of redirection
def no_redirect(driver, handler):
    if handler is None:
        redirect_off = ActionChains(driver)
        redirect_off.click().perform()
    else:
        driver.implicitly_wait(3)
        handler.click()
    try:
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except IndexError:
        print('IndexError: ' + driver.current_url)
    return driver
