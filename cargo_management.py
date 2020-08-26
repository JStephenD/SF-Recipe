from math import ceil
from amounter import amounter
from resources import (
    silver_ingot, aluminum_bronze_ingot,bronze_ingot, billon_ingot,
    brass_ingot
)
from technical_components import (
    hardened_glass, electromagnet, electric_motor, reinforced_plate
)

def cargo_motor(amt=4):
    return {
        'hardened glass': hardened_glass(4*ceil(amt/4)),
        'silver ingot': silver_ingot(2*ceil(amt/4)),
        'electromagnet': electromagnet(2*ceil(amt/4)),
        'electrice motor': electric_motor(1*ceil(amt/4))
    }

def cargo_manager(amt=1):
    return amounter({

    }, amt)

def cargo_node(amt=4):
    return {
        'silver ingot': silver_ingot(4*ceil(amt/4)),
        'bronze ingot': bronze_ingot(4*ceil(amt/4)),
        'cargo motor': cargo_motor(1*ceil(amt/4))
    }

def cargo_node_input(amt=2):
    return {
        'cargo node': cargo_node(1*ceil(amt/2)),
        'hopper': 2*ceil(amt/2),
        'billon_ingot': billon_ingot(2*ceil(amt/2))
    }

def cargo_node_output(amt=2):
    return {
        'cargo node': cargo_node(1*ceil(amt/2)),
        'hopper': 2*ceil(amt/2),
        'brass_ingot': brass_ingot(2*ceil(amt/2))
    }

def export():
    return {
        'cargo_motor': cargo_motor, 'cargo_manager': cargo_manager,
        'cargo_node': cargo_node, 'cargo_node_input': cargo_node_input,
        'cargo_node_output': cargo_node_output
    }
