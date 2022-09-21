import RPI_Sasdie_Lib

d = RPI_Sasdie_Lib.DataStream()
buffer = "Numéro d’échantillon;PM25\n"

for i in range(10):
    data = d.lectureDonnéesCourante()
    # La version de python est tellement veille qu'elle ne support pas les f-string
    # Le RPI utilise python 3.5.3 alors que le support de cette version (patch de sécurité)
    # à été arrêté il y a plus de 2 ans...

    buffer += "{d.count};{d.pm25}\n".format(d=data)

d.ecritureDuFichierCSV(buffer)
