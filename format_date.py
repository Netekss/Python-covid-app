import datetime


class FormatDate:
    @staticmethod
    def change_date_format(date):
        splitted_data = str(date).split("/")
        new_date = datetime.date(int(splitted_data[2]),
                                 int(splitted_data[1]),
                                 int(splitted_data[0]),
                                 )  # Converted from str to datetime object
        return new_date

    @staticmethod
    def another_day(i, day):
        another = day + datetime.timedelta(days=i)
        splitted_data = str(another).split("-")
        expected_date = f"{splitted_data[2]}/{splitted_data[1]}/{splitted_data[0]}"
        return expected_date
