def remove_none_values(dict):
    delete = []
    for k, v in dict.items():
        if v is None:
            delete.append(k)
    for key in delete:
        del dict[key]
    return dict


def sort_pages(dict):
    sorted_tuples = sorted(dict.items(), key = lambda item: item[1], reverse=True)
    sorted_dict = {k: v for k, v in sorted_tuples}
    return sorted_dict
    
def print_report(pages):
    report = remove_none_values(pages)
    report = sort_pages(report)
    for link, count in report.items():
        print(f"Found {count} internal links for {link}")
