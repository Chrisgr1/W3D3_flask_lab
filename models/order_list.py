from models.order import *
import datetime

order1= Order("Spendy McSpenderson", datetime(2022,2,1), "infra-red light", 1, True)
order2= Order("Walt Disney", datetime(2022,3,1), "cryogenic chamber", 3, False)

orders = [order1, order2]