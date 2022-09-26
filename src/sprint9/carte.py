import os

try:
    import sasdie
    # Lorsque que l'on importe la version originale de sasdie,
    # on signale l'utilisation de celle-ci
    IS_REPLACEMENT = False

except ImportError:
    import fake_sasdie as sasdie
    # Si "sasdie" n'est pas trouvé, on importe la version locale
    # https://github.com/UwU-Bacoin/ProjetDIE/tree/main/lib/fake_sasdie
    IS_REPLACEMENT = True

if not IS_REPLACEMENT:
    # Si le module importé n'est pas la version locale de sasdie,
    # on applique des corrections sur le module afin de le rendre cohérent.

    # ces corrections permettent au programme de marcher
    # avec la version originale de Sasdie.

    # On crée un wrapper autour de Sasdie pour rendre l'utilisation
    #  plus simple et intuitif (moins de méthodes)
    class API(sasdie.Sasdie):

        def __init__(self, email, student_id):
            super().__init__()
            self.setLogin(email)
            self.setPasswd(student_id)

        # on renomme la méthode "publierpage_html" en anglais
        publish_webpage = sasdie.Sasdie.publierpage_html


    _s = sasdie.Sasdie()

    # On créé un pseudo-object Map pour améliorer la lisibilité (Map <=> sasdie.Sasdie)
    sasdie.Map = lambda: (_s.creerCarte(), _s.macarte)[1]

    # On y ajoute les méthodes d'ajout d'un cercle, d'un marker et de rendu
    # pour constituer "groupe" de la même manière que Sasdie.macarte
    sasdie.Sasdie.add_circle = sasdie.Sasdie.ajoutCercleSurLaCarte
    sasdie.Sasdie.add_marker = sasdie.Sasdie.ajoutMarqueurSurLaCarte
    sasdie.Sasdie.render_html = sasdie.Sasdie.produireHTMLCarte


# On utilise les variables d'environement pour stocker les identifiants
EMAIL = os.environ.get('EMAIL')
STUDENT_ID = os.environ.get('STUDENT_ID')


def main():
    c = sasdie.API(EMAIL, STUDENT_ID)

    if not c.connect():
        print("Couldn't connect to the api.")
        return

    donnees_pol = sasdie.read_pollution_data("data-pm-sasdie-bus.csv")
    donnees_geo = sasdie.read_gps_coords()

    my_map = sasdie.Map()

    for i in range(len(donnees_geo)):
        lon1 = float(donnees_pol[i][0])
        lon2 = float(donnees_pol[i][2])
        avg_lon = (lon1 + lon2) / 2

        lat1 = float(donnees_pol[i][1])
        lat2 = float(donnees_pol[i][3])
        avg_lat = (lat1 + lat2) / 2

        my_map.add_marker(avg_lon, avg_lat, donnees_pol[i][1])

    c.publish_webpage(my_map.render_html())


if __name__ == '__main__':
    main()
