import importlib
import re

from fake_sasdie import export_catch


FLOAT_PATTERN = re.compile(r"-?\d*?\.\d*")


def test_sprint7():
    importlib.import_module("src.sprint7.lectureCapteurFixe")

    assert len(export_catch) == 1
    assert isinstance(export := export_catch[0], str)

    assert export.count("\n") == 11
    csv = [line.split(";") for line in export.split("\n")]

    previous = None
    for line in csv[1::]:
        assert line[0] != previous
        previous = line[0]

        assert re.match(FLOAT_PATTERN, line[1])
