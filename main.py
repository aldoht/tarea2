import functions

# Quite el comentario de esta sección para resolver el problema dado con mi planteamiento
# data = {
#     'boughtGallons': 5,
#     'costPerGallon': 2.0,
#     'stores': 4,
#     'pricePerGallon': 6.0,
#     'pricePerRemainingStock': 0.2,
#     'demandPerGallonPerStore': {
#         0: [0.32, 0.06, 0.14, 0.1],
#         1: [0.23, 0.12, 0.02, 0.13],
#         2: [0.05, 0.04, 0.02, 0.23],
#         3: [0.05, 0.22, 0.2, 0.27],
#         4: [0.2, 0.28, 0.33, 0.12],
#         5: [0.15, 0.28, 0.29, 0.15]
#     }
# }

# Quite el comentario de esta sección para resolver el problema dado con el planteamiento original
# data = {
#     'boughtGallons': 6,
#     'costPerGallon': 1.0,
#     'stores': 3,
#     'pricePerGallon': 2.0,
#     'pricePerRemainingStock': 0.5,
#     'demandPerGallonPerStore': {
#         0: [0, 0, 0],
#         1: [0.6, 0.5, 0.4],
#         2: [0, 0.1, 0.3],
#         3: [0.4, 0.4, 0.3],
#         4: [0, 0, 0],
#         5: [0, 0, 0],
#         6: [0, 0, 0]
#     }
# }

# Comente esta línea si desea usar uno de los planteamientos ya definidos
data = functions.get_inputs()

gains = {}
for i in range(data['boughtGallons']+1):
    gains[i] = functions.calculate_gains(i, data)

result = functions.assign_gallons(data['boughtGallons'], data['stores'], gains)
print(f'La ganancia máxima es de ${round(result[0], 4)} con la siguiente asignación {result[1]}.')