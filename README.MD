# Парсер срока истечения прокси-сервера с belurk.online

Этот проект позволяет автоматически авторизоваться на сайте, а затем парсить таблицу с прокси-серверами (IPv4) и вывести их в консоль. Он использует Python, библиотеку Selenium для автоматизации браузера и dotenv для загрузки конфиденциальных данных из файла `.env`.

## Установка
### Клонировать репозиторий:
```
git clone https://github.com/shusharkin/Domconnect_test_task.git
cd Domconnect_test_task
```
Заполнить файл .env в корне проекта и добавить в него ваш email и пароль:
```
EMAIL=your-email@example.com
PASSWORD=your-password
```
### Использование
Запустите скрипт с помощью следующей команды:
```
python belurk_parser.py
```
Скрипт автоматически откроет браузер, выполнит вход на сайт с использованием ваших данных, а затем спарсит таблицу с прокси-серверами. Информация о каждом прокси будет выведена в консоль в формате:
```
<IP-адрес> - <Дата истечения>
<IP-адрес> - <Дата истечения>
<IP-адрес> - <Дата истечения>
```