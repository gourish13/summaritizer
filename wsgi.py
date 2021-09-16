from sys import path
path.append('../')

from app.routes.routes import app

def main():
    return app

if __name__ == "__main__":
    from os import environ
    main().run(debug=True, addr='0.0.0.0', port=int(environ['PORT']))
