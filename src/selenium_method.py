from enum import Enum


class SeleniumMethod(Enum):
    XPATH             = 'xpath'
    NAME              = 'name'
    LINK_TEXT         = 'link_text'
    PARTIAL_LINK_TEXT = 'partial_link_text'
    TAG_NAME          = 'tag_name'
    CLASS_NAME        = 'class_name'
    CSS_COLLECTOR     = 'css_collector'
