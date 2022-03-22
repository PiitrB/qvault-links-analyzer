def remove_none_values(dict):
    delete = []
    for k, v in dict.items():
        if v is None:
            delete.append(k)
    for key in delete:
        del dict[key]
    return dict