from source import create_app

def main():
    app = create_app()
    app.run(port=8080, debug=True)


if __name__ == "__main__":
    main()