import pytest
from selene.support.shared import config


@pytest.fixture
def set_options_in_browser():
    config.base_url = 'https://demoqa.com/'
    config.window_width = 1920
    config.window_height = 1080
