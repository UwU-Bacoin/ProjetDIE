try:
    import sasdie

    class API(sasdie.Sasdie):

        def __init__(self, email, student_id):
            super().__init__()
            self.setLogin(email)
            self.setPasswd(student_id)

        get_key = sasdie.Sasdie.macle
        publish_webpage = sasdie.Sasdie.publierpage_html


    sasdie.API = API


except ImportError:
    import fake_sasdie as sasdie


import os

PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang='fr'>
<head>
  <title>Account Key</title>
</head>
<body>
  <h1>Account Key</h1><code><pre>{key}</pre></code>
  <hr/>
  <p>
    <em>
      "A computer is like air conditioning
      - it becomes useless when you open Windows"
    </em> - Linus Torvalds
  </p>
</body>
</html>
"""

sasdie.init()

# les identifiants sont stockés dans des variables d'environement

EMAIL = os.environ.get('EMAIL')
STUDENT_ID = os.environ.get('ID')


def main():
    c = sasdie.API(EMAIL, STUDENT_ID)

    if not c.connect():
        print("Couldn't connect to the api.")
        return

    if not (key := c.get_key()):
        print("Error while retrieving the key.")
        return

    c.publish_webpage(PAGE_TEMPLATE.format(key=key))


if __name__ == '__main__':
    main()
