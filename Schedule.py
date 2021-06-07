import sys

class Task:
    def __init__(self,task_name,arrival_time,priority,cpu_burst):
        self.task_name = task_name
        self.arrival_time = arrival_time
        self.priority = priority
        self.cpu_burst = cpu_burst
        self.waiting_time = 0
        self.turnaround_time = 0
        self.last_executed_time = 0

def task_list(file_name):
    def isDigit(x):
        try:
            float(x)
            return True
        except ValueError:
            return False
    listed_tasks = []
    file = open(file_name,"r")
    for line in file.readlines():
        if line:
            line = line.strip().split(",")
            if len(line) == 4:
                task_name, arrival_time, priority, cpu_burst = line[0], line[1], line[2], line[3]
                if isDigit(arrival_time) and isDigit(priority) and isDigit(cpu_burst):
                    listed_tasks.append(Task(task_name,float(arrival_time),int(priority),float(cpu_burst)))

    file.close()
    return listed_tasks



def fcfs(file_name):
    tasks_by_arrival = sorted(task_list(file_name), key= lambda x: (x.arrival_time,int(x.task_name[1:])))
    file = open("output.txt","w")
    tasks = []
    time_passed = 0
    turn_around_times = []
    waiting_times = []
    while len(tasks_by_arrival) != 0:
        minimum_arrival = min([task.arrival_time for task in tasks_by_arrival])
        if time_passed < minimum_arrival:
            before_updating_time_passed = time_passed
            time_passed = minimum_arrival
            tasks.append((None, minimum_arrival - before_updating_time_passed, time_passed))
        current_task = \
                sorted([task for task in tasks_by_arrival if time_passed >= task.arrival_time],
                       key=lambda x: (x.arrival_time,int(x.task_name[1:])))[0]
        time_passed += current_task.cpu_burst
        tasks.append((current_task.task_name, current_task.cpu_burst, time_passed))
        current_task.last_executed_time = time_passed
        tasks_by_arrival.remove(current_task)
        current_task.waiting_time = sum([temp_burst for a_task, temp_burst, ttime_passed in tasks
                                         if
                                         current_task.last_executed_time >= ttime_passed and a_task != current_task.task_name]) - current_task.arrival_time
        current_task.turnaround_time = current_task.waiting_time + current_task.cpu_burst
        waiting_times.append(current_task.waiting_time)
        turn_around_times.append(current_task.turnaround_time)
        file.write(f"\nWill run name : {current_task.task_name}\n"
                   f"Priority : {current_task.priority}\n"
                   f"Burst: {current_task.cpu_burst}\n"
                   f"Task {current_task.task_name} finished.\n"
                   f"\nWaiting time for {current_task.task_name} : {current_task.waiting_time}\n"
                   f"Turnaround time for {current_task.task_name} : {current_task.turnaround_time}\n"
                   f"Finishing time for {current_task.task_name} : {current_task.last_executed_time}\n")

    file.write("\t*-*" * 8)
    file.write(f"\n\n\tAverage waiting time : {sum(waiting_times) / len(waiting_times)}"
               f"\t\n\tAverage turnaround time : {sum(turn_around_times) / len(turn_around_times)}")
    file.close()

