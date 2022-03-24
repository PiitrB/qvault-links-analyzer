import sys

from crawl import crawl_page
from report import print_report


def main():
    if len(sys.argv) != 2:
        exit(1)
    empty_dict = {}
    pages = crawl_page(sys.argv[1], sys.argv[1], empty_dict)
    print(pages)
    print_report(pages)

if __name__ == "__main__":
    main()