from sys import argv
from random import random
from math import sqrt

def handle_input():
    ''' This function handles the inputs passed by the user
        returns:
            num_trials: int - number of trials to be completed
            num_pairs: int - number of random pairs to be generated for each trial
                             with a default value of 1000'''
    
    default_num_rands = 1000
    
    if len(argv)<2:
        print("Please pass a number of trials\n" +
              "You may also pass a number of random pairs per trial if you " +
              "want someting other than the default of " + str(default_num_rands) + ".")
        exit(0)
    elif len(argv) == 2:
        print("Will use " + str(default_num_rands) + " per trial. Specify something else after the number of trials if desired.")
        num_pairs = default_num_rands
    else: num_pairs = int(argv[2])
    num_trials = int(argv[1])

    return num_trials, num_pairs

def in_circle(x:"int in [0,1]", y:"int in [0,1]"):
    '''Takes in coordinates x and y, which should both be in [0, 1]
       and evaulates if this (x,y) is within a circle of radius 1 centered at (0,0)
       returns:
           0 if (x,y) not in circle
           1 if (x,y) is in the circle or its boundary
    '''
    if sqrt(x**2 + y**2) <= 1:
        return 1
    else: return 0 

def do_trials(trials:int, N:int):
    '''Takes in the number of trials to be completed and the number of pairs per trial
       and finds the estimate of the area of a quarter circle of radius 1 in the square region 
       with corners at (0,0), (0,1), (1,0), (1,1)
       returns:
           outcomes: array of ints - array of estimates, with one for each trial
    '''
    outcomes = [0]*trials
    for i in range(trials):
        trial_sum = 0
        for j in range(N):
            trial_sum += in_circle(random(), random())
        outcomes[i] = 4*trial_sum/N
    return outcomes

def do_stats(outcomes:"output from do_trials"):
    '''Takes in the outcomes from do_trials and computes
    the mean and standard deviation of the estimates
    returns:
        mean: float - mean of the samples in outcomes
        stdev: float - standard deviation of the samples in outcomes
    '''
    mean = sum(outcomes)/trials
    stdev = 0
    for i in range(trials):
        stdev += (outcomes[i] - mean)**2
    stdev = sqrt(stdev/(trials-1))
    return mean, stdev

if __name__ == '__main__':

    trials, N = handle_input()

    outcomes = do_trials(trials, N)
    
    mean, stdev = do_stats(outcomes)
    
    print(f"Result: "+str(mean)+"+-"+str(stdev))
    quit(0)
