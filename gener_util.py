import time
from log_tools import logged

log_dir = 'log/'

@logged(log_dir)
def gener_listfromlists(outerlist):
    for item in outerlist:
        if isinstance(item, list):
            for inner_item in gener_listfromlists(item):
                yield inner_item
        else:
            yield item


