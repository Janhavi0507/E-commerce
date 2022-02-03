from enum import Enum
class counCode(Enum):
    India = '+91'
    USA   = '+1'




class phoneNo():
    countryCode = None
    numberSize = None
    Number = None

    def _init_(self, number = None, CCode = counCode.India, numSize = 10):
        self.countryCode = CCode.value
        self.numberSize = numSize
        self.Number = number
    
    def _repr_(s) -> str:
        return f"{s.countryCode} {s.Number}"




class address:
    RN_Floor_Building = None
    Strt_Area = None
    City_State = None

    def _init_(self, RNFB, SA, CS) -> None:
        self.RN_Floor_Building = RNFB
        self.Strt_Area = SA
        self.City_State = CS
    
    def _repr_(s) -> str:
        return f"{s.RN_Floor_Building}/{s.Strt_Area}/{s.City_State}"










class Currency:
    Name = None
    PerUSD = None
    C_Type = None

    def _init_(self, cId, name, pUSD, ctype='Physical') -> None:
        self.currency_Id = cId
        self.Name = name
        self.PerUSD = pUSD
        self.C_Type = ctype
    
    def _repr_(self) -> str:
        return f"{self.Name} : {self.PerUSD} : {self.C_Type}"
    
    def _str_(self) -> str:
        return f"{self.Name}"




from django.db import models

class Country(models.Model):
    counName: str = None
    counCode: str = None
    currency: str = None

    def _init_(self, name, cCode, currency = '($):US Dollars') -> None:
        self.counName = name
        self.counCode = cCode
        self.currency = currency
    
    def _repr_(self) -> str:
        return f"{self.counName} : {self.counCode} : {self.currency}"
    
    def _str_(self) -> str:
        return f"{self.counName}"