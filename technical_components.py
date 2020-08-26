from math import ceil
from amounter import amounter
from resources import (
    copper_ingot, zinc_ingot, sulfate, nickel_ingot,
    cobalt_ingot, reinforced_alloy_ingot, synthetic_diamond,
    synthetic_sapphire, brass_ingot
)

def battery(amt=1):
    return amounter({
        'copper ingot': copper_ingot(2),
        'zinc ingot': zinc_ingot(2),
        'sulfate': sulfate(2),
        'redstone dust': 1
    }, amt)

def magnet(amt=1):
    return amounter({
        'nickel ingot': nickel_ingot(1),
        'cobalt ingot': cobalt_ingot(1),
        'aluminum dust': 1,
        'iron dust': 1
    }, amt)

def electromagnet(amt=1):
    return amounter({
        'nickel ingot': nickel_ingot(1),
        'cobalt ingot': cobalt_ingot(1),
        'magnet': magnet(1),
        'batter': battery(1)
    }, amt)

def copper_wire(amt=8):
    return {
        'copper ingot': copper_ingot(3*ceil(amt/8))
    }

def electric_motor(amt=1):
    return amounter({
        'copper wire': copper_wire(6),
        'electromagnet': electromagnet(1)
    }, amt)

def heating_coil(amt=1):
    return amounter({
        'electric motor': electric_motor(1),
        'copper wire': copper_wire(8)
    }, amt)

def reinforced_plate(amt=1):
    return amounter({
        'reinforced alloy ingot': reinforced_alloy_ingot(8)
    }, amt)

def hardened_glass(amt=16):
    return {
        'glass': 8*ceil(amt/16),
        'reinforced plate': reinforced_plate(1*ceil(amt/16))
    }

def power_crystal(amt=1):
    return amounter({
        'redstone dust': 4,
        'synthetic_sapphire': 4,
        'synthetic_diamond': 1
    }, amt)

def android_memory_core(amt=1):
    return amounter({
        'power_crystal': 2,
        'tin dust': 1,
        'orange stained glass': 2,
        'brass_ingot': brass_ingot(4)
    }, amt)

def export():
    return {
        'battery': battery, 'magnet': magnet, 'electromagnet': electromagnet,
        'copper_wire': copper_wire, 'electric_motor': electric_motor,
        'heating_coil': heating_coil, 'reinforced_plate': reinforced_plate,
        'hardened_glass': hardened_glass, 'power_crystal': power_crystal, 
        'android_memory_core': android_memory_core
    }