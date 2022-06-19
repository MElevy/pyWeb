import socket

def response(html):
    text = f"""HTTP/2 200
content-type: text/html

{html}"""
    return text

class View:
    def __init__(self):
        self.html = str(self.view())

    def view(self):
        return "Hello! This is the default message, to modify it, overrun the 'view' method."

    def run(self, host="127.0.0.1", port=8000):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            print(f"Running on http://{host}:{port}/")
            while 1:
                try:
                    s.listen()
                    conn, addr = s.accept()
                    with conn:
                        print("Connection to", addr)
                        conn.sendall(self.html.encode("utf-8"))
                except KeyboardInterrupt:
                    if input("Are you sure you want to exit(y/N)? ").lower() in ("y", "yes", "yup", "correcto", "y!", "yes!", "correcto!"):
                        break
        print("Server closed")
