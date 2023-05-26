from controller import OperatorController, BarangController
from flask.blueprints import Blueprint

# create new blueprint for API
blueprint = Blueprint(__name__, "blueprint", static_folder="static", url_prefix='/api')

# routes for operator
operator_br = Blueprint("operator", "operator_blueprint", url_prefix='/operator')
operator_br.route('/', methods=["GET", "POST"])(OperatorController.get_self)
operator_br.route('/test', methods=["GET", "POST"])(OperatorController.test_login)
operator_br.get('/<int:id>')(OperatorController.get_operator_by_id)
operator_br.get('/all')(OperatorController.get_all)
operator_br.post('/register')(OperatorController.register_operator)
operator_br.post('/login')(OperatorController.login_operator)
operator_br.route('/logout', methods=["POST", "GET"])(OperatorController.logout_operator)

# routes for barang
barang_br = Blueprint("barang", "barang_blueprint", url_prefix='/barang')
barang_br.get("/<int:id>")(BarangController.get_barang_by_id)
barang_br.post("/")(BarangController.add_barang)
barang_br.put("/<id>")(BarangController.update)
barang_br.delete("/<id>")(BarangController.delete)

blueprint.register_blueprint(operator_br)
blueprint.register_blueprint(barang_br)