from typing import List


class Sasdie:
    def setLogin(self, email: str) -> None:
        ...

    def setPasswd(self, password: str) -> None:
        ...

    def publierpage_html(self, webpage_content: str) -> bool:
        ...

    def lectureDonnéesCourante(self) -> str:
        ...

    def lireDonneesPollutionRPI(self) -> List[str]:
        ...

    def macle(self) -> str:
        ...
