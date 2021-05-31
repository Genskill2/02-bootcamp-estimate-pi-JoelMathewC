import math
import unittest
import random

def wallis(val):
    prod = 1.0
    for i in range(1,val+1):
        num = 4 * (i**2)
        denom = num - 1
        prod *= float(num/denom)
    return 2*prod


def monte_carlo(val):

    num_sq = 0
    num_c = 0
    
    for i in range(0,val):
        x = random.uniform(0,1)
        y = random.uniform(0,1)


        res = ((x**2) + (y**2))**(1/2)

        if res <= 1:
            num_c += 1
        else:
            num_sq += 1

    return float(4*num_c/num_sq)




class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
