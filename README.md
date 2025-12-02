# Проект автоматизации тестирования (SkyPro)

Автоматизированные тесты для веб-приложений с использованием Selenium WebDriver, Pytest и Allure.

## Как запустить тесты для формирования отчета

### 1. Установите необходимые зависимости
```bash
pip install selenium pytest allure-pytest
```
### 2. Запустите тесты с генерацией Allure-отчета
```bash
pytest --alluredir=allure-results
```
### 3. Для запуска конкретных тестов
```bash
pytest test_calculator.py --alluredir=allure-results
```
или
```bash
pytest test_saucedemo.py --alluredir=allure-results
```

## Как просмотреть сформированный отчет
### 1. Установите Allure CLI (если еще не установлен)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
scoop install allure
```
### 2. Сгенерируйте HTML-отчет
```bash
allure generate allure-results -o allure-report --clean
```
### 3. Откройте отчет в браузере
```bash
allure open allure-report
```
## Альтернативный способ (прямой просмотр без сохранения)
```bash
allure serve allure-results
```
