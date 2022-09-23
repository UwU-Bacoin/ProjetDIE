# -*- coding: utf-8 -*-
# http://all4dev.libre-entreprise.org/index.php/Des_constantes_en_python
import time
import json
import csv
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


class Const:
    def __init__(self):
        Const.__items = {}

    def __getattr__(self, attr):
        try:
            return Const.__items[attr]
        except:
            return self.__dict__[attr]

    def __setattr__(self, attr, value):
        if attr in Const.__items.keys():  # En python 2.1, écrire if attr in Const.__items.keys()
            raise "Cannot reassign constant %s" % attr
        else:
            Const.__items[attr] = value

    def __str__(self):
        return '\n'.join(['%s: %s' % (str(k), str(v)) for k, v in Const.__items.items()])


const = Const()
const.dataServeur = "127.0.0.1"
const.nomfichierpm10 = 'data_pm10.csv'
const.nomfichierpm25 = 'data_pm25.csv'


class dataUnit:
    def __init__(self, c, dj):
        self.count = c
        self.data = dj
        self.pm10 = -1
        self.pm25 = -1
        self.tic = -1
        if self.data:
            self.pm10 = self.data["pm10"]
            self.pm25 = self.data["pm25"]
            self.tic = self.data["tic"]

    def __str__(self):
        return '(pm10={} pm25={} tic={})'.format(self.pm10, self.pm25, self.tic)


class DataStream:

    def __init__(self):
        def on_message(mqtt_client, userdata, msg):
            # Ignore errors
            try:
                self.currentPayload = str(msg.payload.decode("utf-8"))
            except:
                pass
            try:
                # print(msg.topic, self.currentPayload)
                pl = json.loads(self.currentPayload)
                if "pm25" in pl and "pm10" in pl and "tic" in pl:
                    self.currentPayloadJson = pl
                    self.currentPayloadJsonCount = self.currentPayloadJsonCount + 1
            except:
                pass

        self.data = self
        self.csv = self
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_message = on_message
        self.mqtt_client.connect(const.dataServeur, port=1884)  # , keepalive=180)
        self.mqtt_client.subscribe("#")
        self.mqtt_client.loop_start()
        self.currentPayloadJson = json.loads('{}')
        self.currentPayloadJsonCount = 0
        print("DataStream est initialisé")

    def lectureDonnéesCourante(self):
        time.sleep(2)
        du = dataUnit(self.currentPayloadJsonCount, self.currentPayloadJson)
        return du

    def ecritureDuFichierCSV(self, c):
        if c == None:
            return False
        self.fichier = open(const.nomfichierpm25, 'w')
        self.fichier.write(c)
        self.fichier.close()
        # to check
        try:
            with open(const.nomfichierpm25, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                print("écriture de :")
                for row in reader:
                    print(row)
        except:
            return False
        return True
