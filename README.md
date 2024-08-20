[![CI](https://github.com/SicutDeus/SBER_TEST/actions/workflows/ci.yml/badge.svg)](https://github.com/SicutDeus/SBER_TEST/actions/workflows/ci.yml)
# Калькулятор депозита
## Описание

Этот сервис представляет собой REST API на Flask для расчета суммы вклада по месячным периодам.

## Запуск приложения

### Локальный запуск

1. Клонируйте репозиторий:
   ```bash
   git clone <your-repository-url>
   cd deposit_calculator
   ```
2. Создайте и активируйте виртуальное окружение:
    ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
4. Запустите приложение
   ```
   flask run
   ```

### Запуск с использованием Docker
1. Постройте Docker-образ:
   ```bash
   docker build -t deposit-calculator .
   ```
2. Запустите контейнер:
    ```
   docker run -d -p 5000:5000 deposit-calculator
   ```
#### Приложение будет доступно по адресу http://127.0.0.1:5000.

## Пример запроса
Для расчета суммы вклада выполните POST-запрос по следующему URL: `/calculate`

#### Пример тела запроса:
```
{
  "date": "31.01.2021",
  "periods": 3,
  "amount": 10000,
  "rate": 6.0
}
```
#### Описание параметров:

| Имя     | Тип     | Валидация                              | Описание                     |
|---------|---------|----------------------------------------|------------------------------|
| date    | String  | Формат даты dd.mm.YYYY                 | Дата заявки                  |
| periods | Integer | от <u>1</u> до <u>60</u>               | Количество месяцев по вкладу |
| amount  | Integer | от <u>10 0000</u> до <u>3 000 000</u>  | Сумма вклада                 |
| rate    | Float   | от <u>1</u> до <u>8</u>                | Процент по вкладу            |

#### Пример успешного ответа

Если запрос выполнен успешно, API вернет статус 200 и тело ответа в формате JSON, содержащее сумму вклада на конец каждого месяца:

```
{
  "31.01.2021": 10050.0,
  "28.02.2021": 10100.25,
  "31.03.2021": 10150.75
}
```

#### Пример неуспешного ответа

Если запрос содержит некорректные данные, API вернет статус 400 и сообщение об ошибке.

```
{
   "error": "Некорректный формат даты. Используйте формат dd.mm.YYYY."
}
```
Возможные ошибки для различных полей: 

| Имя     | Тип ошибки             | Сообщение ошибки                                                             |
|---------|------------------------|------------------------------------------------------------------------------|
| date    | Неверный тип           | Некорректный формат даты: Формат даты должен быть dd.mm.YYYY.                |
| date    | Не пройдена валидация  | Некорректный формат даты: Дата должна быть строкой.                          |
| periods | Неверный тип           | Количество месяцев вклада должно быть целым числом.                          |
| periods | Не пройдена валидация  | Количество месяцев вклада должно быть от 1 до 60.                            |
| amount  | Неверный тип           | Сумма вклада должна быть целым числом.                                       |
| amount  | Не пройдена валидация  | Некорректная сумма вклада: Сумма вклада должна быть от 10 000 до 3 000 000.  |
| rate    | Неверный тип           | Процентная ставка должна быть числом с плавающей точкой.                     |
| rate    | Не пройдена валидация  | Некорректная процентная ставка: Процентная ставка должна быть от 1.0 до 8.0. |


## Тестирование
Для запуска unit-тестов выполните команду:
```
python -m unittest discover -s tests 
```
Создание репорта о покрытии тестами:
```
coverage run -m unittest discover -s tests
```
Просмотр репорта о покрытии тестами (в папке tests на гите есть ридми с таблицей о покрытии):
```
coverage report
```
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqFKUAfCZsgf3lb849Hw5D_U4G_4mapvtVTQ&s)

