from math import ceil
from amounter import amounter
from resources import (
    copper_ingot, zinc_ingot, sulfate, nickel_ingot,
    cobalt_ingot,
)

def battery(amt=1):
    return amounter({
        'copper_ingot': copper_ingot(2*amt),
        'zinc_ingot': zinc_ingot(2*amt),
        'sulfate': sulfate(2*amt),
        'redstone_dust': 1
    }, amt)

def magnet(amt=1):
    return amounter({
        'nickel_ingot': nickel_ingot(1*amt),
        'cobalt_ingot': cobalt_ingot(1*amt),
        'aluminum_dust': 1,
        'iron_dust': 1
    }, amt)

def electromagnet(amt=1):
    return amounter({
        'nickel_ingot': nickel_ingot(1*amt),
        'cobalt_ingot': cobalt_ingot(1*amt),
        'magnet': magnet(1*amt),
        'batter': battery(1*amt)
    }, amt)

def copper_wire(amt=8):
    return amounter({
        'copper_ingot': copper_ingot(3*ceil(amt//8))
    }, amt)

def electric_motor(amt=1):
    return amounter({
        'copper_wire': copper_wire(6*amt),
        'electromagnet': electromagnet(1*amt)
    }, amt)

def heating_coil(amt=1):
    return amounter({
        'electric_motor': electric_motor(1*amt),
        'copper_wire': copper_wire(8*amt)
    }, amt)



def export():
    return {
        'battery': battery, 'magnet': magnet, 'electromagnet': electromagnet,
        'copper_wire': copper_wire, 'electric_motor': electric_motor,
        'heating_coil': heating_coil
    }