def main():
    from sys import path
    path.append('../')
    from app.routes.routes import app
    return app

if __name__ == "__main__":
    main().run()
