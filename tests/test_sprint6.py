import re
import importlib
import builtins


def test_add(monkeypatch):
    catcher = []

    monkeypatch.setattr(builtins, "print", lambda x: catcher.append(x))
    importlib.import_module("src.sprint6.add")

    assert catcher[0] == 999999


def test_api(monkeypatch):
    monkeypatch.setenv("EMAIL", "email_test")
    monkeypatch.setenv("STUDENT_ID", "42")
    monkeypatch.setenv("SASDIE_TEST", "True")

    api = importlib.import_module("src.sprint6.API")

    assert api.sasdie.is_initialized

    api.main()
    s = api.sasdie.API

    assert s.email == "email_test"
    assert s.student_id == "42"

    assert s.connected
    assert s.key != 0
    assert re.search(r"<pre>(\d+)</pre>", s.published_content)[1] == "1"


def test_boucle(monkeypatch):
    catcher = []

    monkeypatch.setattr(
        builtins, "print", lambda *x: catcher.append(" ".join(map(str, x)))
    )

    importlib.import_module("src.sprint6.boucle")

    assert "\n".join(catcher) == (
        "3 impair\n4 pair\n5 impair\n6 pair\n7 impair\n8 pair\n9 impair\n"
        "10 pair\n11 impair\n12 pair\n13 impair\n14 pair\n15 impair\n16 pair\n"
        "17 impair\n18 pair\n19 impair\n20 pair\n21 impair\n22 pair\n23 impair\n"
        "24 pair\n25 impair"
    )


def test_concat(monkeypatch):
    catcher = []
    monkeypatch.setattr(
        builtins, "print", lambda *x: catcher.append(" ".join(map(str, x)))
    )

    importlib.import_module("src.sprint6.hello")

    assert catcher == ["hello world!"]


def test_liste():
    module = importlib.import_module("src.sprint6.liste")

    assert module.my_strings == [
        "je ne extension de chaîne ",
        "sais extension de chaîne ",
        "pas extension de chaîne ",
        "quoi extension de chaîne ",
        "mettre... extension de chaîne ",
    ]
