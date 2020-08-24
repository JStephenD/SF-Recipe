from amounter import amounter
from pprint import pprint, pformat

def carbon(amt=1): 
    return amounter({
        'coal': 8
    }, amt)

def compressed_carbon(amt=1):
    return amounter({
        'carbon': carbon(4*amt)
    }, amt)

def carbon_chunk(amt=1):
    return amounter({
        'flint': 1,
        'compressed carbon': compressed_carbon(8*amt)
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
        'carbon': carbon(1*amt),
        'iron ingot': 1
    }, amt)

def damascus_steel_ingot(amt=1):
    return amounter({
        'iron ingot': 1,
        'iron dust': 1,
        'steel ingot': steel_ingot(1*amt),
        'carbon': carbon(1*amt)
    }, amt)

def bronze_ingot(amt=1):
    return amounter({
        'copper dust': 1,
        'copper ingot': copper_ingot(1*amt),
        'tin dust': 1
    }, amt)

def duralumin_ingot(amt=1):
    return amounter({
        'aluminum dust': 1,
        'aluminum ingot': aluminum_ingot(1*amt),
        'copper dust': 1
    }, amt)

def billon_ingot(amt=1):
    return amounter({
        'silver dust': 1,
        'silver ingot': silver_ingot(1*amt),
        'copper dust': 1
    }, amt)
    
def brass_ingot(amt=1):
    return amounter({
        'copper dust': 1,
        'copper ingot': copper_ingot(1*amt),
        'zinc dust': 1
    }, amt)

def aluminum_brass_ingot(amt=1):
    return amounter({
        'aluminum dust': 1,
        'aluminum ingot':aluminum_ingot(1*amt),
        'brass ingot': brass_ingot(1*amt)
    }, amt)

def aluminum_bronze_ingot(amt=1):
    return amounter({
        'aluminum dust': 1,
        'aluminum ingot': aluminum_ingot(1*amt),
        'bronze ingot': bronze_ingot(1*amt)
    }, amt)

def hardened_metal(amt=1):
    return amounter({
        'damascus steel ingot': damascus_steel_ingot(1*amt),
        'duralumin ingot': duralumin_ingot(1*amt),
        'compressed carbon': compressed_carbon(1*amt),
        'aluminum bronze ingot': aluminum_bronze_ingot(1*amt) 
    }, amt)

def corinthian_bronze_ingot(amt=1):
    return amounter({
        'bronze ingot': bronze_ingot(1*amt),
        'silver dust': 1,
        'gold dust': 1,
        'copper dust': 1
    }, amt)

def solder_ingot(amt=1):
    return amounter({
        'lead dust': 1,
        'lead ingot': lead_ingot(1*amt),
        'tin dust': 1
    }, amt)

def synthetic_sapphire(amt=1):
    return amounter({
        'lapiz lazuli': 1,
        'aluminum dust': 1,
        'aluminum ingot': aluminum_ingot(1*amt),
        'glass': 1,
        'glass pane': 1
    }, amt)

def synthetic_diamond(amt=1):
    return amounter({
        'carbon chunk': 1
    }, amt)

def raw_carbonado(amt=1):
    return amounter({
        'carbon chunk': carbon_chunk(1*amt),
        'synthetic diamond': synthetic_diamond(1*amt),
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
        'nickel ingot': nickel_ingot(1*amt)
    }, amt)

def carbonado(amt=1):
    return amounter({
        'raw carbonado': raw_carbonado(1*amt)
    }, amt)

def silicon(amt=1):
    return amounter({
        'quartz block': 1
    }, amt)

def ferrosilicon(amt=1):
    return amounter({
        'iron dust': 1,
        'iron ingot': 1,
        'silicon': silicon(1*amt)
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
        'gold 4': gold_4(1*amt)
    }, amt)

def gold_8(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 6': gold_6(1*amt)
    }, amt)

def gold_10(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 8': gold_8(1*amt)
    }, amt)

def gold_12(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 10': gold_10(1*amt)
    }, amt)

def gold_14(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 12': gold_12(1*amt)
    }, amt)

def gold_16(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 14': gold_14(1*amt)
    }, amt)

def gold_18(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 16': gold_16(1*amt)
    }, amt)

def gold_20(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 18': gold_18(1*amt)
    }, amt)

def gold_22(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 20': gold_20(1*amt)
    }, amt)

def gold_24(amt=1):
    return amounter({
        'gold dust': 1,
        'gold 22': gold_22(1*amt)
    }, amt)

def reinforced_alloy_ingot(amt=1):
    return amounter({
        'damascus steel ingot': damascus_steel_ingot(1*amt),
        'hardened metal': hardened_metal(1*amt),
        'corinthian bronze ingot': corinthian_bronze_ingot(1*amt),
        'solder ingot': solder_ingot(1*amt),
        'billon ingot': billon_ingot(1*amt),
        'gold 24': gold_24(1*amt)
    }, amt)

def synthetic_emerald(amt=1):
    return amounter({
        'synthetic sapphire': synthetic_sapphire(1*amt),
        'aluminum dust': 1,
        'aluminum ingot': aluminum_ingot(1*amt),
        'glass pane': 1
    }, amt)

def a(amt=1):
    return amounter({
        
    }, amt)

def a(amt=1):
    return amounter({
        
    }, amt)

def a(amt=1):
    return amounter({
        
    }, amt)

def a(amt=1):
    return amounter({
        
    }, amt)

def a(amt=1):
    return amounter({
        
    }, amt)

def a(amt=1):
    return amounter({
        
    }, amt)

def a(amt=1):
    return amounter({
        
    }, amt)

def a(amt=1):
    return amounter({
        
    }, amt)

def a(amt=1):
    return amounter({
        
    }, amt)

def a(amt=1):
    return amounter({
        
    }, amt)

def a(amt=1):
    return amounter({
        
    }, amt)

def a(amt=1):
    return amounter({
        
    }, amt)

def a(amt=1):
    return amounter({
        
    }, amt)

def a(amt=1):
    return amounter({
        
    }, amt)

def a(amt=1):
    return amounter({
        
    }, amt)

def a(amt=1):
    return amounter({
        
    }, amt)


def export():
    return {
        'carbon': carbon, 'compressed_carbon': compressed_carbon, 'carbon_chunk': carbon_chunk,
        'copper_ingot': copper_ingot, 'silver_ingot': silver_ingot, 'magnesium_ingot': magnesium_ingot,
        'zinc_ingot': zinc_ingot,
    }

x = pformat(damascus_steel_ingot(1))
# print(x)