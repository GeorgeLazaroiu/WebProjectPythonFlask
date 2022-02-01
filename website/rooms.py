from flask import Flask

class Rooms:
    id_room = 0
    number = 0
    price = 0
    no_pers = 0
    confort = 0

    def __init__(self):
        pass

    def select_from_dbData(self, data):
        self.id_room = data[0][0]
        self.number = data[0][1];
        self.price = data[0][2];
        self.no_pers = data[0][3];
        self.confort = data[0][4];

    def get_data(self):
        data ={
        self.number: 'numar',
        self.price: 'pret',
        self.no_pers: 'numar_persoane',
        self.confort: 'confort'
        }
        return data

