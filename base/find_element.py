from readini import readini
class FindElement(object):
    def __init__(self,driver):
        self.driver = driver
    def get_element(self,key):
        read = readini()
        data = read.get_value(key)
        by = data.split(">")[0]
        value = data.split(">")[1]
        try:
            if by == "id":
                element=self.driver.find_element_by_id(value)
            elif by == "name":
                element=self.driver.find_element_by_name(value)
            elif by == "css":
                element=self.driver.find_element_by_css_selector(value)
            elif by == "class":
                element=self.driver.find_element_by_class_name(value)
            elif by =="link":
             element = self.driver.find_element_by_link_text(value)
            else:
                element=self.driver.find_element_by_xpath(value)
            return element
        except:
            return None



