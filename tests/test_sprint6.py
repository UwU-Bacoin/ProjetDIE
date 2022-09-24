import os


def test_add(monkeypatch):
    catcher = []

    import builtins
    monkeypatch.setattr(builtins, 'print', lambda x: catcher.append(x))

    import src.sprint6.add

    assert catcher[0] == 999999
