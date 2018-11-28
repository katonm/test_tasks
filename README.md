# Описание выполнения тестового задания

###Первое задание
   Оно выполенено на Python3, поэтому запускается так:
```python3 1.py```
   В скрипте используется генератор логина для подстановки в функцию.
   Он генерирует новый логин при каждом запуске.
   Результат выполнения программы выводится в консоль.
   
###Второе задание
   Перед запуском скрипта необходимо изменить права доступа при помощи
   команды `chmod +x 2.sh`
   Скрипт запускать там же, где запущен postgres, с помощью команды `./2.sh`
   
###Третье задание
   Если формат access.log нам известен, и мы знаем, что ip-адреса, 
   расположены, например в первом столбце, то можно воспользоваться 
   таким запросом

    `awk '{print $1}' access.log | sort | uniq -c | sort -r | head -n 10`

   Здесь:
   * awk - вызов утилиты awk
   * '{print $1}' - печать столбца с IP
   * access.log - обращение к файлу
   * sort - команда сортировки
   * uniq -c - команда для вывода количества повторений
   * sort -r - сортировка по убыванию
   * head -n 10 - вывод первых 10 строк
    
###Четвертое задание 
   * Запуск приложения 
   `python3 -m aiohttp.web -P 8080 app:app_factory`
   * Пример GET-запроса
   `curl -i -H "Accept: application/json" -H "Content-Type: application/json" http://localhost:8080/todos/1`
   * Пример DELETE-запроса
   `curl -X "DELETE" http://localhost:8080/todos/1`
   
   Оба примера запросов добавлены в скрипт `4.sh`. Необходимое окружение прописано
   в файле `requiremets.txt`.

###Пятое задание 
   В скрипт включена проверка на трёх наборах списков разной длины.
   

   
