import time
from control import Controller

ctrl = Controller()


ctrl.open_calendar()
time.sleep(2)
ctrl.switch_to_next_recent_app()
