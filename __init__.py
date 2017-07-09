import os

from app import create_app

# pylint:disable=invalid-name
app = create_app()

if __name__ == "__main__":
    app.run()
