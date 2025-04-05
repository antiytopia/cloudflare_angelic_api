# cloudflare_angelic_api

Инструмент для управления Cloudflare через терминал PowerShell, удобно для массовых переездов. Ниже все о функционале.

## Возможности (｡◕‿◕｡)ﾉ*:･ﾟ✧  
- Ввод и сохранение Cloudflare API токена
- Ввод доменов списком
- Массовое добавление A-записей
- Массовое изменение IP у всех A-записей
- Включение Always Use HTTPS
- Отключение TLS 1.3
- Изменение SSL-режима (Flexible, Full, Strict)
- Полная очистка всех DNS-записей
- Просмотр NS
- Просмотр всех DNS-записей
- Действия будут применяться ко всем выбранным доменам! UwU

## Требования (¬_¬)
- Python 3.11+
- pip (идёт с Python)
- Git (только если клонируешь репозиторий)

## Установка и запуск (๑•̀ㅂ•́)و✧ 
### 1. Установи Python (если ещё не установлен)
- Скачай с официального сайта: https://www.python.org/downloads/windows/
- При установке обязательно поставь галочку: ✅ Add Python to PATH

### 2. Проверь, что Python и pip работают
**Открой PowerShell:**

1. Нажми Win + R

2. Введи PowerShell

3. Нажми Enter

**Введи команды:**

      python --version
      pip --version
Если всё установлено правильно — ты увидишь версии Python и pip.

### 3. Скачай проект
**Вариант A — через Git (если установлен Git)**

         git clone https://github.com/antiytopia/cloudflare_angelic_api.git
         cd cloudflare-angelic
   
**Вариант B — без Git**

- Зайди на GitHub-страницу проекта

- Нажми Code → Download ZIP

- Распакуй архив в удобную папку, например:

      C:\Users\user\Documents\cloudflare_angelic

Потом открой PowerShell и перейди в эту папку:

      cd "C:\Users\user\Documents\cloudflare_angelic"
(⛔ не забудь обернуть путь в кавычки, если в нём есть пробелы!)

(или открой через меню нажав shift+ПКМ в любой пустой области папки с проектом)

### 4. Создай и активируй виртуальное окружение

 Введи в терминале следующие комнады (ctrl+c-ctrl+v)

      python -m venv venv
      .\venv\Scripts\activate

После активации в начале строки появится (venv) — значит окружение работает.

### 5. Установи зависимости (один раз)
   pip install -r requirements.txt
### 6. Запусти приложение

      python main.py

Появится меню с пунктами управления, всё работает через клавиатуру — просто выбирай номер нужного действия.
      
Для последующего запуска необходимо вводить только две команды: 

      .\venv\Scripts\activate
      python main.py 


![image](https://github.com/user-attachments/assets/f29dd731-0a9b-49f9-a6f4-28965123a037)


## Как создать API токен для Cloudflare ( ‾́ ◡ ‾́ )ゝ
1. Перейди: https://dash.cloudflare.com/profile/api-tokens
2. Нажми "Create Token"
3. Выбери "Custom Token"
4. В Permissions выбери:
   
                                         Zone - Zone - Read
                                         Zone - Zone Settings - Read
                                         Zone - Zone Settings - Edit
                                         Zone - DNS - Read
                                         Zone - DNS - Edit
6. В Resource выбери: All zones (НЕ specific!)
7. Скопируй токен и вставь его при запуске

- Add A-records - добавление А-записи (@ для root работает так же)
- Change A-record IPs — замена IP у всех A-записей
- Enable Always Use HTTPS — включает принудительное HTTPS
- Disable TLS 1.3 — отключает TLS 1.3
- Change SSL Mode — выбирай режим SSL (full, strict, flexible)
- Purge All DNS Records — удаляет все DNS-записи в зоне
- Show NS Names - покажет Name Servers для выбранных доменов

**Все действия применяются сразу ко всем выбранным доменам**
Если токен не видит нужный домен — он, скорее всего, не в списке доступных зон токена
❤️ Автор

