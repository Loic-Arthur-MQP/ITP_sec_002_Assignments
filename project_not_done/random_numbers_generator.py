# Your first name: Loic Arthur
# Your section: 0002 

import random
import matplotlib.pyplot as plt

# Write your functions with their docstrings here

# nextMiddleSquare
def next_middle_square(num1 : float, num2: float) -> float:


# listMiddleSquare
def list_middle_squares(seed: float):
    next_middle_squre(1,2)
    return None

   
# nextLehmer
def nextlehmer(a : float , b ; int, r_num: float) -> float:
    new_r_num = a * (r_num % m)

# listLehmer
def list_lehme(a: int, m:int):
    return None


# listRandom
def list_random():
    random.

def chartRandomNumbers(mid, lehmer, rand):
  '''
  This function draws a histogram of the three lists on the same plot
  :param mid: a list of random numbers from middle squares
  :param lehmer: a list of random numbers from lehmer
  :param rand: a list of random numbers from Python random module
  '''
  multi = [mid, lehmer, rand]
  plt.hist(multi, histtype='bar', label=['middle square', 'lehmer', 'random module'])
  plt.legend(prop={'size': 10})
  plt.show()
  


def main():
  start = 29
  list1 = listMiddleSquare(start)
  list2 = listLehmer(start)
  list3 = listRandom()
  chartRandomNumbers(list1, list2, list3)

if __name__ == "__main__":
  main()
