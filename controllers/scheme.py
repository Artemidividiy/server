import json
from models.scheme import SchemeModel
from models.user import UserModel
from services.postgresDefault import PostgreServiceDefault


class SchemeController:
    def __init__(self) -> None:
        self.pg = PostgreServiceDefault()

    def getSchemas(self):

        schemas = self.pg.execute("select * from schema_view", vars=())
        return json.dumps(schemas)

    def postScheme(self, scheme: SchemeModel) -> SchemeModel:
        try:
            algo = self.pg.execute(
                "select id from public.algorithms where name = %s", (scheme.algo.name,))
            if len(algo) == 0:
                raise Exception()
        except:
            print(f"no algo found in database. adding {scheme.algo}")
            self.pg.execute(
                "insert into public.algorithms (name) values(%s)", vars=(scheme.algo.name,))
            algo = self.pg.execute(
                "select id from algorithms where name = %s", vars=(scheme.algo.name,))
        print(algo)
        self.pg.execute(
            "INSERT INTO public.schemas(algo) VALUES ( %s );", vars=(algo))
        scheme.id = self.pg.execute(
            "select id from public.schemas order by id desc limit 1", ())[0][0]
        for i in scheme.colors:
            self.pg.execute("INSERT INTO public.colors(name, hex, rgb) VALUES ( %s, %s, %s);", vars=(
                i.name, i.hex, i.rgb,))
            i.id = self.pg.execute(
                "select id from public.colors order by id desc limit 1 ", vars=())[0][0]
        for i in scheme.colors:
            self.pg.execute(
                "insert into public.colors_in_schemas(color, schema) values (%s, %s)", vars=(i.id, scheme.id,))
        
        return scheme

    def like_schema(self, user, scheme):
        self.pg.execute("Insert into liked_schemas(user, schema) values(%s, %s)", vars=(
            user.id, scheme.id,))
