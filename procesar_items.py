import pickle


def items_data_to_dict(items_data_ruta):
    items_data_dict = dict()
    with open(items_data_ruta) as archivo:
        for linea in archivo:
            # linea = linea[1:-2].split(', "')
            linea = linea[1:-2].split(', "title": ')
            item_id = linea[0].split(": ")[1]
            linea = linea[1].split(', "domain_id": ')
            titulo = linea[0][1:-1]
            linea = linea[1].split(', "product_id": ')
            dominio = linea[0][1:-1]
            linea = linea[1].split(', "category_id": ')
            precio = linea[0].split(', "price": ')[1][1:-1]
            condicion = linea[1].split(', "condition": ')[1][1:-1]
            items_data_dict[item_id] = [titulo, dominio, precio, condicion]
    return items_data_dict


###


items_data_ruta = "E:/Proyectos/MeLi-Data-Challenge-2020/item_data.jl"
items_data_dict = items_data_to_dict(items_data_ruta)

items_data_dict_ruta = "E:/Proyectos/MeLi-Data-Challenge-2020/items_data_dict.pickle"
with open(items_data_dict_ruta, "wb") as handle:
    pickle.dump(items_data_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
