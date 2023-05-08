from app import app
import unittest


class TestApp(unittest.TestCase):

    def test_fetch_pass_percentage(self):

        client = app.test_client(self)

        response = client.post('/teaching/passpercentage', json={
            'teacher_id': '3'
        })

        self.assertIn('Pass Percentage', str(response.json.keys()))

        self.assertEqual(response.status_code, 200)

    def test_add_invalid_teacher_id(self):

        client = app.test_client(self)

        response = client.post('/teaching/add', json={
            'teacher_id': '3',
            'teacher_name': 'Sahil',
            'subject_codes': ['CSL201', 'CSL202']
        })

        self.assertEqual(response.status_code, 400)

    def test_ping(self):

        client = app.test_client(self)

        response = client.get('/ping')

        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()