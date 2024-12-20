import getpass
import poplib

# Настройки для подключения к Outlook
pop3_server = 'outlook.office365.com'
username = 'eztwokey@bk.ru'  # Укажите полный адрес электронной почты
password = 'agent123zxc9'  # Ваш пароль

try:
    # Подключаемся к POP3-серверу Outlook
    M = poplib.POP3_SSL(pop3_server)
    
    # Входим в почтовый ящик
    M.user(username)
    M.pass_(password)
    
    print("Подключение успешно!")
    
    # Получаем количество сообщений
    numMessages = len(M.list()[1])
    print(f"Количество сообщений: {numMessages}")
    
    # Выводим содержимое каждого сообщения
    for i in range(numMessages):
        print(f"\nСообщение {i + 1}:")
        for j in M.retr(i + 1)[1]:
            print(j.decode('utf-8'))  # Декодируем байты в строку

    # Закрываем соединение
    M.quit()

except Exception as e:
    print("Ошибка подключения:", e)
