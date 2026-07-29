from textnode import *


def main():

    fetchski = TextNode("This is the Fetchski Website", TextType.LINK_TEXT, "https://fetchski.com")

    print(repr(fetchski))

if __name__ == "__main__":
    main()
