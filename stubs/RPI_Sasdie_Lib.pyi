class DataStream:
    def lectureDonn√©esCourante(self) -> dataUnit: ...
    def ecritureDuFichierCSV(self) -> str: ...

class dataUnit:
    count: int
    pm10: int
    pm25: int
