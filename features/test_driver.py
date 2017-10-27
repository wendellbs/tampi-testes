# encoding: utf-8

import time


class TestDriver(object):
    def __init__(self):
        self.driver = None

    def open(self):
        pass

    def quit(self):
        if self.driver:
            self.driver.quit()

    def screen_assert_equal(self, title):
        pass

    # def hide_keyboard(self):
    #     pass
    #
    def url_assert_equal(self, url):
        pass

    def find_element(self, component):
        if component.type == component.ID:
            return self.find_element_by_xpath('//*[@id="' + component.internal_id + '"]')
        elif component.type == component.TEXT:
            return self.find_element_by_xpath('//*[text()='+ component.internal_id +']')
        elif component.type == component.NAME:
            return self.find_element_by_name(component.internal_id)
        else:
            assert False, 'Invalid component type'

    def find_element_by_xpath(self, xpath):
        return self.__try_to_get_element(self.driver.find_element_by_xpath, xpath)

    def find_element_by_id(self, id):
        return self.__try_to_get_element(self.driver.find_element_by_id, id)

    def find_element_by_name(self, name):
        return self.__try_to_get_element(self.driver.find_element_by_name, name)

    def __try_to_get_element(self, func, parameter):
        for retries in xrange(0, 30):
            try:
                el = func(parameter)
                for retries in xrange(0, 10):
                    if el.is_displayed:
                        return el
                    time.sleep(1)
                return el
            except:
                time.sleep(1)

        return None
