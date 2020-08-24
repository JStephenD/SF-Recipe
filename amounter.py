def amounter(d, a):
    rv = {}
    for k, v in d.items():
        # print(k, v)
        if isinstance(v, dict):
            rv[k] = amounter(v, a)
        else:
            rv[k] = v*a
    return rv