import pytest
import logging
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

@pytest.fixture
def browser(request):
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    logging.info("Launched Chrome browser")

    yield driver

    # On test failure, capture screenshot
    if request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"screenshots/{request.node.name}_{timestamp}.png"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        driver.save_screenshot(filename)
        logging.error(f"Test failed — screenshot saved to {filename}")

    driver.quit()
    logging.info("Closed Chrome browser")

# Add test outcome hook
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
