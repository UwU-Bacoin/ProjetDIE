"""Replacement lib for sasdie meant to be used for local development and unit-testing."""
from __future__ import annotations

import os
import random
from dataclasses import dataclass
from functools import partial
from typing import Optional, List

import folium as folium

export_catch = []
is_initialized = False  # used for sasdie.init() tests
IS_REPLACEMENT = True


class DataStream:
    __counter = 0
    __previous: Optional[DataUnit] = None
    fake = True  # used to ensure this is the random replacement of sasdie DataStream.

    def read(self) -> DataUnit:
        """
        Return a random float value expressed as a data unit.
        Will sometimes return the value generated in the previous call.
        """
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
    """Represent the core features of the sasdie class."""
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
    def publish_webpage(cls, page_content, start_server=True):
        """Produce a minimal httpserver to display the page content given."""
        cls.published_content = page_content

        if not start_server:
            return

        _start_web_preview(page_content)


class API(_Sasdie):
    email = None
    student_id = None

    def __init__(self, email, password):
        self._cls_set(email, password)

    @classmethod
    def _cls_set(cls, email, password):
        """Ensure the email and password to be set as class attributes."""
        cls.email = email
        cls.student_id = password


def read_csv(partial_path: str, trim=False) -> List[List[str]]:
    """
    Read from a csv file without parse the data types.

    :param partial_path: str
        A partial relative path that may be prepended internally.

    :param trim: bool
        Whether to trim the given path to solve relative path issues.
    """
    if trim:
        path = os.getcwd().split('/')

        if 'src' in path:
            path = path[:path.index('src')]

        base = '/'.join(path) + '/'
    else:
        base = ''

    with open(f'{base}{partial_path}') as f:
        return [
            line.split(';') for line in f.read().split('\n')
        ]


# Providing custom read function for sasdie feature equivalence
read_gps_coords = partial(read_csv, 'tmp_territoires.csv')
read_pollution_data_rpi = partial(read_csv, '/src/sprint7/data_pm25.csv', trim=True)
read_pollution_data = read_csv


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


def _start_web_preview(homepage: str):
    """
    Start a minimal read-only httpserver to see the given html string.
    Will run until KeyInterrupt.

    :param homepage: str
        What to respond upon request.

    """
    if os.environ.get('SASDIE_TEST', 'True'):
        return

    from http.server import BaseHTTPRequestHandler, HTTPServer

    class Server(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(bytes(homepage, 'utf8'))

    web_server = HTTPServer(('localhost', 8080), Server)
    print("Server started http://localhost:8080")

    try:
        web_server.serve_forever()

    except KeyboardInterrupt:
        web_server.server_close()


class Map(folium.Map):
    """
    Provides a Map object to replace the poorly
    implemented sasdie.Sasdie.macarte system.
    """

    def __init__(self):
        super().__init__(location=(48.116622, -1.638717), zoom_start=13)

    def add_circle(self, longitude, latitude, diameter, label):
        folium.Circle(
            location=(latitude, longitude),
            popup=label,
            fill_color='#8aadf4',
            radius=diameter,
            weight=2,
            color="#000"
        ).add_to(self)

    def add_marker(self, longitude, latitude, label):
        folium.Marker(
            location=(latitude, longitude),
            fill_color='#8aadf4',
            popup=label
        ).add_to(self)

    def render_html(self):
        return self._repr_html_()


__all__ = (
    'API',
    'DataUnit',
    'DataStream',
    'export_to_csv',
    'read_pollution_data',
    'Map',
    'IS_REPLACEMENT'
)
