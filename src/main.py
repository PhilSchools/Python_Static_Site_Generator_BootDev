from htmlnode import *
from textnode import *


def main():

    # fetchski = TextNode("This is the Fetchski Website", TextType.LINK_TEXT, "https://fetchski.com")

    # print(repr(fetchski))

    html = HTMLNode("a", "This is a Link", None, {"href": "https://link.com", "target": "_blank"})
    html_propped = html.props_to_html()

    print(f"{html!r} \n\n")
    print(html_propped)




if __name__ == "__main__":
    main()