def sjf(file_name):
    tasks_by_arrival = sorted(task_list(file_name),key= lambda x : (x.arrival_time,int(x.task_name[1:])))
    time_passed = 0
    tasks = []
    turn_around_times = []
    waiting_times = []
    file = open("output.txt","w")
    while len(tasks_by_arrival) != 0:
        minimum_arrival = min([task.arrival_time for task in tasks_by_arrival])
        if time_passed < minimum_arrival:
            before_updating_time_passed = time_passed
            time_passed = minimum_arrival
            tasks.append((None, minimum_arrival - before_updating_time_passed, time_passed))
        current_task = \
        sorted([task for task in tasks_by_arrival if time_passed >= task.arrival_time], key=lambda x: (x.cpu_burst,x.arrival_time))[0]
        time_passed += current_task.cpu_burst
        tasks.append((current_task.task_name, current_task.cpu_burst, time_passed))
        current_task.last_executed_time = time_passed
        tasks_by_arrival.remove(current_task)
        current_task.waiting_time = sum([temp_burst for a_task, temp_burst, ttime_passed in tasks
                                     if current_task.last_executed_time >= ttime_passed and a_task != current_task.task_name]) - current_task.arrival_time
        current_task.turnaround_time = current_task.waiting_time + current_task.cpu_burst
        waiting_times.append(current_task.waiting_time)
        turn_around_times.append(current_task.turnaround_time)
        file.write(f"\nWill run name : {current_task.task_name}\n"
                   f"Priority : {current_task.priority}\n"
                   f"Burst: {current_task.cpu_burst}\n"
                   f"Task {current_task.task_name} finished.\n"
                   f"\nWaiting time for {current_task.task_name} : {current_task.waiting_time}\n"
                   f"Turnaround time for {current_task.task_name} : {current_task.turnaround_time}\n"
                   f"Finishing time for {current_task.task_name} : {current_task.last_executed_time}\n"
                   )

    file.write("\t*-*" * 8)
    file.write(f"\n\n\tAverage waiting time : {sum(waiting_times)/len(waiting_times)}"
               f"\t\n\tAverage turnaround time : {sum(turn_around_times)/len(turn_around_times)}")
    file.close()



def pri(file_name):
    tasks_by_arrival = sorted([task for task in task_list(file_name) if 1 <= task.priority <= 10], key=lambda x: (x.arrival_time,int(x.task_name[1:])))
    time_passed = 0
    tasks = []
    waiting_times = []
    turn_around_times = []
    file = open("output.txt","w")
    while len(tasks_by_arrival) != 0:
        minimum_arrival = min([task.arrival_time for task in tasks_by_arrival])
        if time_passed < minimum_arrival:
            before_updating_time_passed = time_passed
            time_passed = minimum_arrival
            tasks.append((None, minimum_arrival - before_updating_time_passed, time_passed))
        current_task = \
                sorted([task for task in tasks_by_arrival if time_passed >= task.arrival_time], key=lambda x: x.priority, reverse=True)[
                    0]
        time_passed += current_task.cpu_burst
        tasks.append((current_task.task_name, current_task.cpu_burst, time_passed))
        current_task.last_executed_time = time_passed
        tasks_by_arrival.remove(current_task)
        current_task.waiting_time = sum([temp_burst for a_task, temp_burst, ttime_passed in tasks
                                         if
                                         current_task.last_executed_time >= ttime_passed and a_task != current_task.task_name]) - current_task.arrival_time
        current_task.turnaround_time = current_task.waiting_time + current_task.cpu_burst
        waiting_times.append(current_task.waiting_time)
        turn_around_times.append(current_task.turnaround_time)
        file.write(f"\nWill run name : {current_task.task_name}\n"
                   f"Priority : {current_task.priority}\n"
                   f"Burst: {current_task.cpu_burst}\n"
                   f"Task {current_task.task_name} finished.\n"
                   f"\nWaiting time for {current_task.task_name} : {current_task.waiting_time}\n"
                   f"Turnaround time for {current_task.task_name} : {current_task.turnaround_time}\n"
                   f"Finishing time for {current_task.task_name} : {current_task.last_executed_time}\n")

    file.write("\t*-*" * 8)
    file.write(f"\n\tAverage waiting time : {sum(waiting_times)/len(waiting_times)}"
                   f"\n\tAverage turnaround time : {sum(turn_around_times)/len(turn_around_times)}")
    file.close()

