import re

import utils.constants as constants

class DevicesParser():

    ram = None
    rom = None
    brand = None
    model = None

    def __init__(self, string, ram, rom, brand):        
        self.ram = ram
        self.rom = rom
        self.brand = brand.name.lower()
        self.model = self.get_model(string)

    def get_model(self, model):
        model_stop_words = constants.get_model_stop_words()
        try:
            model = re.sub(model_stop_words, '', model.lower()).strip()
            model = model.replace('celular', '')
            model = re.sub(' +', ' ', model)
        except:
            pass   

        return model


    


