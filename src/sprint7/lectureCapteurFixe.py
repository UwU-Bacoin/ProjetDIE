try:
    from RPI_Sasdie_Lib import DataStream, dataUnit
    IS_REPLACEMENT = True

except ImportError:
    from fake_sasdie import DataStream, export_to_csv, IS_REPLACEMENT


if not IS_REPLACEMENT:
    DataStream.read = DataStream.lectureDonnéesCourante

    from functools import partial

    export_to_csv = partial(DataStream.ecritureDuFichierCSV, type('', (), {}))
    dataUnit.id = property(lambda self: self.count)


CSV_HEADER = "Numéro d'échantillon;PM25\n"


d = DataStream()

result = []
latest_id = 0

while len(result) <= 10:
    data = d.read()

    if data.id != latest_id:
        latest_id = data.id

        # python 3.5 :<
        result.append("{a};{b}".format(a=data.id, b=data.pm25))


export_to_csv(CSV_HEADER + "\n".join(result))
