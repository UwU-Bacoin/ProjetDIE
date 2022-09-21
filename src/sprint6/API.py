import sasdie
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

# les identifiants sont stocké dans des variables d'environement

EMAIL = os.environ.get('EMAIL')
STUDENT_ID = os.environ.get('ID')


def main():
    c = sasdie.Sasdie()

    c.setLogin(EMAIL)
    c.setPasswd(STUDENT_ID)

    state = c.connect()
    if not state:
        return

    key = c.macle()
    c.publierpage_html(PAGE_TEMPLATE.format(key=key))


if __name__ == '__main__':
    main()
