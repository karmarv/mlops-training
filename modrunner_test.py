from modrunner import operate, progress_sleep


def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 10
    function.y = 20


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x
    del function.y


### Run to see failed test
#def test_hello_add():
#    assert add(test_hello_add.x) == 12

def test_modrunner_sum():
    assert operate(test_modrunner_sum.x, test_modrunner_sum.y, "sum") == 30