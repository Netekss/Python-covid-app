import requests


class Geo:
    @staticmethod
    def geo_auto():
        data = requests.get('http://geolocation-db.com/json/')
        data_json = data.json()
        country = data_json['country_name']
        return country

    @staticmethod
    def geo_manual():
        country = input("Input country name which you want to check: ").title().replace(" ", "")
        return country
