from nose.tools import assert_equal
def get_string(x,y):
    return str(x)+ str(y)

assert_equal(get_string(4, 5), '45')
print("Passed")

