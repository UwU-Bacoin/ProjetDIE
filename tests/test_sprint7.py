import re
from fake_sasdie import export_catch


FLOAT_PATTERN = re.compile(r'-?\d*?\.\d*')


def test_sprint7():
    import src.sprint7.lectureCapteurFixe

    assert isinstance(export_catch[0], str)
    export = export_catch[0]

    assert export.count('\n') == 11

    csv = [line.split(';') for line in export.split('\n')]

    previous = None
    for line in csv[1::]:
        assert line[0] != previous
        previous = line[0]

        assert re.match(FLOAT_PATTERN, line[1])
