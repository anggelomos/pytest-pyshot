

def get_element(func):
    def wrapper(self):
        locator = func(self)
        return self.driver.find_element(*locator)
    return wrapper


def get_elements(func):
    def wrapper(self):
        locator = func(self)
        return self.driver.find_elements(*locator)
    return wrapper
