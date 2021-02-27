# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


from selenium import  webdriver
#Give the path to the driver
driver = webdriver.Chrome(executable_path="chromedriver.exe")

#Give the url to the IDE
driver.get("https://www.amazon.fr/")

#Identify the search bar
search_bar = driver.find_element_by_id("twotabsearchtextbox")

#Put the desired keyword
search_bar.send_keys("AirPodsPro")

# Get the button
search_btn= driver.find_element_by_id("nav-search-submit-button")

#Use button and click
search_btn.click()

# Recover names
all_tittles = driver.find_element_by_class_name("a-link-normal a-text-normal")

#Browse the list
for title in all_tittles:
    print(title.text)