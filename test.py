from collections import defaultdict

def clean(d):
    rv = defaultdict(int)
    for k, v in d.items():
        if isinstance(v, dict):
            for k, v in clean(v).items():
                rv[k] = v
        else:
            rv[k] += v
    return rv


d = {
    1: 2,
    3: 4,
    14: 15,
    16: 17
}

e = {
    5: {
        6: 7,
        8: 9
    },
    10: 11,
    12: 13
}

x = ''

for i, t in enumerate(clean(e).items()):
    k, v = t
    if i == 0: x += f'>{k}: {v}'
    else: x += f'\n>{k}: {v}'

print(x)