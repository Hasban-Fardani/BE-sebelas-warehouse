from controller import OperatorController
from flask.blueprints import Blueprint

# create new blueprint for API
blueprint = Blueprint(__name__, "blueprint", static_folder="static", url_prefix='/api')

# routes for operator
operator_br = Blueprint("operator", "operator_blueprint", url_prefix='/operator')
operator_br.route('/test', methods=["GET", "POST"])(OperatorController.test_login)
operator_br.get('/<int:id>')(OperatorController.get_operator_by_id)
operator_br.post('/register')(OperatorController.register_operator)
operator_br.post('/login')(OperatorController.login_operator)
operator_br.route('/logout', methods=["POST", "GET"])(OperatorController.logout_operator)

# routes for barang
barang_br = Blueprint("barang", "barang_blueprint", url_prefix='/barang')


blueprint.register_blueprint(operator_br)
blueprint.register_blueprint(barang_br)