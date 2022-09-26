import os

try:
    import sasdie

    # Lorsque que l'on importe la version originale de sasdie,
    # on signale l'utilisation de celle-ci
    IS_REPLACEMENT = False

except ImportError:
    # Si "sasdie" n'est pas trouvé, on importe la version locale
    # https://github.com/UwU-Bacoin/ProjetDIE/tree/main/lib/fake_sasdie
    import fake_sasdie as sasdie

    IS_REPLACEMENT = True


if not IS_REPLACEMENT:
    # Si le module importé n'est pas la version locale de sasdie,
    # on applique des corrections sur le module afin de le rendre cohérent.

    # ces corrections permettent au programme de marcher
    # avec la version originale de Sasdie.

    from functools import partial

    # on renomme la méthode "lireDonneesPollutionRPI" en anglais
    # et l'on retire son appartenance à la classe Sasdie.
    sasdie.read_pollution_data = partial(
        sasdie.Sasdie.lireDonneesPollutionRPI, sasdie.Sasdie()
    )

    # On crée un wrapper autour de Sasdie pour rendre l'utilisation
    #  plus simple et intuitif (moins de méthodes)
    class API(sasdie.Sasdie):
        def __init__(self, email, student_id):
            super().__init__()
            self.setLogin(email)
            self.setPasswd(student_id)

        # on renomme la méthode "publierpage_html" en anglais
        publish_webpage = sasdie.Sasdie.publierpage_html

    # On inject l'objet API dans le module sasdie
    sasdie.API = API


PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang='fr'>
<head>
  <meta charset="UTF-8">
  <title>Account Key</title>
</head>
<body>
    <h1>Donnees RPI</h1>
    <table>
        <thead>
            {table_head}
        </thead>
        <tbody>
            {table_body}
        </tbody>
    </table>
</body>
</html>
"""


# On utilise les variables d'environement pour stocker les identifiants
EMAIL = os.environ.get("EMAIL")
STUDENT_ID = os.environ.get("STUDENT_ID")


def main():
    c = sasdie.API(EMAIL, STUDENT_ID)

    if not c.connect():
        print("Couldn't connect to the api.")
        return

    donnees = sasdie.read_pollution_data_rpi()

    if not donnees:
        print("Error while retrieving the data.")
        return

    line = donnees[0]
    thead = f"""
    <thead>
        <tr>
            <th>{line[0]}</th>
            <th>{line[1]}</th>
        </tr>
    </thead>
    """

    tbody = "\n".join(
        f"""
        <tr>
            <td>{i[0]}</td>
            <td>{i[1]}</td>
        </tr>
        """
        for i in donnees[1:]
    )

    c.publish_webpage(PAGE_TEMPLATE.format(table_head=thead, table_body=tbody))


if __name__ == "__main__":
    main()
