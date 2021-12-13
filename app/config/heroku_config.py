class HerokuConfig(object):
    SECRET_KEY = "top secret"
    JWT_ACCESS_LIFESPAN = {"hours": 24}
    JWT_REFRESH_LIFESPAN = {"days": 30}
    SQLALCHEMY_DATABASE_URI = "postgresql://zskisktcgpcjig:6aaab573a652d0263acd8de16476f5ff4a98cb71534d76fddb7b62062c30a6d7@ec2-52-48-137-75.eu-west-1.compute.amazonaws.com:5432/d5e4scnlqnmnda"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
