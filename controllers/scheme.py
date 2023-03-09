import json
from models.algo import AlgoModel
from models.color import ColorModel
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

    def like_schema(self, user_id, scheme_id):
        self.pg.execute('Insert into liked_schemas("user", scheme) values(%s, %s)', vars=(
            user_id, scheme_id,))

    def dislike_schema(self, user_id, scheme_id):
        self.pg.execute('delete from liked_schemas where "user" = %s and liked_schemas.scheme = %s', vars=(
            user_id, scheme_id,))

    def user_liked(self, user_id):
        schemas_raw = self.pg.execute(
            'select * from schema_view where "belongs to" = %s', vars=(user_id,))
        temp = {}
        for i in schemas_raw:
            if i[0] not in temp:
                temp[i[0]] = {
                    "algo": i[1],
                    "colors": [
                        {
                            "name": i[4],
                            "hex": i[5],
                            "rgb": [
                                int(i[6][0]),
                                int(i[6][1]),
                                int(i[6][2])]}]}
            else:
                temp[i[0]]["colors"].append({
                    "name": i[4],
                    "hex": i[5],
                    "rgb": [
                        int(i[6][0]),
                        int(i[6][1]),
                        int(i[6][2])]})
        target = []
        for i in temp.keys():
            target.append(SchemeModel(id=i, algo=AlgoModel(name=temp[i]["algo"]), colors=[
                          ColorModel(name=j['name'], hex=j['hex'], rgb=j['rgb']) for j in temp[i]['colors']]))
        
        return target
        # schemas = []
        # for i in ids:
        #     schemas.append(SchemeModel())
