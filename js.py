class Js:
    def __init__(self, js):
        self.js = js

    def __str__(self):
        return self._replace(self.js)

    def _replace(self, js):
        dict = {
            "ids": "document.getElementById",
            "classes": "getElementsByClass",
            "text": "innerHTML",
            "def": "function",
            "print": "console.log"
        }
        for k, v in dict.items():
            js = js.replace(k, v)
        return js

if __name__=="__main__":
    js = """def set() {
    var out = ids("output")
    var in = ids("input")
    out.text = in.value
}"""
    print(Js(js))
