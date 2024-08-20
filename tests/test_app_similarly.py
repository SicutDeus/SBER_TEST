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
        self.default_data = {
            "date": "31.01.2021",
            "periods": 3,
            "amount": 10000,
            "rate": 6,
        }
        self.invalid_cases = [
            (
                {"date": "31-01-2021"},
                "date: Некорректный формат даты. Используйте формат %d.%m.%Y.",
            ),
            (
                {"date": 123},
                "date: Неверный тип поля date: ожидался str, был получен int",
            ),
            (
                {"periods": 61},
                "periods: Количество месяцев по вкладу должно быть от 1 до 60. Было получено 61. ",
            ),
            (
                {"periods": "331238"},
                "periods: Неверный тип поля periods: ожидался int, был получен str",
            ),
            (
                {"amount": 5000},
                "amount: Сумма вклада должна быть от 10000 до 3000000. Было получено 5000. ",
            ),
            (
                {"amount": "3103"},
                "amount: Неверный тип поля amount: ожидался int, был получен str",
            ),
            (
                {"rate": 9},
                "rate: Процентная ставка должна быть от 1.0 до 8.0. Было получено 9.0. ",
            ),
            (
                {"rate": "123"},
                "rate: Неверный тип поля rate: ожидался float/int, был получен str",
            ),
        ]

    # def test_successful_calculation(self):
    #     test_data = self.default_data.copy()
    #     expected_result = {
    #         "31.01.2021": 10050.0,
    #         "28.02.2021": 10100.25,
    #         "31.03.2021": 10150.75,
    #     }
    #     response = self.client.post(self.endpoint, json=test_data)
    #     self.assertEqual(response.status_code, self.success_status_code)
    #     self.assertEqual(response.get_json(), expected_result)
    #
    # def test_invalid_inputs(self):
    #     for update, expected_msg in self.invalid_cases:
    #         with self.subTest(update=update):
    #             test_data = self.default_data.copy()
    #             test_data.update(update)
    #             self.check_bad_request(test_data, expected_msg)
    #
    # def check_bad_request(self, test_data, expected_msg):
    #     response = self.client.post(self.endpoint, json=test_data)
    #     self.assertEqual(response.status_code, self.error_status_code)
    #     self.assertEqual(response.get_json()["error"], expected_msg)


if __name__ == "__main__":
    unittest.main()
