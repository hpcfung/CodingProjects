import sys, re

def check_file(file_name):
    file1 = open(file_name, 'r')
    Lines = file1.readlines()

    for i, line in enumerate(Lines):
        # print(repr(line)) # \n is printed literally
        if line.startswith("Starting task"):
            print(line[9:-1]) # \n is not printed (counted as 1 char)
            task_num = int(re.search(r"[a-zA-Z\s]*([0-9]*)\n", line).group(1))
            job_list[task_num] = True # this job is present

        for error_word in error_keywords_list:
            if error_word.casefold() in line.casefold():
                print(file_name)
                print(repr(line))
                sys.exit()

    last_line = Lines[-1]
    if last_line.startswith("qmc program") and last_line.endswith("completed\n"):
        print(repr(last_line))
    else:
        print("program incomplete:")
        print(repr(last_line))
        sys.exit()


if __name__ == "__main__":
    """
    cd qmc_test
    module load python/3.10
    python checking.py

    - Checks that the last line in .out is of the form qmc program ... completed
    - Looks for error keywords in error_keywords_list
    - Also checks that all 270 jobs are present
        - if one is missing, throws FileNotFoundError

    Error examples:
    slurmstepd: error: *** JOB 6800453 ON gra812 CANCELLED AT 2023-05-26T02:17:00 DUE TO TIME LIMIT ***
    slurmstepd: error: Detected 1 oom-kill event(s) in StepId=6800197.batch. Some of your processes may have been killed by the cgroup out-of-memory handler.
    
    Protocol: For each L,
    """

    job_id = 7228219
    job_num = 270
    job_name = "out/7228219/L11_prod_test-" # "L20_prod_test-"

    error_keywords_list = ["slurmstepd", "error", "CANCEL", "LIMIT", "kill"]

    job_list = [False] * job_num
    for k in range(job_id,job_id+job_num):
        check_file(file_name=job_name+str(k)+".out")
        # sys.exit() # first .out only
    
    if all(job_list):
        print(f"All {job_num} tasks are present.")
    else:
        missing_jobs = [ID for ID in range(job_num) if job_list[x] == False]
        print(f"Missing tasks = {missing_jobs}")
    print("All programs are complete. No error keywords found.")
