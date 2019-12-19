from flask_restful import Api
import info

def add_route(api: Api):
    api.add_resource(info.InfoRoute, '/')
