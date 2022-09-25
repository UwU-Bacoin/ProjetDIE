from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Optional

export_catch = []
is_initialized = False


def export_to_csv(content: str):
    """
    Export a string to a csv file.
    Meant for DataStream.écritureDuFichierCSV

    :param content: str
        the content to write within the csv.
        It might follow the regex:
    """
    export_catch.append(content)
    print('=>', content)


class DataStream:
    __counter = 0
    __previous: Optional[DataUnit] = None
    fake = True

    def read(self):
        """Equivalent of lectureDonnéesCourante."""
        if random.random() < 0.4 and self.__previous is not None:
            return self.__previous

        self.__counter += 1
        self.__previous = DataUnit(self.__counter, round(random.random(), 2))
        return self.__previous


@dataclass
class DataUnit:
    id: int
    pm25: float


class Sasdie:

    def __init__(self):
        self.publish_content = None

        self.connected = False
        self.key = 0

    def connect(self):
        self.connected = True
        return True

    def get_key(self):
        self.key = 1
        return 1

    def publish_webpage(self, page_content):
        self.publish_content = page_content


class API(Sasdie):

    def __init__(self, email, password):
        super().__init__()
        self.email = email
        self.password = password


def init():
    global is_initialized
    is_initialized = True


__all__ = (
    'DataUnit',
    'DataStream',
    'export_to_csv'
)