def rr(file_name):
    tasks_by_arrival = sorted(task_list(file_name), key=lambda x: (x.arrival_time,int(x.task_name[1:])))
    time_passed = 0
    total_bursts = {task.task_name : task.cpu_burst for task in tasks_by_arrival}
    tasks = []
    file = open("output.txt","w")
    current_list = [tasks_by_arrival[0]]
    while len(tasks_by_arrival) != 0:
        min_arrival = min([task.arrival_time for task in tasks_by_arrival])
        if time_passed < min_arrival:
            before_updating_time_passed = time_passed
            time_passed = min_arrival
            tasks.append((None, min_arrival - before_updating_time_passed, time_passed))
            current_list.extend(
                task for task in tasks_by_arrival if time_passed >= task.arrival_time and task not in current_list
                and task.last_executed_time == 0)
        current_task = current_list[0]
        if time_passed >= current_task.arrival_time:
            if current_task.cpu_burst > 10:
                        file.write(f"\nWill run name : {current_task.task_name}\nPriority : {current_task.priority}"
                                   f"\nBurst: {current_task.cpu_burst}\n")
                        current_task.cpu_burst -= 10
                        time_passed += 10
                        current_list.extend(
                            [task for task in tasks_by_arrival if time_passed >= task.arrival_time and task not in current_list])
                        file.write(f"""Task {current_task.task_name} is executed.
                                        Remaining CPU Burst: {current_task.cpu_burst}\n""")
                        current_list.remove(current_task)
                        current_list.append(current_task)
                        tasks.append((current_task, 10, time_passed))


            elif current_task.cpu_burst == 10:
                        file.write(f"\nWill run name : {current_task.task_name}\nPriority : {current_task.priority}"
                                   f"\nBurst: {current_task.cpu_burst}\n")
                        current_task.cpu_burst = 0
                        time_passed += 10
                        current_list.extend(
                            [task for task in tasks_by_arrival if time_passed >= task.arrival_time and task not in current_list])
                        tasks_by_arrival.remove(current_task)
                        current_list.remove(current_task)
                        tasks.append((current_task, 10, time_passed))
                        current_task.last_executed_time = time_passed
                        file.write(f"""Task {current_task.task_name} finished
                                       Remaining CPU Burst : {current_task.cpu_burst}\n"""
                                   )


            else:
                time_passed += current_task.cpu_burst
                file.write(f"\nWill run name : {current_task.task_name}\nPriority : {current_task.priority}"
                           f"\nBurst: {current_task.cpu_burst}\n")
                current_list.extend(
                    [task for task in tasks_by_arrival if
                     time_passed >= task.arrival_time and task not in current_list])
                tasks_by_arrival.remove(current_task)
                current_list.remove(current_task)
                tasks.append((current_task, current_task.cpu_burst, time_passed))
                current_task.last_executed_time = time_passed
                current_task.cpu_burst = 0
                file.write(f"""Task {current_task.task_name} finished
                                                       Remaining CPU Burst : {current_task.cpu_burst}\n""")

    turn_around_times = []
    waiting_times = []
    for task in set([task for task, temp_burst, time_passed in tasks if task is not None]):
        task.waiting_time = sum([temp_burst for a_task, temp_burst, ttime_passed in tasks
                             if task.last_executed_time >= ttime_passed and (a_task is None or a_task.task_name != task.task_name)]) - task.arrival_time
        task.turnaround_time = task.waiting_time + total_bursts[task.task_name]
        turn_around_times.append(task.turnaround_time)
        waiting_times.append(task.waiting_time)
        file.write(f"""Waiting time for {task.task_name} : {task.waiting_time}\n""")
        file.write(f"""Turnaround time for {task.task_name} : {task.turnaround_time}\n"""
                   f"Finishing time for {task.task_name} : {task.last_executed_time}\n")
    file.write("\t*-*" * 8)
    file.write(f"\nAverage waiting time : {sum(waiting_times)/len(waiting_times)}"
               f"\nAverage turnaround time : {sum(turn_around_times)/len(turn_around_times)}")
    file.close()




