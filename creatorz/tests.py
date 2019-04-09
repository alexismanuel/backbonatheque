from django.test import TestCase
from django_rq import get_queue, enqueue


class TestApi(TestCase):

    fixtures = ["sample.json"]

    def test_get_writers(self):
        response = self.client.get("/api/writer/")
        results = response.json()
        self.assertDictEqual(results[0], {
            "id": 1,
            "books": [
                1
            ],
            "firstname": "Stephen",
            "lastname": "King",
            "publisher": "La Maison de l'horreur",
            "agent": 1
        })
        self.assertDictEqual(results[1], {
            "id": 2,
            "books": [
                2
            ],
            "firstname": "Bernard",
            "lastname": "Werber",
            "publisher": "La Maison du fantastique",
            "agent": 2
        })

    def test_get_musicians(self):
        response = self.client.get("/api/musician/")
        results = response.json()
        self.assertDictEqual(results[0], {
            "id": 1,
            "albums": [
                1
            ],
            "firstname": "Bob",
            "lastname": "Marley",
            "birthday": "1945-02-06",
            "nickname": "Bobby",
            "band": "himself",
            "instrument": "guitar",
            "agent": 1
        })
        self.assertDictEqual(results[1], {
            "id": 2,
            "albums": [
                2
            ],
            "firstname": "Niles",
            "lastname": "Rodgers",
            "birthday": "1952-11-19",
            "nickname": "Naïlz",
            "band": "Chic",
            "instrument": "guitar",
            "agent": None
        })
        self.assertDictEqual(results[2], {
            "id": 3,
            "albums": [],
            "firstname": "Nicky",
            "lastname": "Larson",
            "birthday": "1958-03-26",
            "nickname": "Ryô",
            "band": "Une ombre file dans la nuit",
            "instrument": "357 Magnum",
            "agent": 2
        })

    def test_get_customers(self):
        response = self.client.get("/api/customers/")
        results = response.json()
        self.assertDictEqual(results[0], {
            "id": 1,
            "firstname": "John",
            "lastname": "Dope",
        })


