from enum import Enum


class ReturnFormat(int, Enum):
    HTML = 1
    PRETTY_JSON = 2
    PLAIN_TEXT = 3
    TREE = 4
    JSON = 5
    COLLAPSED_TREE = 6
