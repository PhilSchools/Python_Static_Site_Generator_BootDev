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
        self.props = props


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
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None):
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

        if not tag and value is not None:
            return value

        if props is not None:
            props_string = self.props_to_html()

            return f"<{tag}{props_string}>{value}</{tag}>"

        return f"<{tag}>{value}</{tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag: str | None, children, props: dict[str, str] | None = None):
        super().__init__(tag, None, children, props)

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}( \n"
            f"tag={self.tag!r}, \n"
            f"children={self.children}, \n"
            f"props={self.props} \n"
            f"stringified='{self.props_to_html()}' \n"
            f")"
            )

    def to_html(self) -> str:
        tag = self.tag
        children = self.children
        props = self.props

        if not tag:
            raise ValueError("ParentNode must have tag")

        if not children:
            raise ValueError("ParentNode must have children")


        html_parts = []
        if props is not None:
            props_string = self.props_to_html()
            html_parts.append(f"<{tag}{props_string}>")
        else:
            html_parts.append(f"<{tag}>")

        for child in children:
            html_parts.append(child.to_html())

        html_parts.append(f"</{tag}>")

        return "".join(html_parts)
