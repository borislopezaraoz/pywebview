import webview

html = """
<!doctype html>
<html lang="en" data-framework="javascript">
    <head>
        <meta charset="utf-8">
        <title>counter</title>
    </head>
    <body>
        <div id="counter">
        </div>
        <button onclick="send('chg', -10)">--</button>
        <button onclick="send('chg', -1)">-</button>
        <button onclick="send('res')">reset</button>
        <button onclick="send('chg', 1)">+</button>
        <button onclick="send('chg', 10)">++</button>
    </body>
    <script type="text/javascript">
        function send(...message) {
            window.pywebview.api.update(...message);
        }
    </script>
</html>
"""

class Model:
    counter = 0


def reset():
    update('res')


def update(*message):
    cmd, args = message[0], message[1:]
    print(f"{cmd}{args}")
    if cmd == 'res':
        model.counter = 0
    elif cmd == 'chg':
        model.counter = model.counter + args[0]
    render()


def render():
    window.evaluate_js(f"document.getElementById('counter').innerHTML={model.counter}")


if __name__ == '__main__':
    model = Model()
    window = webview.create_window('counter', html=html)
    window.expose(update)
    webview.start(reset)
