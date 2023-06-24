import sys

def check_file(file_name):
    file1 = open(file_name, 'r')
    Lines = file1.readlines()

    last_line = Lines[-1]
    if last_line.startswith("qmc program") and last_line.endswith("completed\n"):
        print(repr(last_line))
    else:
        print("program incomplete:")
        print(repr(last_line))
        sys.exit()

    for i, line in enumerate(Lines):
        # print(repr(line)) # \n is printed literally
        for error_word in error_keywords_list:
            if error_word.casefold() in line.casefold():
                print(file_name)
                print(repr(line))
                sys.exit()

if __name__ == "__main__":
    """
    cd qmc_test
    module load python/3.10
    python checking.py

    slurmstepd: error: *** JOB 6800453 ON gra812 CANCELLED AT 2023-05-26T02:17:00 DUE TO TIME LIMIT ***
    slurmstepd: error: Detected 1 oom-kill event(s) in StepId=6800197.batch. Some of your processes may have been killed by the cgroup out-of-memory handler.
    """

    job_id = 7228219
    job_num = 270
    job_name = "L11_prod_test-"

    error_keywords_list = ["slurmstepd", "error", "CANCEL", "LIMIT", "kill"]

    for k in range(job_id,job_id+job_num):
        check_file(file_name=job_name+str(k)+".out")
        # sys.exit() # first .out only
    print("All programs are complete. No error keywords found.")
