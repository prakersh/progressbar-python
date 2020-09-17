import time
from progress_bar import update_progress
def test():
    for i in range(11):
        update_progress(i, 10)
        time.sleep(1)
test()
