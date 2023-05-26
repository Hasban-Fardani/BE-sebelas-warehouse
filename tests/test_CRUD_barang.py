import unittest
import requests

base_url = 'http://localhost:8080/api'
login_url = f'{base_url}/operator/login'
barang_keluar_url = f'{base_url}/barang'

class TestBarangKeluarAPI(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()

    def tearDown(self):
        self.session.get(f'{base_url}/operator/logout')

    def test_login(self):
        login_data = {
            "NI": 123,
            "password": "123"
        }
        response = self.session.post(login_url, json=login_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['message'], 'Login successful!')

    def test_get_barang_keluar(self):
        self.test_login()
        response = self.session.get(barang_keluar_url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)

    def test_create_barang_keluar(self):
        self.test_login()
        new_barang_keluar = {
            "id": "3",
            "item_name": "Barang 3",
            "item_code": "GHI789"
        }
        response = self.session.post(barang_keluar_url, json=new_barang_keluar)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['message'], 'Barang Keluar created successfully!')

    def test_update_barang_keluar(self):
        self.test_login()
        update_barang_keluar = {
            "item_name": "Barang 3 Updated",
            "item_code": "GHI789"
        }
        response = self.session.put(f'{barang_keluar_url}/3', json=update_barang_keluar)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['message'], 'Barang Keluar updated successfully!')

    def test_delete_barang_keluar(self):
        self.test_login()
        response = self.session.delete(f'{barang_keluar_url}/3')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['message'], 'Barang Keluar deleted successfully!')

if __name__ == '__main__':
    unittest.main()
