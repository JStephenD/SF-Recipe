from amounter import amounter
from pprint import pprint, pformat

def carbon(amt=1): 
    return amounter({
        'coal': 8
    }, amt)

def compressed_carbon(amt=1):
    return amounter({
        'carbon': carbon(4)
    }, amt)

def carbon_chunk(amt=1):
    return amounter({
        'flint': 1,
        'compressed carbon': compressed_carbon(8)
    }, amt)

def copper_ingot(amt=1):
    return amounter({
        'copper dust': 1
    }, amt)

def tin_ingot(amt=1):
    return amounter({
       'tin dust': 1
    }, amt)

def silver_ingot(amt=1):
    return amounter({
        'silver dust': 1
    }, amt)

def lead_ingot(amt=1):
    return amounter({
        'lead dust': 1
    }, amt)

def aluminum_ingot(amt=1):
    return amounter({
        'aluminum dust': 1
    }, amt)

def zinc_ingot(amt=1):
    return amounter({
        'zinc dust': 1
    }, amt)

def magnesium_ingot(amt=1):
    return amounter({
        'magnesium dust': 1
    }, amt)

def steel_ingot(amt=1):
    return amounter({
        'iron dust': 1,
        'carbon': carbon(1),
        'iron ingot': 1
    }, amt)

def damascus_steel_ingot(amt=1):
    return amounter({
        'iron ingot': 1,
        'iron dust': 1,
        'steel ingot': steel_ingot(1),
        'carbon': carbon(1)
    }, amt)

def bronze_ingot(amt=1):
    return amounter({
        'copper dust': 1,
        'copper ingot': copper_ingot(1),
        'tin dust': 1
    }, amt)

def duralumin_ingot(amt=1):
    return amounter({
        'aluminum dust': 1,
        'aluminum ingot': aluminum_ingot(1),
        'copper dust': 1
    }, amt)

def billon_ingot(amt=1):
    return amounter({
        'silver dust': 1,
        'silver ingot': silver_ingot(1),
        'copper dust': 1
    }, amt)
    
def brass_ingot(amt=1):
    return amounter({
        'copper dust': 1,
        'copper ingot': copper_ingot(1),
        'zinc dust': 1
    }, amt)

def aluminum_brass_ingot(amt=1):
    return amounter({
        'aluminum dust': 1,
        'aluminum ingot':aluminum_ingot(1),
        'brass ingot': brass_ingot(1)
    }, amt)

def aluminum_bronze_ingot(amt=1):
    return amounter({
        'aluminum dust': 1,
        'aluminum ingot': aluminum_ingot(1),
        'bronze ingot': bronze_ingot(1)
    }, amt)

def hardened_metal(amt=1):
    return amounter({
        'damascus steel ingot': damascus_steel_ingot(1),
        'duralumin ingot': duralumin_ingot(1),
        'compressed carbon': compressed_carbon(1),
        'aluminum bronze ingot': aluminum_bronze_ingot(1) 
    }, amt)

def corinthian_bronze_ingot(amt=1):
    return amounter({
        'bronze ingot': bronze_ingot(1),
        'silver dust': 1,
        'gold dust': 1,
        'copper dust': 1
    }, amt)

def solder_ingot(amt=1):
    return amounter({
        'lead dust': 1,
        'lead ingot': lead_ingot(1),
        'tin dust': 1
    }, amt)

def synthetic_sapphire(amt=1):
    return amounter({
        'lapiz lazuli': 1,
        'aluminum dust': 1,
        'aluminum ingot': aluminum_ingot(1),
        'glass': 1,
        'glass pane': 1
    }, amt)

def synthetic_diamond(amt=1):
    return amounter({
        'carbon chunk': 1
    }, amt)

def raw_carbonado(amt=1):
    return amounter({
        'carbon chunk': carbon_chunk(1),
        'synthetic diamond': synthetic_diamond(1),
        'glass pane': 1
    }, amt)

