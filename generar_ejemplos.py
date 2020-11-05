import pickle


def generar_ejemplos(datos_entrenamiento_ruta, items_dict):
    with open(datos_entrenamiento_ruta) as archivo:
        for linea in archivo:
            cadena = str()
            linea = linea[1:-2].split('], ')
            y = linea[1].split(" ")[1]
            x = linea[0].split(": [")[1][1:-1].split("}, {")
            print(y)
            for e in x:
                eventos = e.split(", ")
                evento_tipo = eventos[2].split(": ")[1][1:-1]
                evento_info = eventos[0].split(": ")[1]
                texto = str()
                if evento_tipo == "view" or evento_tipo == "purchase":
                    texto = items_dict[evento_info]
                elif evento_tipo == "search":
                    texto = evento_info[1:-1].lower()
                print(texto)
                cadena = cadena + " " + texto
            print(cadena)
            print(len(cadena))
            # break





# Carga del diccionario de items
items_dict_ruta = "E:/Proyectos/MeLi-Data-Challenge-2020/items_dict.pickle"
with open(items_dict_ruta, "rb") as handle:
    items_dict = pickle.load(handle)

datos_entrenamiento_ruta = "E:/Proyectos/MeLi-Data-Challenge-2020/train_dataset.jl"
generar_ejemplos(datos_entrenamiento_ruta, items_dict)