# Crear una matriz 3D que represente los datos de temperaturas diarias en diferentes ciudades
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas o 1 mes)
temperaturas = [
    [   # Ciudad 1 Puyo
        [   # Semana 1
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 20}
        ]
    ],
    [   # Ciudad 2 Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 16}
        ],
        [ # Semana 3
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 15}
        ]
    ],
    [   # Ciudad 3 Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 34}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 33}
        ]
    ]
]

# Promedio de temperaturas para cada una de las ciudades segun la semana
ciudades = ["Ciudad de Puyo", "Ciudad de Quito", "Ciudad de Guayaquil"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")