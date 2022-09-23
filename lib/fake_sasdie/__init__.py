from __future__ import annotations

import random

import time
from dataclasses import dataclass
from typing import Optional


export_catch = []


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


__all__ = (
    'DataUnit',
    'DataStream',
    'export_to_csv'
)
