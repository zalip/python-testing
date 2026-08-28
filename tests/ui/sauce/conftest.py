# pytest-playwright читает это через ini/CLI;
# программно часто так:
import pytest
from config import BASE

# @pytest.fixture(scope="session")
# def browser_type_launch_args():
#    return {"headless": True}


@pytest.fixture
def page(page):
    page.goto(BASE)
    return page
