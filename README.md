# apipy	

Это набор python скриптов для автоматизированной проверки простых API запросов методами GET и POST.
Скрипты имеют единый интерфейс с возможностью выбора метода тестирования, демонстрации результатов API запросов, сохранения [response body](/img/response.PNG), подсчета времени ответа, повторного проведения набора тестов, [записи логов](/img/log.PNG), сохранения результатов для каждого теста в [простом отчете](/img/report.PNG) формата xlsx для дальнейшего просмотра и редактирования.

**Порядок установки:**

- Установите интерпретатор Python версии 3.8 или выше, с официального сайта  [python](https://www.python.org/downloads/)
- Установите дополнительные пакеты 

	- requests
 	- openpyxl

  c помощью командной строки, используя команду ```pip3 install [package name]```
- Клонируйте репозиторий
- Переместитe файлы из папки QApipy в выбранную директорию

**Порядок работы:**

- Изучите документацию тестируемого API
- Подготовьте тестовые данные
- Изучите шаблон составления тестов [template.txt](template.txt)
- Перейдите в папку testrun
- Выберите подпапку get или post согласно тестируемому методу
- Cоздайте в выбранной подпапке файлы JSON с тестовыми сценариями	
- Откройте и запустите файл QApipy.py используя стандартную среду разработки Python IDLE,
  либо оболочку командной строки python, запустив файл QApipy.bat
- Следуя информационным указаниям выберите тестируемый метод и возможность сохранения отчета
- Запустите созданную последовательность тестов
- Отслеживайте состояние и статус прохождения тестов в последующем информационном сообщении
- По завершению прохождения тестов, выберите дальнейшие действия в меню


	![alt text](/img/result.PNG)

Результаты работы скрипта с запуском одного теста, средствами командной строки



Успехов в Вашей работе !
