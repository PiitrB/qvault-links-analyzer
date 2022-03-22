def sort_pages(dict):
    sorted_tuples = sorted(dict.items(), key = lambda item: item[1], reverse=True)
    #sorted_dict = {k: v for k, v in sorted_tuples}
    print(sorted_tuples)


dict = {
    "first": 45,
    "third": 15,
    "second": 25
}
sort_pages(dict)