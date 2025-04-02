# cloudflare_angelic_api

Инструмент для управления Cloudflare через терминал PowerShell, удобно для массовых переездов. Ниже все о функционале.

## Возможности
- Ввод и сохранение Cloudflare API токена
- Ручной ввод доменов
- Массовое добавление A-записей
- Массовое изменение IP у всех A-записей
- Включение Always Use HTTPS
- Отключение TLS 1.3
- Изменение SSL-режима (Flexible, Full, Strict)
- Полная очистка всех DNS-записей
- Просмотр NS выбранных доменов 

## Требования
- Python 3.11+
- pip (идёт с Python)
- Git (только если клонируешь репозиторий)

## Установка и запуск
1. Установи Python (если его нет)
2. Скачай с офсайта: https://www.python.org/downloads/windows/
3. Обязательно включи галочку: Add Python to PATH
4. Проверь в PowerShell:
      python --version
      pip --version
5. Клонируй проект или скачай архив
  - git clone [https://github.com/antiytopia/cloudflare-angelic.git](https://github.com/antiytopia/cloudflare_angelic_api)
  - cd cloudflare-angelic
  Или скачай .zip с GitHub → распакуй в любую папку.
5. Создай и активируй виртуальное окружение
    python -m venv venv
    .\venv\Scripts\activate
6. Установи зависимости
    pip install -r requirements.txt
7. Запусти
    python main.py
## Как пользоваться
При запуске ты увидишь меню:
1. Set API Token
2. Input Domains Manually
3. Show Selected Zones
...
Навигация — цифрами.

## Как создать API токен для Cloudflare
1. Перейди: https://dash.cloudflare.com/profile/api-tokens
2. Нажми "Create Token"
3. Выбери "Custom Token"
4. В Permissions выбери:
- Zone - Read
- Zone Settings - Read
- Zone Settings - Edit
- DNS - Read
- DNS - Edit
5. В Resource выбери: All zones (НЕ specific!)
6. Скопируй токен и вставь его при запуске

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

