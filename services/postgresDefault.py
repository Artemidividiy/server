import json
from typing import Any
from psycopg2 import sql, connect

class PostgreServiceDefault:
    def __init__(self, host = None, port= None, database= None, user= None, password= None) -> None:
        default_config = json.load(fp=open("configs/postgres.json", "r"))
        target = ""
        if host == None: 
            self.host = default_config["host"]
            target += "host configured via config"
        else: 
            self.host = host 
            target += "host configured via given port"
        if port == None: 
            self.port = default_config["port"]
            target += "port configured via config"
        else: 
            self.port = port 
            target += "port configured via given port"
        if database == None: 
            self.database = default_config["database"]
            target += "database name configured via given port"
        else: 
            self.database = database 
            target += "database name configured via given port"
        if user == None: 
            self.user = default_config["user"]
            target += "username configured via given port"
        else: 
            self.user = user 
            target += "username configured via given port"
        if password == None: 
            self.password = default_config["password"]
            target += "password configured via given port"
        else: 
            self.password = password 
            target += "password configured via given port"
        try: self.connect()
        except Exception as e:
            print("cannot establish connection")

    def connect(self):
        self.connection = connect(host=self.host, port=self.port, dbname=self.database, user=self.user, password=self.password)
        self.cursor = self.connection.cursor()

    def get_config(self):
        return f"host: {self.host}\nport: {self.port}\ndatabase {self.database}\nusername: {self.user}\npassword: {self.password}\n-|-"

    def test_connection(self):
        self.test("Colors")
        self.test("Users")
        self.test("Liked_schemas")
        self.test("Schemas")
        self.test("Algorithms")

    def test(self, table):
        try: 
            self.cursor.execute(sql.SQL("select * from {table}").format(table=table))
            if len(self.cursor.fetchall()) == -1 : raise Exception("test failed") 
        except Exception as e:
            print(e)

    def execute(self, query, vars) -> Any:
        self.cursor.execute(query=query, vars=vars)
        self.connection.commit()
        try:
            return self.cursor.fetchall()
        except:
            print("nothing to fetch")