def nickel_ingot(amt=1):
    return amounter({
        'copper dust': 1,
        'iron dust': 1,
        'iron ingot': 1
    }, amt)

def cobalt_ingot(amt=1):
    return amounter({
        'copper dust': 1,
        'iron dust': 1,
        'nickel ingot': nickel_ingot(1)
    }, amt)

def carbonado(amt=1):
    return amounter({
        'raw carbonado': raw_carbonado(1)
    }, amt)

def silicon(amt=1):
    return amounter({
        'quartz block': 1
    }, amt)

def ferrosilicon(amt=1):
    return amounter({
        'iron dust': 1,
        'iron ingot': 1,
        'silicon': silicon(1)
    }, amt)

def sulfate(amt=1):
    return amounter({
        'netherrack': 16
    }, amt)

def gold_4(amt=1):
    return amounter({
        'gold dust': 1
    }, amt)

def gold_6(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 4': gold_4(1)
    }, amt)

def gold_8(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 6': gold_6(1)
    }, amt)

def gold_10(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 8': gold_8(1)
    }, amt)

def gold_12(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 10': gold_10(1)
    }, amt)

def gold_14(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 12': gold_12(1)
    }, amt)

def gold_16(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 14': gold_14(1)
    }, amt)

def gold_18(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 16': gold_16(1)
    }, amt)

def gold_20(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 18': gold_18(1)
    }, amt)

def gold_22(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 20': gold_20(1)
    }, amt)

def gold_24(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 22': gold_22(1)
    }, amt)

def reinforced_alloy_ingot(amt=1):
    return amounter({
        'damascus steel ingot': damascus_steel_ingot(1),
        'hardened metal': hardened_metal(1),
        'corinthian bronze ingot': corinthian_bronze_ingot(1),
        'solder ingot': solder_ingot(1),
        'billon ingot': billon_ingot(1),
        'gold 24': gold_24(1)
    }, amt)

def synthetic_emerald(amt=1):
    return amounter({
        'synthetic sapphire': synthetic_sapphire(1),
        'aluminum dust': 1,
        'aluminum ingot': aluminum_ingot(1),
        'glass pane': 1
    }, amt)

def export():
    return {
        'carbon': carbon, 'compressed_carbon': compressed_carbon, 'carbon_chunk': carbon_chunk,
        'copper_ingot': copper_ingot, 'silver_ingot': silver_ingot, 'magnesium_ingot': magnesium_ingot,
        'zinc_ingot': zinc_ingot, 'tin_ingot': tin_ingot, 'lead_ingot': lead_ingot,
        'aluminum_ingot': aluminum_ingot, 'steel_ingot': steel_ingot, 'damascus_steel_ingot': damascus_steel_ingot,
        'bronze_ingot': bronze_ingot, 'duralumin_ingot': duralumin_ingot, 'billon_ingot': billon_ingot,
        'brass_ingot': brass_ingot, 'aluminum_brass_ingot': aluminum_brass_ingot,
        'aluminum_bronze_ingot': aluminum_bronze_ingot, 'hardened_metal': hardened_metal,
        'corinthian_bronze_ingot': corinthian_bronze_ingot, 'solder_ingot': solder_ingot,
        'synthetic_sapphire': synthetic_sapphire, 'synthetic_diamond': synthetic_diamond, 'raw_carbonado': raw_carbonado,
        'nickel_ingot': nickel_ingot, 'cobalt_ingot': cobalt_ingot, 'carbonado': carbonado, 'silicon': silicon,
        'ferrosilicon': ferrosilicon, 'sulfate': sulfate, 'gold_4': gold_4, 'gold_6': gold_6, 'gold_8': gold_8,
        'gold_10': gold_10, 'gold_12': gold_12, 'gold_14': gold_14, 'gold_16': gold_16, 'gold_18': gold_18,
        'gold_20': gold_20, 'gold_22': gold_22, 'gold_24': gold_24, 'reinforced_alloy_ingot': reinforced_alloy_ingot,
        'synthetic_emerald': synthetic_emerald,
    }