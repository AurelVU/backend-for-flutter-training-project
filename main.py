from app import create_app
from app.config import BaseConfig


app = create_app(config=BaseConfig)

if __name__ == "__main__":
    app.run(debug=True)