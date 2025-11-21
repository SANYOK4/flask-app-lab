import unittest
from app import app, db

class TodoTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()
        
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_todo_page_loads(self):
        """Перевіряємо, чи відкривається сторінка /todo/"""
        response = self.client.get('/todo/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Todo List", response.data)

if __name__ == '__main__':
    unittest.main()