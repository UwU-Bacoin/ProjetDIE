from dataclasses import dataclass
from pprint import pprint
from typing import List

import requests


STUDENT_ID = 23111447

URL_BASE = (
    f"http://depot-l1miee.irisa.fr/informations/"
    f"{STUDENT_ID}_sasdie.json?v=1664154515426"
)


@dataclass
class File:
    name: str
    sprint: str
    validation: str

    def __str__(self):
        return '| ' + ' | '.join(
            (self.name.ljust(25), self.sprint.ljust(10), self.validation.ljust(16))
        ) + '|'


def generate_table(files: List[File]) -> str:
    return (
        '| Fichiers                  | Sprint     | Statut          |\n'
        + '| :------------------------ | :--------- | :-------------- |\n'
        + '\n'.join(map(str, files))
    )


def write_to_md(files: List[File]):
    with (
        open('docs/BASE.md') as base,
        open('docs/README.md', 'w') as out
    ):
        base_content = base.read()
        out.write(base_content.format(
            table=generate_table(files)
        ))


def main():
    response = requests.get(URL_BASE)

    if not response.ok:
        return

    payload = response.json()
    files = []

    for filename, file_data in payload.get('fichiers').items():
        if filename == '--':
            continue

        sprint = file_data.get('sprint')
        status = file_data.get('statut')

        files.append(File(filename, sprint, status))

    write_to_md(files)


if __name__ == '__main__':
    main()
