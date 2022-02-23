def test_1():
    x = 100
    assert(x < 200)


def test_2():
    x = 10
    assert x == 10


def test_3(): 
	sum = 0
	for i in range(100000):
		sum += i
	assert(sum > 10000000)




