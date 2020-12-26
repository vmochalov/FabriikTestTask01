from selenium import webdriver
import time

FINISH_VALUE = 30


class FabriikTestTask01:

    def setup_driver(self):
        driver = webdriver.Chrome(r"C:\seleniumwebdrivers\chromedriver.exe")
        driver.maximize_window()
        driver.get('https://www.igame.com/eye-test/')
        return driver

    def take_screenshot(self, webdriver, path):
        webdriver.get_screenshot_as_file(path)

    def win_the_game(self, webdriver, finish_score):
        for score in range(finish_score):
            diff_square = webdriver.find_element_by_class_name('thechosenone')
            diff_square.click()

        time.sleep(15)

        self.take_screenshot(webdriver, "Result.png")

    def endless_game(self, webdriver):
        result = webdriver.find_element_by_id('resultdisplay')
        while not result.is_displayed():
            diff_square = webdriver.find_element_by_class_name('thechosenone')
            diff_square.click()
            result = webdriver.find_element_by_id('resultdisplay')

        time.sleep(15)

        self.take_screenshot(webdriver, "Result.png")



if __name__ == "__main__":

    test = FabriikTestTask01()
    driver = test.setup_driver()
    test.win_the_game(driver, FINISH_VALUE)
    # test.endless_game(driver)
    driver.close()
