import pytest
from selenium import webdriver
from config import Config
import pytest_html

@pytest.fixture(scope="function")
def driver(request):
    """Sets up the driver instance and exposes it to the reporting hooks."""
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    
    # Attach driver to the running test node so the HTML hook can see it
    request.node.funcargs['driver'] = driver
    
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Pytest hook to capture screenshots and attach them to the HTML report."""
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    # Capture screenshots during the 'call' phase (when the actual test runs)
    if report.when == "call":
        driver = item.funcargs.get("driver")
        if driver:
            # Take base64 screenshot to embed directly into the HTML document
            screenshot = driver.get_screenshot_as_base64()
            html = f'<div><img src="data:image/png;base64,{screenshot}" alt="screenshot" style="width:600px;height:auto;"/></div'
            extra.append(pytest_html.extras.html(html))
            report.extra = extra
