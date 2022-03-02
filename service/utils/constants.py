from enum import Enum

POSSIBLE_MEMORY_VALUES = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
BRANDS_DICT = {
    'Samsung': 'samsung',
    'iPhone': 'iphone',
    'Xiaomi': 'xiaomi|redmi',
    'Huawei': 'huawei',
    'LG': 'lg',
    'Alcatel': 'alcatel',
    'Motorola': 'motorola|moto',
    'Nokia': 'nokia',
    'Pixel': 'pixel',
    'ZTE': 'zte',
    'Oppo': 'oppo',
    'Honor': 'honor',
    'Vivo': 'vivo',
    'Realme': 'realme'

}

BRANDS_DICT_REQUEST = BRANDS_DICT.copy()
BRANDS_DICT_REQUEST['default'] = 'any'
BRANDS_DICT_REQUEST['Xiaomi'] = 'xiaomi'
BRANDS_DICT_REQUEST['Motorola'] = 'motorola'
BRANDS_DICT_REQUEST['iPhone'] = 'apple'


BRAND_ENUM = Enum('BRAND_ENUM', BRANDS_DICT_REQUEST)

def get_model_stop_words():
    model_stop_words = '/'
    for k,v in BRANDS_DICT.items():
        model_stop_words = model_stop_words + '|' + v
    for v in ['GB', 'Gb', 'gb']:
        model_stop_words = model_stop_words + '|' + v
    model_stop_words = model_stop_words +  '|(?<=con).+|con'

    return model_stop_words