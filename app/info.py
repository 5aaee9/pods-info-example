from flask_restful import Resource
import requests

class InfoRoute(Resource):
    def get(self):
        res = requests.get('https://api.ip.sb/geoip')
        return res.json()
