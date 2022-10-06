import unittest

from application.website import create_app


def get_client():
    app = create_app()
    app.testing = True
    return app.test_client()


class MyTestCase(unittest.TestCase):

    def test_login_get(self):
        url = "/login"
        response = get_client().get(url)
        self.assertEqual(response.status_code, 200, "Error invoking get on login")

    def test_signup_get(self):
    
        url = "/sign-up"
        response = get_client().get(url)
        self.assertEqual(response.status_code, 200, "Error during get on sign up")

    def test_signup_post(self):

        url = "/sign-up"
        mimetype = 'application/x-www-form-urlencoded'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype
        }

        # This user is not present in the db
        data = {
            'email': 'test@gmail.com',
            'firstName': 'test_user',
            'lastName': 'test_end_name',
            'gender': 'unknown',
            'phoneNumber': 99999999999,
            'password1': 'password123',
            'password2': 'password123',
            'age': 25,
            'city': 'Raleigh'
        }

        response = get_client().post(url, data=data, headers=headers)
        self.assertEqual(response.status_code, 200, "Error during post on sign up")

    def test_login_post(self):

        url = "/login"
        mimetype = 'application/x-www-form-urlencoded'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype
        }

        # This user is not present in the db
        data = {
            'email': 'test@gmail.com',
            'password': 'password123',
        }

        response = get_client().post(url, data=data, headers=headers)
        self.assertEqual(response.status_code, 200, "Error during post on login")


if __name__ == '__main__':
    unittest.main()
