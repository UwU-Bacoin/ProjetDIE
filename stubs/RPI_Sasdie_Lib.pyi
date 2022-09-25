class DataStream:

    def lectureDonnéesCourante(self) -> dataUnit:
        ...


    def ecritureDuFichierCSV(self) -> str:
        ...


class dataUnit:
    count: int
    pm10: int
    pm25: int

