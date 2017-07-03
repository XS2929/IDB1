""" Launch the application """
import os

from app import create_app

# pylint:disable=invalid-name
application = create_app()

if __name__ == "__main__":
    application.run()