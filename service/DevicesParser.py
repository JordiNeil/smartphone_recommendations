import re

import utils.constants as constants

class DevicesParser():

    ram = None
    rom = None
    brand = None
    model = None

    def __init__(self, string, ram, rom):        
        self.ram = ram
        self.rom = rom
        self.brand = self.get_brand(string)
        self.model = self.get_model(string)

    def get_brand(self, string):
        for k, v in constants.BRANDS_DICT.items():
            if re.search(v, string.lower()):
                return k
        return None

    def get_model(self, string):
        model_stop_words = constants.get_model_stop_words()
        model = re.sub(model_stop_words, '', string.lower()).strip()
        try:
            model = model.replace('celular', '')
            model = re.sub(' +', ' ', model)
        except:
            pass   

        return model


    


