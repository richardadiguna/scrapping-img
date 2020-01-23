from pathlib import Path
from enum import Enum


class CermatiScenario(Enum):
    CARD_CONTAINER_CLASS = 'nui-cards-listing'
    CARD_LIST_XPATH = "//div[@class='nui-card has-tag-layer']"
    MORE_BUTTON_XPATH = "//div[@id='load-more-credit-cards']"
    IMAGE_DETAIL_XPATH = ".//div[@class='details-image-holder']/a[@class='btn-track']"
    PRODUCT_INFO_BOX_XPATH = "//div[@class='nui-product-info-box']"

    @classmethod
    def card_container_class(cls):
        return cls.CARD_CONTAINER_CLASS.value

    @classmethod
    def card_list_xpath(cls):
        return cls.CARD_LIST_XPATH.value

    @classmethod
    def more_button_xpath(cls):
        return cls.MORE_BUTTON_XPATH.value

    @classmethod
    def image_detail_xpath(cls):
        return cls.IMAGE_DETAIL_XPATH.value

    @classmethod
    def product_info_box_xpath(cls):
        return cls.PRODUCT_INFO_BOX_XPATH.value