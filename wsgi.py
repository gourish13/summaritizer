from sys import path

path.append('../')

def main():
    from app.routes.routes import app
    return app

if __name__ == "__main__":
    main().run()
