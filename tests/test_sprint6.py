import re
import importlib
import builtins


def test_add(monkeypatch):
    catcher = []

    monkeypatch.setattr(builtins, 'print', lambda x: catcher.append(x))
    importlib.import_module('src.sprint6.add')

    assert catcher[0] == 999999


def test_api(monkeypatch):
    monkeypatch.setenv('EMAIL', 'email_test')
    monkeypatch.setenv('STUDENT_ID', '42')

    api = importlib.import_module('src.sprint6.API')

    assert api.sasdie.is_initialized

    api.main()
    s = api.sasdie.API

    assert s.email == 'email_test'
    assert s.student_id == '42'

    assert s.connected
    assert s.key != 0
    assert re.search(r'<pre>(\d+)</pre>', s.published_content)[1] == '1'
