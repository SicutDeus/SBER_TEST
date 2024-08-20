import unittest

from app import create_app


class DepositAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True
        self.endpoint = "/calculate"
        self.error_status_code = 400
        self.success_status_code = 200

    def test_successful_calculation(self):
        test_data = {
            "date": "31.01.2021",
            "periods": 3,
            "amount": 10000,
            "rate": 6,
        }
        expected_result = {
            "31.01.2021": 10050.0,
            "28.02.2021": 10100.25,
            "31.03.2021": 10150.75,
        }
        response = self.client.post(
            self.endpoint,
            json=test_data,
        )
        self.assertEqual(response.status_code, self.success_status_code)
        self.assertEqual(response.get_json(), expected_result)

    def test_invalid_date_format(self):
        test_data = {
            "date": "31-01-2021",
            "periods": 3,
            "amount": 10000,
            "rate": 6,
        }
        expected_msg = "date: Некорректный формат даты. Используйте формат %d.%m.%Y."
        self.check_bad_request(test_data, expected_msg, self.error_status_code)

    def test_invalid_date_type(self):
        test_data = {"date": 123, "periods": 3, "amount": 10000, "rate": 6}
        expected_msg = "date: Неверный тип поля date: ожидался str, был получен int"
        self.check_bad_request(test_data, expected_msg, self.error_status_code)

    def test_invalid_periods(self):
        test_data = {
            "date": "31.01.2021",
            "periods": 61,
            "amount": 10000,
            "rate": 6,
        }
        expected_msg = "periods: Количество месяцев по вкладу должно быть от 1 до 60. Было получено 61. "
        self.check_bad_request(test_data, expected_msg, self.error_status_code)

    def test_invalid_periods_type(self):
        test_data = {
            "date": "31.01.2021",
            "periods": "331238",
            "amount": 10000,
            "rate": 6,
        }
        expected_msg = (
            "periods: Неверный тип поля periods: ожидался int, был получен str"
        )
        self.check_bad_request(test_data, expected_msg, self.error_status_code)

    def test_invalid_amount(self):
        test_data = {
            "date": "31.01.2021",
            "periods": 3,
            "amount": 5000,
            "rate": 6,
        }
        expected_msg = (
            "amount: Сумма вклада должна быть от 10000 до 3000000. Было получено 5000. "
        )
        self.check_bad_request(test_data, expected_msg, self.error_status_code)

    def test_invalid_amount_type(self):
        test_data = {
            "date": "31.01.2021",
            "periods": 3,
            "amount": "3103",
            "rate": 6,
        }
        expected_msg = "amount: Неверный тип поля amount: ожидался int, был получен str"
        self.check_bad_request(test_data, expected_msg, self.error_status_code)

    def test_invalid_rate(self):
        test_data = {
            "date": "31.01.2021",
            "periods": 3,
            "amount": 10000,
            "rate": 9,
        }
        expected_msg = (
            "rate: Процентная ставка должна быть от 1.0 до 8.0. Было получено 9.0. "
        )
        self.check_bad_request(test_data, expected_msg, self.error_status_code)

    def test_invalid_rate_type(self):
        test_data = {
            "date": "31.01.2021",
            "periods": 3,
            "amount": 10000,
            "rate": "123",
        }
        expected_msg = (
            "rate: Неверный тип поля rate: ожидался float/int, был получен str"
        )
        self.check_bad_request(test_data, expected_msg, self.error_status_code)

    def check_bad_request(self, test_data, expected_msg, expected_status_code):
        response = self.client.post(
            self.endpoint,
            json=test_data,
        )
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(expected_msg, response.get_json()["error"])


if __name__ == "__main__":
    unittest.main()
