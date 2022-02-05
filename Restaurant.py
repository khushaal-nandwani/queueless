from Table import Table


class Restaurant:

    tables: list[Table]
    name: str

    def __init__(self, name):
        self.tables = []
        self.name = name

    def add_table(self, table: Table) -> bool:
        pass

    def occupy_table(self, size_of_table: Table) -> bool:
        pass

    def vacate_table(self, size_of_table: Table) -> bool:
        pass

    def get_vacancy_info(self) -> dict:
        """ Returns the tables and seats available"""
        pass

