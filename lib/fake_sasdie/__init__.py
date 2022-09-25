from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Optional

export_catch = []
is_initialized = False


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


class _Sasdie:
    connected = False
    published_content = None
    key = 0

    @classmethod
    def connect(cls):
        cls.connected = True
        return True

    @classmethod
    def get_key(cls):
        cls.key = 1
        return 1

    @classmethod
    def publish_webpage(cls, page_content):
        cls.published_content = page_content


class API(_Sasdie):
    email = None
    student_id = None

    def __init__(self, email, password):
        self._cls_set(email, password)

    @classmethod
    def _cls_set(cls, email, password):
        cls.email = email
        cls.student_id = password


def read_pollution_data():
    with open('src/sprint7/data_pm25.csv') as f:
        return [
            line.split(';') for line in f.read().split('\n')
        ]


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


def init():
    global is_initialized
    is_initialized = True


__all__ = (
    'DataUnit',
    'DataStream',
    'export_to_csv'
)
