import sys

from crawl import crawl_page


def main():
    if len(sys.argv) != 2:
        exit(1)
    empty_dict = {}
    pages = crawl_page(sys.argv[1],empty_dict)
    # print(f"This is the name of the script: {sys.argv[0]}")
    # print(f"Number of arguments: {len(sys.argv)}")
    # print(f"The argument is: {str(sys.argv[1])}")
    print(pages)

if __name__ == "__main__":
    main()