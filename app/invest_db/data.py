import pandas as pd
import re


class InvestObj:
    economy = pd.read_excel("techno.xlsx", sheet_name="List1")
    regional_measure = pd.read_excel("measure.xlsx", sheet_name="List1")
    room_construction = pd.read_excel("room.xlsx", sheet_name="List1")

    def redefine(self):
        result = self.room_construction["Перечень видов экономической деятельности, возможных к реализации на площадке"].str.replace(r"[^\d\.]", "", regex=True)
        result.to_excel("r.xlsx", sheet_name="List1")



    def find_object(self, **filters):
        object_kind = self.room_construction.loc[
            self.room_construction["Формат площадки"] == filters["object_type"], "Формат площадки"]
        business = self.room_construction.loc[self.room_construction["ОКВЭД"] == filters["business"], "Формат площадки"]
        print(business)


# InvestObj().find_object(object_type="Земельный участок", business="")
InvestObj().redefine()
