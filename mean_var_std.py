import numpy as np


def calculate(list):
    # Si la lista no tiene exactamente 9 elementos, lanzamos un error
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convertimos la lista en una matriz de 3 filas x 3 columnas
    matriz = np.array(list).reshape(3, 3)

    # Devuelve [por columnas (axis=0), por filas (axis=1), matriz completa]
    def estadisticas(funcion):
        return [
            funcion(matriz, axis=0).tolist(),
            funcion(matriz, axis=1).tolist(),
            funcion(matriz).tolist()
        ]

    calculations = {
        'mean': estadisticas(np.mean),
        'variance': estadisticas(np.var),
        'standard deviation': estadisticas(np.std),
        'max': estadisticas(np.max),
        'min': estadisticas(np.min),
        'sum': estadisticas(np.sum),
    }

    return calculations
