# План: автотесты на Python (pytest)

Объект этапа 1: мини-магазин (src/shop) — цена, корзина, склад.

## База (обязательно) — shop

| # | Тема | Что делаем | Практика на коде |
|---|------|------------|------------------|
| 1 | pytest-скелет | запуск, assert, структура tests/ | test_pricing |
| 2 | Исключения | pytest.raises, сообщения | ValueError, OutOfStockError |
| 3 | Parametrize | таблица кейсов вместо копипасты | скидки 0/25/100% |
| 4 | Fixtures | @pytest.fixture, scope | общий Cart/Inventory |
| 5 | Arrange-Act-Assert | читаемый AAA в каждом тесте | рефактор существующих |
| 6 | Моки | monkeypatch / pytest-mock | платёжный шлюз, время |
| 7 | Unit vs integration | граница модулей vs сценарий | tests/unit vs tests/integration |
| 8 | Coverage | pytest --cov; не гонимся за 100% впустую | отчёт по shop |
| 9 | Регрессии | баг → тест → фикс | намеренный баг в pricing |

## Следующий слой (свой код)

| # | Тема | Зачем |
|---|------|-------|
| 10 | Свой API (FastAPI) + httpx/TestClient | HTTP без браузера |
| 11 | БД в тестах | фикстура, транзакции, изоляция |
| 12 | Property-based (hypothesis) | генерация входов |
| 13 | Markers + selective run | @pytest.mark.slow, -m |

## AQA-полигоны (после shop) — реальные учебные цели

Специально сделаны под практику ручного/автотестирования. Не «наш» продукт — публичные демо.

### API (сначала — дешевле UI)

| Цель | URL / док | Что отрабатываем |
|------|-----------|------------------|
| Restful Booker | https://restful-booker.herokuapp.com | CRUD + auth/token, нестабильность (reset ~10 мин) |
| Restful Booker Platform | https://restful-booker.herokuapp.com/apidoc/index.html | контракт, негативные кейсы |
| ReqRes | https://reqres.in | типичный REST mock (users), статусы |
| HTTPBin | https://httpbin.org | headers, status codes, auth, delay |
| JSONPlaceholder | https://jsonplaceholder.typicode.com | простой CRUD без auth |
| Petstore (Swagger) | https://petstore.swagger.io | OpenAPI + codegen / schema checks |
| ParaBank API | https://parabank.parasoft.com | банковский сценарий + UI рядом |

Стек практики: httpx / 
equests + pytest; позже schema (schemathesis / pydantic).

### UI (Playwright предпочтительнее Selenium для старта)

| Цель | URL | Что отрабатываем |
|------|-----|------------------|
| Sauce Demo | https://www.saucedemo.com | e2e магазин: login, cart, checkout, юзеры с разными багами |
| The Internet | https://the-internet.herokuapp.com | классика: alerts, frames, waits, upload, auth |
| DemoQA | https://demoqa.com | формы, widgets, dynamic elements |
| WebdriverUniversity | https://webdriveruniversity.com | набор UI-задач под автоматизацию |
| Automation Exercise | https://automationexercise.com | длинные e2e-флоу магазина + API на том же домене |
| ParaBank | https://parabank.parasoft.com | UI+API банк |
| RealWorld | https://github.com/gothinkster/realworld | « Condit » — полноценное SPA+API (несколько фронтов) |

Стек: Playwright + pytest-playwright (или Selenium + pytest, если нужен именно Selenium для вакансий).

### Рекомендуемый порядок после shop

1. Restful Booker (API + auth)  
2. Sauce Demo (Playwright e2e)  
3. The Internet (сложные локаторы / waits)  
4. Свой FastAPI поверх shop + TestClient  
5. ParaBank или RealWorld (комбо UI+API)  
6. Опционально: мобилка / нагрузка — отдельно

## Опционально (CI / Jenkins и т.п.)

Не нужно для обучения основам. Подключаем, когда локальные тесты стабильны.

| Тема | Зачем | Минимум |
|------|-------|---------|
| GitHub Actions | прогон на push/PR | job: pytest + cache pip |
| Jenkins | то же в корпоративном CI | Pipeline: checkout → venv → pytest → junit/cobertura |
| GitLab CI | альтернатива Actions | .gitlab-ci.yml |
| Allure / JUnit XML | отчёты для CI UI | --junitxml=report.xml |
| pre-commit | локальный гейт до push | ruff + pytest на staged |
| Docker | одинаковое окружение агента/CI | образ с Python + pytest |
| Selenium/Playwright | UI E2E | только после API/unit; дорого и хрупко |

Порядок опционального: **Actions (или Jenkins) → отчёт JUnit → Docker**. UI-полигоны — после базы shop + API.
