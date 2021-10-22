import unittest
import requests
import requests_mock

class TestAPI(unittest.TestCase):
    URL = 'http://127.0.0.1:5000/'

    data = {
        'name': 'test2',
        'email': 'test2@example.com'
    }

    meeting_data = {
        "persons": [
            1, 2
        ],
        "title": "title2",
        "content": "lorem ipsum2",
        "start": 1634799894.479386
    }

    def setUp(self):
        super().setUp()
        self.requests_mock = requests_mock.Mocker()
        self.requests_mock.post(self.URL, status_code='200')
        self.requests_mock.start()

    @requests_mock.Mocker()
    def test_create_person(self, m):
        m.register_uri('POST', self.URL + 'person')
        resp = requests.post(self.URL + 'person', json=self.data)
        self.assertEqual(resp.status_code, 200)
        print('Test create person')

    @requests_mock.Mocker()
    def test_create_person_error(self, m):
        m.register_uri('POST', self.URL + 'person', status_code=400)
        resp = requests.post(self.URL + 'person', json='')
        self.assertEqual(resp.status_code, 400)
        print('Test create person error')

    @requests_mock.Mocker()
    def test_create_meeting(self, m):
        m.register_uri('POST', self.URL + 'meeting')
        resp = requests.post(self.URL + 'meeting', json=self.meeting_data)
        self.assertEqual(resp.status_code, 200)
        print('Test create meeting')

    @requests_mock.Mocker()
    def test_create_meeting_error(self, m):
        m.register_uri('POST', self.URL + 'meeting', status_code=500)
        resp = requests.post(self.URL + 'meeting', json='')
        self.assertEqual(resp.status_code, 500)
        print('Test create meeting error')

    @requests_mock.Mocker()
    def test_get_schedule(self, m):
        m.register_uri('GET', self.URL + 'schedule/1', text='resp')
        resp = requests.get(self.URL + 'schedule/1')
        self.assertEqual(resp.status_code, 200)
        print('Test show schedule of a person')

    @requests_mock.Mocker()
    def test_get_schedule_error(self, m):
        m.register_uri('GET', self.URL + 'schedule', text='resp', status_code=404)
        resp = requests.get(self.URL + 'schedule')
        self.assertEqual(resp.status_code, 404)
        print('Test show schedule of a person error')

    def tearDown(self):
        super().tearDown()
        self.requests_mock.stop()

if __name__ == '__main__':
    unittest.main()
