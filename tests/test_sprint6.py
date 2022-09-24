import importlib
import builtins


def test_add(monkeypatch):
    catcher = []

    monkeypatch.setattr(builtins, 'print', lambda x: catcher.append(x))
    importlib.import_module('src.sprint6.add')

    assert catcher[0] == 999999
