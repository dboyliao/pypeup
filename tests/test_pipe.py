from pypipe import DataPipe

class MyPipe(DataPipe):

    def add(self, to_add):
        return self.data + to_add

    def sub(self, to_substract):
        return self.data - to_substract


pipe = MyPipe(3)

def test_pipe():

    pipe.add(1).sub(5).add(6)

    assert pipe.data == 5

class MyPipe2(DataPipe):
    pass

pipe2 = MyPipe2(5)

def my_fun(data, x, y = 1):
    return data + 3 * x - 2 * y

def test_register():

    pipe2.register(my_fun)
    pipe2.my_fun(3, 6)

    assert pipe2.data == 2

def test_default_value():
    pipe2.my_fun(1)

    assert pipe2.data == 3

try:
    import numpy as np

    class NpPipe(DataPipe):

        def add(self, x):
            return self.data + x

        def flat(self):
            return self.data.flatten()

        def mul(self, a):
            return self.data * a

    def test_np_array():
        np_pipe = NpPipe(np.array([[1, 2], [3, 4]]))

        np_pipe.add(5).flat().mul(3)

        assert np.allclose(np_pipe.data, np.array([18, 21, 24, 27]))
        
except ImportError:
    print "In order to test the all functionality, "
    print "it is recommended to install numpy first. "
    print "But if you don't care about it, just ignore these messages."

