import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

from config import config
from src.operation.scenario import CermatiScenario
from src.support.utils import url_2_filename, downloader
from src.support.utils import get_multiple_element, get_single_element


# Chrome option configuration
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# Selenium driver configuration
driver = webdriver.Chrome(options=chrome_options)
driver.set_page_load_timeout(30)
driver.get(config.INITIAL_URL_CERMATI)


def main():
    info_boxes = []
    images = []

    wait = WebDriverWait(driver, 5)

    first_element = get_single_element(
        driver, method='xpath', value=CermatiScenario.more_button_xpath())

    while True:
        try:
            time.sleep(5)
            first_element.click()
        except ElementNotInteractableException as e:
            break

    second_element = wait.until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, CermatiScenario.card_container_class())))

    third_element = get_multiple_element(
        second_element, method='xpath', value=CermatiScenario.card_list_xpath())

    for card in third_element:
        image_holder = get_single_element(
            card, method='xpath', value=CermatiScenario.image_detail_xpath())
        url = image_holder.get_attribute('href')
        info_boxes.append(url)

    for box in info_boxes:
        try:
            driver.get(box)
            container = get_single_element(
                driver, method='xpath', value=CermatiScenario.product_info_box_xpath())
            img = container.find_element_by_tag_name('img').get_attribute('src')
            images.append(img)
            time.sleep(5)
        except NoSuchElementException as e:
            print("This url is invalid : {0}".format(box))
            continue

    for url in images:
        print("image url: {0}".format(url))
        img = url_2_filename(url)
        downloader(url, os.path.join(config.DOWNLOAD_PATH_CERMATI, img))


if __name__ == '__main__':
    main()
    driver.quit()