def pri_rr(file_name):
        tasks_by_arrival = sorted([task for task in task_list(file_name) if 1 <= task.priority <= 10], key=lambda x: (x.arrival_time,int(x.task_name[1:])))
        time_passed = 0
        total_bursts = {task.task_name : task.cpu_burst for task in tasks_by_arrival}
        tasks = []
        current_list = [task for task in tasks_by_arrival if time_passed >= task.arrival_time]
        file = open("output.txt", "w")
        while len(tasks_by_arrival) != 0:
            min_arrival = min([task.arrival_time for task in tasks_by_arrival])
            if time_passed < min_arrival:
                before_updating_time_passed = time_passed
                time_passed = min_arrival
                current_list.extend(task for task in tasks_by_arrival if time_passed >= task.arrival_time and task not in current_list
                                    and task.last_executed_time == 0)
                tasks.append((None,min_arrival - before_updating_time_passed,time_passed))
            current_task = \
                sorted([task for task in current_list],
                       key=lambda x: (x.priority), reverse=True)[
                   0]
            if [task.priority for task in current_list].count(current_task.priority) == 10:
                    temp = [task for task in tasks_by_arrival if time_passed < task.arrival_time < time_passed +
                                current_task.cpu_burst and task.priority > current_task.priority]
                    if temp:
                        if current_task.cpu_burst >= 10 and time_passed + 10 <= temp[0].arrival_time:
                            if current_task.cpu_burst > 10:
                                file.write(f"\nWill run name : {current_task.task_name}\nPriority : {current_task.priority}"
                                           f"\nBurst: {current_task.cpu_burst}\n")
                                current_task.cpu_burst -= 10
                                time_passed += 10
                                current_list.extend(
                                    [task for task in tasks_by_arrival if
                                     time_passed >= task.arrival_time and task not in current_list])
                                file.write(f"""Task {current_task.task_name} is executed
                                            Remaining CPU Burst : {current_task.cpu_burst}\n""")
                                current_list.remove(current_task)
                                current_list.append(current_task)
                                tasks.append((current_task, 10, time_passed))
                            elif current_task.cpu_burst == 10:
                                file.write(
                                    f"\nWill run name : {current_task.task_name}\nPriority : {current_task.priority}"
                                    f"\nBurst: {current_task.cpu_burst}\n")
                                current_task.cpu_burst -= 10
                                time_passed += 10
                                current_list.extend(
                                    [task for task in tasks_by_arrival if
                                     time_passed >= task.arrival_time and task not in current_list])
                                file.write(f"""Task {current_task.task_name} finished
                                            Remaining CPU Burst : {current_task.cpu_burst}\n""")
                                current_list.remove(current_task)
                                tasks_by_arrival.remove(current_task)
                                tasks.append((current_task, 10, time_passed))

                        else:

                                    first_time_passed = time_passed
                                    file.write(
                                        f"\nWill run name : {current_task.task_name}\nPriority : {current_task.priority}"
                                        f"\nBurst: {current_task.cpu_burst}\n")
                                    time_passed = temp[0].arrival_time
                                    current_list.extend(
                                            [task for task in tasks_by_arrival if
                                             time_passed >= task.arrival_time and task not in current_list])
                                    current_list.remove(current_task)
                                    current_list.append(current_task)
                                    tasks.append((current_task, temp[0].arrival_time - first_time_passed, time_passed))
                                    current_task.cpu_burst -= temp[0].arrival_time - first_time_passed
                                    file.write(f"""Task {current_task.task_name} is executed
                                                Remaining CPU Burst : {current_task.cpu_burst}\n""")
                    else:

                            time_passed += current_task.cpu_burst
                            file.write(f"\nWill run name : {current_task.task_name}\nPriority : {current_task.priority}"
                                       f"\nBurst: {current_task.cpu_burst}\n")
                            current_list.extend(
                                [task for task in tasks_by_arrival if
                                 time_passed >= task.arrival_time and task not in current_list])
                            tasks_by_arrival.remove(current_task)
                            current_list.remove(current_task)
                            tasks.append((current_task, current_task.cpu_burst, time_passed))
                            current_task.last_executed_time = time_passed
                            current_task.cpu_burst = 0
                            file.write(f"""Task {current_task.task_name} finished
                                       Remaining CPU Burst : {current_task.cpu_burst}\n""")
            elif [task.priority for task in current_list].count(current_task.priority) >= 2:
                temp_list = [task for task in current_list if task.priority == current_task.priority]
                while len(temp_list) != 0 and max([task.priority for task in temp_list]) >= max([task.priority for task in tasks_by_arrival if time_passed >= task.arrival_time]):
                    temp_task = temp_list[0]
                    check_task = [task[0] for task in tasks if isinstance(task[0],Task) and task[0].priority == temp_task.priority]
                    if len(temp_list) >= 2 and check_task and check_task[len(check_task)-1] == temp_task:
                        temp_task = temp_list[1]
                    temp = [task for task in tasks_by_arrival if time_passed < task.arrival_time < time_passed +
                            current_task.cpu_burst and task.priority > current_task.priority]

                    if len(temp_list) != 1:

                        if temp:
                            if temp_task.cpu_burst >= 10 and time_passed + 10 <= temp[0].arrival_time:
                                if temp_task.cpu_burst > 10:
                                    file.write(
                                        f"\nWill run name : {temp_task.task_name}\nPriority : {temp_task.priority}"
                                        f"\nBurst: {temp_task.cpu_burst}\n")
                                    temp_task.cpu_burst -= 10
                                    time_passed += 10
                                    current_list.extend(
                                        [task for task in tasks_by_arrival if
                                         time_passed >= task.arrival_time and task not in current_list])
                                    file.write(f"""Task {temp_task.task_name} is executed
                                                Remaining CPU Burst : {temp_task.cpu_burst}\n""")
                                    current_list.remove(temp_task)
                                    current_list.append(temp_task)
                                    tasks.append((temp_task, 10, time_passed))
                                elif temp_task.cpu_burst == 10:
                                    file.write(
                                        f"\nWill run name : {temp_task.task_name}\nPriority : {temp_task.priority}"
                                        f"\nBurst: {temp_task.cpu_burst}\n")
                                    temp_task.cpu_burst -= 10
                                    time_passed += 10
                                    current_list.extend(
                                        [task for task in tasks_by_arrival if
                                         time_passed >= task.arrival_time and task not in current_list])
                                    file.write(f"""Task {temp_task.task_name} finished
                                                Remaining CPU Burst : {temp_task.cpu_burst}\n""")
                                    current_list.remove(temp_task)
                                    tasks_by_arrival.remove(temp_task)
                                    tasks.append((temp_task, 10, time_passed))

                            else:
                                file.write(
                                    f"\nWill run name : {temp_task.task_name}\nPriority : {temp_task.priority}"
                                    f"\nBurst: {temp_task.cpu_burst}\n")
                                first_time_passed = time_passed
                                time_passed = temp[0].arrival_time
                                current_list.extend(
                                    [task for task in tasks_by_arrival if
                                     time_passed >= task.arrival_time and task not in current_list])
                                current_list.remove(temp_task)
                                current_list.append(temp_task)
                                tasks.append((temp_task, temp[0].arrival_time - first_time_passed, time_passed))
                                temp_task.cpu_burst -= temp[0].arrival_time - first_time_passed
                                file.write(f"""Task {temp_task.task_name} is executed
                                            Remaining CPU Burst : {temp_task.cpu_burst}\n""")

                        else:
                            if temp_task.cpu_burst > 10:
                                file.write(
                                    f"\nWill run name : {temp_task.task_name}\nPriority : {temp_task.priority}"
                                    f"\nBurst: {temp_task.cpu_burst}\n")
                                temp_task.cpu_burst -= 10
                                time_passed += 10
                                current_list.extend(
                                    [task for task in tasks_by_arrival if
                                     time_passed >= task.arrival_time and task not in current_list])
                                file.write(f"""Task {temp_task.task_name} is executed
                                            Remaining CPU Burst : {temp_task.cpu_burst}\n""")
                                temp_list.remove(temp_task)
                                temp_list.append(temp_task)
                                tasks.append((temp_task, 10, time_passed))

                            elif temp_task.cpu_burst == 10:
                                file.write(
                                    f"\nWill run name : {temp_task.task_name}\nPriority : {temp_task.priority}"
                                    f"\nBurst: {temp_task.cpu_burst}\n")
                                temp_task.cpu_burst = 0
                                time_passed += 10
                                current_list.extend(
                                    [task for task in tasks_by_arrival if
                                     time_passed >= task.arrival_time and task not in current_list])
                                file.write(f"""Task {temp_task.task_name} finished
                                            Remaining CPU Burst : {temp_task.cpu_burst}\n""")
                                temp_list.remove(temp_task)
                                tasks_by_arrival.remove(temp_task)
                                current_list.remove(temp_task)
                                tasks.append((temp_task, 10, time_passed))
                                temp_task.last_executed_time = time_passed

                            else:
                                file.write(
                                    f"\nWill run name : {temp_task.task_name}\nPriority : {temp_task.priority}"
                                    f"\nBurst: {temp_task.cpu_burst}\n")
                                time_passed += temp_task.cpu_burst
                                current_list.extend(
                                    [task for task in tasks_by_arrival if
                                     time_passed >= task.arrival_time and task not in current_list])
                                temp_list.remove(temp_task)
                                tasks_by_arrival.remove(temp_task)
                                current_list.remove(temp_task)
                                tasks.append((temp_task, temp_task.cpu_burst, time_passed))
                                temp_task.cpu_burst = 0
                                temp_task.last_executed_time = time_passed
                                file.write(f"""Task {temp_task.task_name} finished
                                            Remaining CPU Burst : {temp_task.cpu_burst}\n""")
                    else:
                        file.write(f"\nWill run name : {temp_task.task_name}\nPriority : {temp_task.priority}"
                                   f"\nBurst: {temp_task.cpu_burst}\n")
                        time_passed += temp_task.cpu_burst
                        current_list.extend(
                            [task for task in tasks_by_arrival if
                             time_passed >= task.arrival_time and task not in current_list])
                        temp_list.remove(temp_task)
                        tasks_by_arrival.remove(temp_task)
                        current_list.remove(temp_task)
                        tasks.append((temp_task, temp_task.cpu_burst, time_passed))
                        temp_task.cpu_burst = 0
                        temp_task.last_executed_time = time_passed
                        file.write(f"""Task {temp_task.task_name} finished
                                    Remaining CPU Burst : {temp_task.cpu_burst}\n""")



                    new_comers = ([task for task in tasks_by_arrival if time_passed < task.arrival_time < time_passed + temp_task.cpu_burst and task.priority == temp_task.priority and task not in temp_list])
                    if new_comers:
                        temp_list.extend(new_comers)
        turn_around_times = []
        waiting_times = []
        for task in set([task for task, temp_burst, time_passed in tasks if task is not None]):
            task.waiting_time = sum([temp_burst for a_task, temp_burst, ttime_passed in tasks
                                     if
                                     task.last_executed_time >= ttime_passed and (a_task is None or a_task.task_name != task.task_name) ]) - task.arrival_time
            task.turnaround_time = task.waiting_time + total_bursts[task.task_name]
            turn_around_times.append(task.turnaround_time)
            waiting_times.append(task.waiting_time)
            file.write(f"""Waiting time for {task.task_name} : {task.waiting_time}\n""")
            file.write(f"""Turnaround time for {task.task_name} : {task.turnaround_time}\n"""
                       f"Finishing time for {task.task_name} : {task.last_executed_time}\n")
        file.write(f"\nAverage waiting time : {sum(waiting_times) / len(waiting_times)}"
                   f"\nAverage turnaround time : {sum(turn_around_times) / len(turn_around_times)}")
        file.close()


