d={}
def update_dictionary(d, key, value):
    if key in d:
        d[key]+=[value]
    elif key not in d:
        if (2*key) in d:
            d[2*key]+=[value]
        else:
            d[2*key]= [value]
    return d
print(update_dictionary(d, 1, -4))  