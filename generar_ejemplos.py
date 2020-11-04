import pickle


def generar_ejemplos(datos_entrenamiento_ruta, items_dict):
    with open(datos_entrenamiento_ruta) as archivo:
        for linea in archivo:
            linea = linea[1:-2].split('], ')
            y = linea[1].split(" ")[1]
            print(linea[0])
            print(linea[1])
            print(y)
            break





# Carga del diccionario de items
items_dict_ruta = "E:/Proyectos/MeLi-Data-Challenge-2020/items_dict.pickle"
with open(items_dict_ruta, "rb") as handle:
    items_dict = pickle.load(handle)

datos_entrenamiento_ruta = "E:/Proyectos/MeLi-Data-Challenge-2020/train_dataset.jl"
generar_ejemplos(datos_entrenamiento_ruta, items_dict)