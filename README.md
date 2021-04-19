# cpu_scheduling_algorithms_implementation_with_python


EXPLANATION OF THE PROGRAMMING ASSIGNMENT OF THE OPERATING SYSTEMS CLASS

Since I've used eval function in the program, pri-rr parameter should be passed as pri_rr.

READING THE DATA FROM THE FILE:
If the line format is not including 4 items separated by 3 commas, it won't be taken into account. (No matter if there are spaces or no space between the commas and the items.)
Later on, there is a function inside the reading function, to determine if the parameter values of the task are numbers such as decimal or integer. Exception for the task name.
Under all these conditions are passed, Each line of the data will belong to a task. TASKS WITH THE PRIORITIES THAT ARE NOT IN THE INTERVAL OF 1 AND 10 WILL BE ADDED
BUT WON'T BE TAKEN INTO ACCOUNT IN PRI AND PRI-RR ALGORITHMS.


GENERAL VARIABLES:

tasks_by_arrival = getting the listed task data read from the file, called for each of the algorithm functions. Sorted by the arrival time, but in some algorithms,
it can be sorted as priority, cpu burst depending on the kind of algorithm. 

tasks = adding the all records of run of the processes in order as if a gantt chart. Also appending what time and how much there is no process to calculate the
waiting times of the processes comprehensively, especially on the round-robin and pri-rr algorithms. (Also the idle time intervals will be appended to this list,
but their Task class object will be None. since there is no object on this interval.)

turn_around_times and waiting_times = to list all the waiting and turn_around_times of the processes, in order to calculate the
average of those.

time_passed = a time implementation to handle the processes easily.

minimum_arrival = getting the minimum arrival time of the process in the tasks_by_arrival list. If it is bigger than time_passed, it will be the new time_passed value.
And the number between time_passed and minimum_arrival will be the idle time being appended to the tasks list.

current_task = used in while loop in order to determine the task that will be run currently. It can be chosen depending on the kind of algorithm.

current_list = Will be used in only rr and pri-rr algorithms, in order to handle the context switches between the tasks easily.

temp = Used in pri-rr and srtf in order to determine while the process is being run, will be a switch to another task with the higher priority or shortest burst time
depending on the algorithm.

temp_list = Used in pri-rr. In order to implement the processes which have the same equality in a round-robin fashion.





FCFS ALGORITHM:

fcfs function gets the name or the path of the text file that is going to be used at extracting the data of the processes. At first, a list of whole the processes are
going to be held sorted by arrival times of the processes. And if some of the processes' arrival times are equivalent, under this condition, by any means, the processes
are going to be aligned at their task number. Such as "T1", "T2" in this case, T1 will come before the T2.



SJF ALGORITHM:
In addition to the FCFS algorithm, in this algorithm, there is a while loop that will be held until all of the processes are removed from the tasks_by_arrival list. 
If there is no process to be run at the time passed, time_passed will be updated to the arrival time of the process which has the smallest. 

PRI ALGORITHM:
Nothing different from the SJF besides the rules of the algorithm.


RR ALGORITHM:
With a while loop, from the tasks_by_arrival it implements one by one the processes that arrived, with a time quantum. If one of the process has completed its first
execution with a time quantum, at the time that it will be executed again, under the condition that there is a new-comer at the same time, then the new-comer one
will first go ahead.

PRI-RR ALGORITHM:
In a list which including the tasks with the equivalent priority, under the condition that if there is a new-comer task with a higher priority, if it's only in the list, it
will execute to completion. After that if no task is not arrived again, then the task of the previous list will be executed again, but the last executed one won't be the one
that run first. So it will be tracing an order even if there is a corruption with a higher priority execution.

SRTF ALGORITHM:
Similar implementations with PRI-RR and SJF. Nothing different.


Program will be run from the command line.
It uses an eval function to read the arguments from the command line and run the program.





YUSUF EREN KAYA
