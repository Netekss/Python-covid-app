import os
import requests
import datetime
import webbrowser

from geo import Geo
from format_date import FormatDate


class Data:

    @staticmethod
    def get_data(decision):
        raw_data = requests.get('https://opendata.ecdc.europa.eu/covid19/casedistribution/json/')
        data = raw_data.json()

        last_7_days = []
        cases = []

        # checking for country
        if decision == 1:
            country = Geo().geo_auto()
        elif decision == 2:
            country = Geo().geo_manual()

        # getting data from last 7 days for specific country
        for record in data['records']:
            if record['countriesAndTerritories'] == country:
                date_from_record = record['dateRep']  # date in format DD/MM/YYYY
                date = FormatDate().change_date_format(date_from_record)  # date formatted to YYYY/MM/DD

                today = datetime.date.today()
                delta = today - date

                if delta.days == 7:
                    for i in range(7):
                        another_day = FormatDate().another_day(i, date)
                        last_7_days.append(another_day)

        # getting cases for each day from last 7 days
        for record in data['records']:
            for day in last_7_days:
                if (record['countriesAndTerritories'] == country) and (record['dateRep'] == day):
                    cases.append(int(record['cases']))

        # returning average cases
        try:
            avg_cases = (sum(cases) / len(cases))
            avg_cases = round(avg_cases)

            return decision, country, avg_cases

        except ZeroDivisionError:
            print(f'\n--error-- download data failed for country "{country}"')

    @staticmethod
    def question():
        possible_answers = ["y", "n"]

        while True:
            decision = input("Do you want to read instruction how to avoid infection? [y]/[n]: ").lower().replace(" ",
                                                                                                                  "")

            if decision in possible_answers:
                if decision == "y":
                    webbrowser.open(os.path.realpath('recommendations.html'))
                    break
                elif decision == "n":
                    break
                else:
                    continue

    @staticmethod
    def show_cases(data):
        country = data[1]
        avg_cases = data[2]

        if data[0] == 1:
            if avg_cases < 500:
                print("\n==LOW RISK==\n"
                      f"Average cases per day from last 7 days in your country ({country}) is {avg_cases}")
                Data.question()
            elif 500 <= avg_cases < 1500:
                print("\n==MEDIUM RISK==\n"
                      f"Average cases per day from last 7 days in your country ({country}) is {avg_cases}")
                Data.question()
            elif 1500 <= avg_cases < 3000:
                print("\n==HIGH RISK==\n"
                      f"Average cases per day from last 7 days in your country ({country}) is {avg_cases}")
                Data.question()
            elif avg_cases >= 3000:
                print("\n==VERY HIGH RISK==\n"
                      f"Average cases per day from last 7 days in your country ({country}) is {avg_cases}!")
                Data.question()

        elif data[0] == 2:
            if avg_cases < 500:
                print("\n==LOW RISK==\n"
                      f"Average cases per day from last 7 days in country ({country}) is {avg_cases}")
                Data.question()
            elif 500 <= avg_cases < 1500:
                print("\n==MEDIUM RISK==\n"
                      f"Average cases per day from last 7 days in country ({country}) is {avg_cases}")
                Data.question()
            elif 1500 <= avg_cases < 3000:
                print("\n==HIGH RISK TRAVEL IS NOT RECOMMENDED==\n"
                      f"Average cases per day from last 7 days in country ({country}) is {avg_cases}")
                Data.question()
            elif avg_cases >= 3000:
                print("\n==VERY HIGH RISK TRAVEL IS NOT RECOMMENDED==\n"
                      f"Average cases per day from last 7 days in country ({country}) is {avg_cases}!")
                Data.question()
