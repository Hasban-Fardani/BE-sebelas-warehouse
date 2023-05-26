from flask_login import login_required, current_user
from flask import request as req
from flask import jsonify
from models.barang_model import Barang
from models.barang_in import Barang_Masuk

class BarangController:
    @login_required
    def get_barang_by_id(id):
        barang_keluar = Barang.select().where(Barang.id == id)
        data = [{'id': bk.id, 'item_name': bk.item_name, 'operator_id': bk.operator_id.id} for bk in barang_keluar]
        return jsonify(data)

    @login_required
    def add_barang():
        data = req.get_json()
        barang_keluar = Barang_Masuk.create(
            id=data['id'],
            operator_id=current_user.id,
            item_name=data['item_name'],
            item_code=data['item_code'],
            room_id=data['room_id'],
            type=data['type'],
            brand=data['brand'],
            note=data['note'],
            jumlah_b=data['jumlah_b'],
            jumlah_kb=data['jumlah_kb'],
            jumlah_rb=data['jumlah_rb']
        )

        return jsonify({'message': 'Barang Keluar created successfully!', 'id': barang_keluar.id})

    @login_required
    def update(id):
        data = req.get_json()
        Barang.update(
            item_name=data['item_name'],
            item_code=data['item_code'],
            room_id=data['room_id'],
            type=data['type'],
            brand=data['brand'],
            note=data['note'],
            jumlah_b=data['jumlah_b'],
            jumlah_kb=data['jumlah_kb'],
            jumlah_rb=data['jumlah_rb']
        ).where(Barang.id == id).execute()
        return jsonify({'message': 'Barang Keluar updated successfully!', 'id': id})

    @login_required
    def delete(id):
        Barang.delete().where(Barang.id == id).execute()
        return jsonify(message='Barang Keluar deleted successfully!')

    