def srtf(file_name):
    tasks_by_arrival = sorted(task_list(file_name), key=lambda x: (x.arrival_time,int(x.task_name[1:])))
    time_passed = 0
    total_bursts = {task.task_name: task.cpu_burst for task in tasks_by_arrival}
    tasks = []
    file = open("output.txt","w")
    while len(tasks_by_arrival) != 0:
        min_arrival = min([task.arrival_time for task in tasks_by_arrival])
        if time_passed < min_arrival:
            before_updating_time_passed = time_passed
            time_passed = min_arrival
            tasks.append((None, min_arrival - before_updating_time_passed, time_passed))
        current_task = \
            sorted([task for task in tasks_by_arrival if time_passed >= task.arrival_time],
                   key=lambda x: x.cpu_burst)[
                0]

        temp = sorted([task for task in tasks_by_arrival if time_passed < task.arrival_time < time_passed +
                current_task.cpu_burst and task.cpu_burst < current_task.cpu_burst],key = lambda x : (x.arrival_time, x.cpu_burst))
        if temp:
            file.write(
                f"\nWill run name : {current_task.task_name}\nPriority : {current_task.priority}"
                f"\nBurst: {current_task.cpu_burst}\n")
            first_time_passed = time_passed
            time_passed = temp[0].arrival_time
            tasks.append((current_task, temp[0].arrival_time - first_time_passed, time_passed))
            current_task.cpu_burst -= temp[0].arrival_time - first_time_passed
            file.write(f"""Task {current_task.task_name} is executed
                        Remaining CPU Burst : {current_task.cpu_burst}\n""")
        else:
            file.write(
                f"\nWill run name : {current_task.task_name}\nPriority : {current_task.priority}"
                f"\nBurst: {current_task.cpu_burst}\n")
            time_passed += current_task.cpu_burst
            tasks_by_arrival.remove(current_task)
            tasks.append((current_task, current_task.cpu_burst, time_passed))
            current_task.last_executed_time = time_passed
            current_task.cpu_burst = 0
            file.write(f"""Task {current_task.task_name} finished
                        Remaining CPU Burst : {current_task.cpu_burst}\n""")
    turn_around_times = []
    waiting_times = []
    for task in set([task for task, temp_burst, time_passed in tasks if task is not None]):
        task.waiting_time = sum([temp_burst for a_task, temp_burst, ttime_passed in tasks
                                     if
                                     task.last_executed_time >= ttime_passed and (
                                                 a_task is None or a_task.task_name != task.task_name)]) - task.arrival_time
        task.turnaround_time = task.waiting_time + total_bursts[task.task_name]
        turn_around_times.append(task.turnaround_time)
        waiting_times.append(task.waiting_time)
        file.write(f"""Waiting time for {task.task_name} : {task.waiting_time}\n""")
        file.write(f"""Turnaround time for {task.task_name} : {task.turnaround_time}\n"""
                   f"Finishing time for {task.task_name} : {task.last_executed_time}\n")
    file.write(f"\nAverage waiting time : {sum(waiting_times) / len(waiting_times)}\n"
               f"Average turnaround time : {sum(turn_around_times) / len(turn_around_times)}")
    file.close()


try:
    eval(f"{sys.argv[1]}('{sys.argv[2]}')")
except:
    print("There was a problem about the name of the file or the algorithm you choose."
          "Algorithms: fcfs, sjf, pri, rr, pri_rr, srtf ")



# YUSUF EREN KAYA 190709054
































