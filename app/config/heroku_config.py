class HerokuConfig(object):
    SECRET_KEY = "top secret"
    JWT_ACCESS_LIFESPAN = {"hours": 24}
    JWT_REFRESH_LIFESPAN = {"days": 30}
    SQLALCHEMY_DATABASE_URI = "postgresql://fejblnatcukmyl:5c4a222f978934f9519248aa28596c971dac60f481ede35ae61f25db29a30c80@ec2-34-250-16-127.eu-west-1.compute.amazonaws.com:5432/d3povtoodkkcr3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
