from itertools import product


class Order():

    def __init__(self, customer_name, order_date, product_name, quantity, mailing_list):
        self.customer_name = customer_name
        self.order_date = order_date
        self.product_name = product_name
        self.quantity = quantity
        self.mailing_list = mailing_list