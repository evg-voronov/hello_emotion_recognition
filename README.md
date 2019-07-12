<p align="center">
  <img src="screenshot/hello..png"/></div>
</p>

Surface
-------
**Surface** — это приложение разработанное командой hello, которое способно облегчить процесс реабилитации людей, переживших инсульт.  С помощью web камеры пользователь сможет в режиме реального времени выполнять упражнения и восстанавливать нормальную подвижность мимических мышц. В отличие от обычного зеркала наше приложение способно идентифицировать мимические мышцы и следить за ними а также определять эмоции.

### Surface работает в двух режимах. 

**Первый режим** — это выполнение упражнений. К программе предоставляется документация базовых заданий, которые необходимо выполнять для восстановление мышц лица, в процессе выполнения упражнений на лице отображаются контрольные точки с помощью, которых в будущем планируется вести мониторинг прогресса (следить за изменением подвижность мышц вычисляя координаты точки).

<p align="center">
  <img src="screenshot/key_points.png"/></div>
</p>

**Второй режим** — это проверка на способность корректно выражать эмоции. Программа с помощью нейронной сети способно детектировать 7 базовых эмоций (радость, удивление, грусть, злость, отвращение, страх, нейтральная эмоция) и выводить результат на экран в виде процентной вероятности. Также к программе предоставляется документация по тому, как правильно следует выражать конкретную эмоцию.

<p align="center">
  <img src="screenshot/emotion.png"/></div>
</p>

## Описание

Приложение состоит из двух несвязанных частей.

С помощью первой части производятся исследование 

**emotion_photo_test.py** — скрипт который на вход принимает набор изображений распознает эмоции и сохраняет новый набор с описанием того где какая эмоция используется.

**find-face-photo-test.py** — с помощью данного скрипта тестируется работа двух детекторов лиц (haar каскад и hog). Скрипт также предназначен для работы с набором фотографий.

**find-face-video_test.py** — тоже самое только уже для видео.

Вторая часть с графическим интерфейсом для пользователей.

**find-face-video.py** — часть приложения которое определяет лицо и ключевые точки

**emotion_video.py** — скрипт определяет эмоции

**neural_network.py** — скрипт нейронной сети (подробнее про используемую нейронную сеть можно прочитать в научной статье)

**find-face-haar.xml** — классификатор из библиотеки opencv с помощью которого производится детектирование лиц.

**form_fon.py** — пользовательский интерфейс написанный с помощью библиотеки PyQt5 (именно тот файл который нужно запускать)

С помощью интерфейса вы можете включить режим зеркала (просто запись с web камеры), включить отображение ключевых точек для выполнения упражнений или режим распознования эмоций. Также есть возможность поставить трансляцию на паузу.

## Установка 

В настоящее время приложение не имеет единую сборку поэтому для его запуска необходимо установить следующие библиотеки

`Python 3.6`

`Opencv 4`

`imutils 0.5.2`

`numpy 1.16`

`tensorflow 1.14`

`tflearn 0.3.2`

`keras 2.2`

`PyQt5`

`dlib 19.17`

Если вы используете windows, то прежде, чем установить dlib необходимо установить следующие компоненты

`Visual Studio 2015`

`CMake v3.8.2`

`Anaconda 3`

Если вы используете Linux прежде, чем ставить dlib установите

`Boost`

`Boost.Python`

`CMake`

`X11`

Также необходимо скачать файлы нейронной сети в корень каталога программы 

https://drive.google.com/open?id=1-nrr8RoJLvX6v-OblMLLGVicNean0yqE
