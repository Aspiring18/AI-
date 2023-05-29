def job_scheduling(J, D, P):
    # Sort jobs in decreasing order of profit
    jobs = sorted(zip(J, D, P), key=lambda x: x[2], reverse=True)

    scheduled_jobs = []  # Set of scheduled jobs
    total_profit = 0  # Total profit earned

    # Schedule each job
    slots = set(range(1, max(D) + 1))  # Available slots
    for job in jobs:
        job_name, deadline, profit = job

        # Schedule the job if a feasible slot is available
        if deadline in slots:
            scheduled_jobs.append((job_name, deadline))
            total_profit += profit
            slots.remove(deadline)

        # Stop scheduling if no more slots are available
        if not slots:
            break

    return scheduled_jobs, total_profit

# Take user input for jobs, deadlines, and profits
num_jobs = int(input("Enter the number of jobs: "))
J = []
D = []
P = []
for i in range(num_jobs):
    job_name = input(f"Enter the name of job {i+1}: ")
    deadline = int(input(f"Enter the deadline for job {i+1}: "))
    profit = int(input(f"Enter the profit for job {i+1}: "))
    J.append(job_name)
    D.append(deadline)
    P.append(profit)

# Perform job scheduling
scheduled_jobs, total_profit = job_scheduling(J, D, P)

# Print the scheduled jobs and total profit
print("Scheduled Jobs:")
for job in scheduled_jobs:
    print(f"Job: {job[0]}, Deadline: {job[1]}")
print("Total Profit:", total_profit)
