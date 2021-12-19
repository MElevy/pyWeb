class Html:
    def __init__(self, title, body):
        self.title, self.body = title, body

    def __str__(self):
        html = f"""
<!DOCTYPE html>
<head>
<title>{self.title}</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
{self.body}
</body>
""".strip("\n")
        return html

class Element:
    def __init__(self, element, children=[], href=None, src=None, id=None, class_=None, style=None, name=None, placeholder=None, action=None, method=None, type=None, onsubmit=None, onclick=None, value=None, oninput=None):
        self.id, self.class_ = id, class_
        self.children = children
        self.element = element
        self.href, self.src = href, src
        self.style = style
        self.onclick, self.oninput = onclick, oninput
        self.method, self.action, self.onsubmit = method, action, onsubmit
        self.placeholder, self.name, self.type, self.value = placeholder, name, type, value

    def __str__(self):
        html = f'<{self.element}'
        if self.href:
            html += f' href="{self.href}"'
        if self.src:
            html += f' src="{self.src}"'
        if self.id:
            html += f' id="{self.id}"'
        if self.class_:
            html += f' class="{self.class_}"'
        if self.style:
            html += f' style="{self.stylize()}"'
        if self.action:
            html += f' action="{self.action}"'
        if self.method:
            html += f' method="{self.method}"'
        if self.placeholder:
            html += f' placeholder="{self.placeholder}"'
        if self.name:
            html += f' name="{self.name}"'
        if self.type:
            html += f' type="{self.type}"'
        if self.value:
            html += f' value="{self.value}"'
        if self.onsubmit:
            html += f' onsubmit="{self.onsubmit}"'
        if self.onclick:
            html += f' onclick="{self.onclick}"'
        if self.oninput:
            html += f' oninput="{self.oninput}"'
        html += '>'
        for child in self.children:
            if len(self.children) in (1, 0):
                html += str(child)
            else:
                html += f'\n{str(child)}'
        if len(self.children) in (1, 0):
            html += f'</{self.element}>'
        else:
            html += f"\n</{self.element}>"
        return html

    def stylize(self):
        style = ""
        for k, v in self.style.items():
            style += f'{k}:{v};'
        return style

class P(Element):
    def __init__(self, children=[], style=None, id=None, class_=None, onclick=None):
        super().__init__("p", children=children, id=id, class_=class_, style=style, onclick=onclick)

class A(Element):
    def __init__(self, children=[], href=None, id=None, class_=None, style=None, onclick=None):
        super().__init__("a", href=href, children=children, id=id, class_=class_, style=style, onclick=onclick)

class H1(Element):
    def __init__(self, children=[], id=None, class_=None, style=None, onclick=None):
        super().__init__("h1", children=children, id=id, class_=class_, style=style, onclick=onclick)

class H2(Element):
    def __init__(self, children=[], id=None, class_=None, style=None, onclick=None):
        super().__init__("h2", children=children, id=id, class_=class_, style=style, onclick=onclick)

class H3(Element):
    def __init__(self, children=[], id=None, class_=None, style=None, onclick=None):
        super().__init__("h3", children=children, id=id, class_=class_, style=style, onclick=onclick)

class H4(Element):
    def __init__(self, children=[], id=None, class_=None, style=None, onclick=None):
        super().__init__("h4", children=children, id=id, class_=class_, style=style, onclick=onclick)

class H5(Element):
    def __init__(self, children=[], id=None, class_=None, style=None, onclick=None):
        super().__init__("h5", children=children, id=id, class_=class_, style=style, onclick=onclick)

class H6(Element):
    def __init__(self, children=[], id=None, class_=None, style=None, onclick=None):
        super().__init__("h6", children=children, id=id, class_=class_, style=style, onclick=onclick)

class Div(Element):
    def __init__(self, children=[], id=None, class_=None, style=None, onclick=None):
        super().__init__("div", children=children, id=id, class_=class_, style=style, onclick=onclick)

class Nav(Element):
    def __init__(self, children=[], id=None, class_=None, style=None, onclick=None):
        super().__init__("nav", children=children, id=id, class_=class_, style=style, onclick=onclick)

class Form(Element):
    def __init__(self, children=[], action="/", method="get", id=None, class_=None, style=None, onclick=None, onsubmit=None):
        super().__init__("form", children=children, action=action, method=method, id=id, class_=class_, style=style, onclick=onclick, onsubmit=onsubmit)

class Input(Element):
    def __init__(self, children=[], type="text", name=None, placeholder=None, value=None, style=None, onclick=None, id=None, class_=None, oninput=None):
        super().__init__("input", children=children, type=type, name=name, placeholder=placeholder, value=value, style=style, onclick=onclick, id=id, class_=class_, oninput=oninput)

class CharField(Input):
    def __init__(self, children=[], name=None, placeholder=None, value=None, style=None, id=None, class_=None, oninput=None):
        super().__init__(children=children, name=name, type="text", value=value, style=style, placeholder=placeholder, id=id, class_=class_, oninput=oninput)

class PasswordField(Input):
    def __init__(self, children=[], name=None, placeholder=None, value=None, style=None, id=None, class_=None, oninput=None):
        super().__init__(children=children, placeholder=placeholder, value=value, style=style, name=name, type="password", id=id, class_=class_, oninput=oninput)

class SubmitButton(Input):
    def __init__(self, children=[], name=None, value=None, style=None, onclick=None, id=None, class_=None):
        super().__init__(children=children, value=value, style=style, name=name, onclick=onclick, id=id, class_=None, type="submit")

class Button(Element):
    def __init__(self, children=[], value=None, id=None, class_=None, onclick=None, style=None):
        super().__init__("button", children=children, value=value, id=id, class_=class_, onclick=onclick, style=style)

class Script(Element):
    def __init__(self, children=[], src=None):
        super().__init__("script", children=children, src=src, type="text/javascript")

class Canvas(Element):
    def __init__(self, children=[], id=None, class_=None, style=None, onclick=None):
        super().__init__("canvas", children=children, id=id, class_=class_, style=style, onclick=onclick)
