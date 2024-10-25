<div align="center">
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.herokuapp.com?font=Tektur&pause=1000&color=DC00F7&center=true&width=435&lines=TELEGRAM+REMINDER+BOT" alt="Typing SVG" /></a>
</div>

# О проекте

Telegram Reminder Bot — бот для создания напоминаний в чатах. Он реализован полностью на Golang и использует многопоточность для работы с несколькими задачами одновременно.

# Функционал бота

— Командный функционал — по команде @имя_бота ctrl NM, где N - интервал, M - единица времени бот ставит напоминание для данного пользователя и отправляет его в чат по истечении  времени. Удобно для пользователей веб-версии.

— Графический функционал — по нажатию на кнопку «Добавить напоминание» бот последовательно собирает необходимую информацию (текст напоминания, интервал, единица времени). Удобно для пользователей мобильной версии.

# Технологии

— Golang

— PostgreSQL

— REST API

— Docker

# Установка бота
1. Клонирование репозитория командой git clone

2. Установка зависимостей командами go mod go mod download и go mod tidy

Для Windows 10:<br />

4. Установка scoop:<br />
     — irm get.scoop.sh -outfile 'install.ps1'<br />

     — .\install.ps1 -RunAsAdmin<br />

     — scoop install migrate<br />

5. Установка make<br />
     — @powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin.<br />

     — choco install make<br />

6. Проверка и изменение файлов config

7. Запуск программы командой make run
