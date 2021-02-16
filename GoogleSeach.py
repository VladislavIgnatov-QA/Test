from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GoogleSeacrhLocators:
    LOCATOR_GOOGLE_SEARCH_FIELD = (By.CSS_SELECTOR, 'input.gLFyf.gsfi')
    LOCATOR_GOOGLE_CLEAR_BUTTON = (By.XPATH, "//div[@aria-label='Очистить']")
    LOCATOR_GOOGLE_TITLES = (By.CSS_SELECTOR, 'cite.iUh30.Zu0yb.tjvcx')
    LOCATOR_GOOGLE_NAVIGATION_BAR = (By.ID, "hdtb-msb-vis")

class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        search_field.send_keys(Keys.ENTER)
        return search_field

    def check_for_cite(self):
        titles_fields = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_TITLES)
        titles = [x.text for x in titles_fields]
        return titles

    def clear_words(self):
        return self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_CLEAR_BUTTON,time=2).click()


    def click_on_the_search_button(self):
        return self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_SEARCH_FIELD,time=2).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(GoogleSeacrhLocators.LOCATOR_GOOGLE_NAVIGATION_BAR,time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu