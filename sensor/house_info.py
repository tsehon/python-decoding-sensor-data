from datetime import date, datetime


class HouseInfo:
    def __init__(self, data) -> None:
        self.data = data
    
    def get_data_by_area(self, field, rec_area=0) -> list:
        field_data = []
        for record in self.data:
            if (rec_area == 0):
                field_data.append(record[field])
            elif rec_area == int(record['area']):
                field_data.append(record['area'])
        return field_data

    def get_data_by_date(self, field, rec_date=date.today()) -> list:
        field_data = []
        for record in self.data:
            if record['date'] == datetime.strftime(rec_date, "%m/%d/%y"):
                field_data.append(record['date'])
        return field_data