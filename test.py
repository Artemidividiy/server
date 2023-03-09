from controllers.scheme import SchemeController
from models.algo import AlgoModel
from models.color import ColorModel
from models.scheme import SchemeModel


controller = SchemeController()

print(controller.user_liked(6))
