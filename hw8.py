import time
import unittest

def measure_time(function, *args, **kwargs):
    start = time.time()
    result = function(*args, **kwargs)
    return result, time.time() - start

def sample_function(i):
    time.sleep(i)
    return i

class TestMeasureTime(unittest.TestCase):
    def test_execution_time(self):
        result, exect_time = measure_time(sample_function, 1)
        self.assertEqual(result, 1)
        self.assertTrue(0.9 <= exect_time <= 1.1)

if __name__ == "__main__":
    unittest.main()
