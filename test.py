from controllers.scheme import SchemeController
from models.algo import AlgoModel
from models.color import ColorModel
from models.scheme import SchemeModel


controller = SchemeController()

controller.postScheme(SchemeModel(algo=AlgoModel(name="test"), colors=[ColorModel(name="test1", hex="#110011", rgb=[
                      1, 2, 3]), ColorModel(name="test2", hex="#110011", rgb=[1, 2, 3]), ColorModel(name="test3", hex="#110011", rgb=[1, 2, 3])]), user_id=1)
