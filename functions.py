def get_inputs() -> dict:
    # Se requieren los siguientes datos del usuario:
    # - Cantidad de galones comprados
    # - Precio de compra por galón
    # - Cantidad de tiendas
    # - Precio de venta de cada galón
    # - Ganancia por galón sobrante
    # - Demanda diaria en cada tienda

    user_input = {
        'boughtGallons': int(input('Ingrese la cantidad de galones comprados: ')),
        'costPerGallon': float(input('¿Cuánto costó cada galón? $')),
        'stores': int(input('¿En cuántas tiendas se van a vender los galones? ')),
        'pricePerGallon': float(input('¿A cuánto se venderá cada galón en las tiendas? $')),
        'pricePerRemainingStock': float(input('¿A cuánto comprarán cada galón que no fue vendido?')),
    }

    user_input['demandPerGallonPerStore'] = get_demand(user_input['boughtGallons'], user_input['stores'])

    return user_input

def get_demand(n_gallons: int, n_stores: int) -> dict:
    demand = {}
    for store in range(1, n_stores+1):
        gallons = []
        for gallonDemand in range(n_gallons+1):
            gallons.append(float(input(f'Ingrese la demanda diaria para {gallonDemand} galones en la tienda {store}: ')))
        demand[store] = gallons
    return demand

def calculate_gains(assigned_gallons: int, user_data: dict) -> dict:
    gains = {}
    for store in range(1, user_data['stores']+1):
        gain = 0
        for i in range(user_data['boughtGallons']+1):
            gain += user_data['demandPerGallonPerStore'][store][i]*aux(assigned_gallons, i, user_data)
        gains[store] = gain
    return gains

def aux(x_n: int, i: int, user_data: dict) -> float:
    if x_n > i:
        return user_data['pricePerGallon']*i + user_data['pricePerRemainingStock']*(x_n - i)
    else:
        return user_data['pricePerGallon']*x_n