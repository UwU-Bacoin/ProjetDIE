import os

try:
    import sasdie

    from functools import partial


    class API(sasdie.Sasdie):

        def __init__(self, email, student_id):
            super().__init__()
            self.setLogin(email)
            self.setPasswd(student_id)

        publish_webpage = sasdie.Sasdie.publierpage_html
        read_pollution_data = sasdie.Sasdie.lireDonneesPollutionRPI


    sasdie.API = API

except ImportError:
    import fake_sasdie as sasdie

# ----
PAGE_HEADER = """
<!DOCTYPE html>
<html lang='fr'>
<head>
  <title>Account Key</title>
</head>
<body>
    <h1>Donnees RPI</h1>
    <table>
"""

PAGE_FOOTER = """
    </tbody>
    </table>
</body>
</html>
"""

EMAIL = os.environ.get('EMAIL')
STUDENT_ID = os.environ.get('STUDENT_ID')


def main():
    global PAGE_HEADER
    c = sasdie.API('lucas.videcoq@etudiant.univ-rennes1.fr', '23111447')

    if not c.connect():
        print("Couldn't connect to the api.")
        return

    donnees = sasdie.read_pollution_data()

    if not donnees:
        print("Error while retrieving the data.")
        return

    line = donnees[0]
    PAGE_HEADER += f"""
    <thead>
        <tr>
            <th>{line[0]}</th>
            <th>{line[1]}</th>
        </tr>
    </thead>
    <tbody>
    """

    for i in donnees[1:]:
        PAGE_HEADER += f"""
        <tr>
            <td>{i[0]}</td>
            <td>{i[1]}</td>
        </tr>
        """

    PAGE_HEADER += PAGE_FOOTER

    c.publish_webpage(PAGE_HEADER)
    # print(c.published_content)


if __name__ == '__main__':
    main()
