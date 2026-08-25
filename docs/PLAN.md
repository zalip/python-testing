# План: автотесты на Python (pytest)

Объект: мини-магазин (`src/shop`) — цена, корзина, склад.

## База (обязательно)

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

## Следующий слой (после базы)

| # | Тема | Зачем |
|---|------|-------|
| 10 | Свой API (FastAPI/Flask) + httpx/TestClient | HTTP-тесты без браузера |
| 11 | БД в тестах | фикстура БД, транзакции, изоляция |
| 12 | Property-based (hypothesis) | генерация входов |
| 13 | Markers + selective run | @pytest.mark.slow, -m |

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

Порядок опционального: **Actions (или Jenkins) → отчёт JUnit → Docker**. UI — в самом конце или отдельно.