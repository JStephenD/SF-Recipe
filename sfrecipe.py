def ferrosilicon(amt=1):
    return amounter({
        'quartz blocks': 1,
        'iron dust': 1,
        'iron ingot': 1
    }, amt)
    
def hardened_metal(amt=1):
    return amounter({
        'coal': 48, 
        'aluminum dust': 4, 
        'copper dust': 3, 
        'iron ingot': 2, 
        'iron dust': 2, 
        'tin dust': 1
    }, amt)