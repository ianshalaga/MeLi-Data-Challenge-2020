import re
import unicodedata
import pickle


def noacentos(s):
    s = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        unicodedata.normalize("NFD", s), 0, re.I
    )
    s = unicodedata.normalize("NFC", s)
    return s


def items_data_to_dict(items_data_ruta):
    '''
    Mete en un diccionario los datos que considero relevantes para el entrenamiento de un modelo NLP.
    '''
    items_dict = dict()
    with open(items_data_ruta) as archivo:
        for linea in archivo:
            linea = linea[1:-2].split(', "')
            cadena = str()
            for elemento in linea:
                if "item_id" in elemento:
                    clave = elemento.split(": ")[1]
                if "title" in elemento:
                    cadena = cadena + " " + elemento.split(": ")[1][1:-1]
                if "price" in elemento:
                    cadena = cadena + " " + elemento.split(": ")[1][1:-1]
                if "condition" in elemento:
                    cadena = cadena + " " + elemento.split(": ")[1][1:-1]
            items_dict[clave] = noacentos(cadena).lower()
    return items_dict


###


items_data_ruta = "E:/Proyectos/MeLi-Data-Challenge-2020/item_data.jl"
item_dict = items_data_to_dict(items_data_ruta)

items_dict_ruta = "E:/Proyectos/MeLi-Data-Challenge-2020/items_dict.pickle"
with open(items_dict_ruta, "wb") as handle:
    pickle.dump(item_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
