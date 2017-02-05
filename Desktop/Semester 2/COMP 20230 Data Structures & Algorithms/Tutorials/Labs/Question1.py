import time

#    Algorithm to be tested
def function_1(n):
    for i in range (11):    #    1 x operation, n times
        return(i * n)        #    2 x operations? (calculation and print)
        
#     Function used to time the algorithm using values of n from 1 to 10,000
for n in range(1, 10000, 100):
    
    t1 = time.time()    #    Algorithm start time
    function_1(n)       #    Function being timed
    t2 = time.time()    #    Algorithm end time
    
    run_time = t2 - t1  #    Total algorithm run time
    
    fileHandle = open('Lab1.csv', 'a')
    print(n, ',', run_time)    #    Print in CSV format
    fileHandle.write(n)
    fileHandle.close()
    
    
    
    