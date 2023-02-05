import psycopg2
from psycopg2 import Error


class Store:
    def __init__(self):
        self.users_with_dates = dict()

    def add_user_to_list(self, user_id: int, time):
        self.users_with_dates[user_id] = time

    def get_users_with_dates(self):
        return self.users_with_dates

