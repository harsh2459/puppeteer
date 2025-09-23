from .stealth_config import get_stealth_driver
from .humanizer import human_type, human_click, random_delay, random_scroll
from ai.adaptive_behavior import AdaptiveBehavior

class PhantomBot:
    def __init__(self, proxy=None, user_agent=None):
        self.proxy = proxy
        self.user_agent = user_agent
        self.driver = None
        self.adaptive_behavior = AdaptiveBehavior()
        self.operation_start_time = None

    def launch_browser(self):
        self.driver = get_stealth_driver(proxy=self.proxy, user_agent=self.user_agent)
        self.operation_start_time = time.time()
        return self.driver

    def human_click(self, element):
        human_click(self.driver, element)

    def human_type(self, element, text):
        human_type(element, text)

    def random_delay(self, min_sec=None, max_sec=None):
        random_delay(min_sec, max_sec)

    def random_scroll(self):
        random_scroll(self.driver)

    def record_success(self, success, actions_count):
        duration = time.time() - self.operation_start_time
        self.adaptive_behavior.record_operation(success, duration, actions_count)

    def quit(self):
        if self.driver:
            self.driver.quit()
            self.driver = None