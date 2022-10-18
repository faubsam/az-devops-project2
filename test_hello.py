from hello import toyou, add, subtract

def setup_function(function):
    print("Running setup: %s" % function.__name__)
    function.x = 10
    
def teardown_function(function):
    print("Tearing down: %s" % function.__name__)
    del function.x
    
def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9
    
def test_hello_add():
    assert add(test_hello_add.x) == 11