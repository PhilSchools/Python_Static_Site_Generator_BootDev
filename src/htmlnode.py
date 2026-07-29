class HTMLNode:
    def __init__(
        self, 
        tag: str | None = None, 
        value: str | None = None, 
        children: list["HTMLNode"] | None = None, 
        props: dict[str, str] | None = None
    ):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}


    def to_html(self):

        raise NotImplementedError

    def props_to_html(self) -> str:

        parts = [f'{k}="{v}"' for k, v in self.props.items()]

        return " " + " ".join(parts)

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}( \n"
            f"tag={self.tag!r}, \n"
            f"value={self.value!r}, \n"
            f"children={self.children}, \n"
            f"props={self.props} \n"
            f"stringified='{self.props_to_html()}' \n"
            f")"
            )

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str | None, props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}( \n"
            f"tag={self.tag!r}, \n"
            f"value={self.value!r}, \n"
            f"props={self.props} \n"
            f"stringified='{self.props_to_html()}' \n"
            f")"
            )

    def to_html(self) -> str:
        tag = self.tag
        value = self.value
        props = self.props

        if props is not None:
            props_string = self.props_to_html()
            if tag == "a":
                return f"<{tag}{props_string}>{value}</{tag}>"

        return f"<{tag}>{value}</{tag}>"