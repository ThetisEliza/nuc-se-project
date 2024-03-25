from dao.database_model import DatabaseBzController

if __name__ == '__main__':
    dbc = DatabaseBzController()
    for g in dbc.getAllGroups('score'):
        print(g)