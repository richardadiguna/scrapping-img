import os
import posixpath
import urllib.request
from urllib.parse import urlsplit, unquote


def url_2_filename(url):
    url_path = urlsplit(url).path
    base_name = posixpath.basename(unquote(url_path))
    if (os.path.basename(base_name) != base_name or
            unquote(posixpath.basename(url_path)) != base_name):
        raise ValueError("Reject '%2f' or 'dir%5Cbasename.ext' on Windows")
    return base_name


def downloader(url, fullpath):
    urllib.request.urlretrieve(url, fullpath)


def get_multiple_element(driver, method, value):
    if method == 'xpath':
        return driver.find_elements_by_xpath(value)
    elif method == 'name':
        return driver.find_elements_by_name(value)
    elif method == 'link_text':
        return driver.find_elements_by_link_text(value)
    elif method == 'partial_link_text':
        return driver.find_elements_by_partial_link_text(value)
    elif method == 'tag_name':
        return driver.find_elements_by_tag_name(value)
    elif method == 'class_name':
        return driver.find_elements_by_class_name(value)
    elif method == 'css_colector':
        return driver.find_elements_by_css_selector(value)
    else:
        raise ValueError('Unspecified method arguments')


def get_single_element(driver, method, value):
    if method == 'id':
        return driver.find_element_by_id(value)
    elif method == 'name':
        return driver.find_element_by_name(value)
    elif method == 'xpath':
        return driver.find_element_by_xpath(value)
    elif method == 'link_text':
        return driver.find_element_by_link_text(value)
    elif method == 'partial_link_text':
        return driver.find_element_by_partial_link_text(value)
    elif method == 'tag_name':
        return driver.find_element_by_tag_name(value)
    elif method == 'class_name':
        return driver.find_element_by_class_name(value)
    elif method == 'css_colector':
        return driver.find_element_by_css_selector(value)
    else:
        raise ValueError('Unspecified method arguments')