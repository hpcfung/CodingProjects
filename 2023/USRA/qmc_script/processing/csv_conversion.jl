using FileIO
using DelimitedFiles

"""
feed to script of this form
https://github.com/PIQuIL/EssiQQurke/tree/main/data
"""
function save_as_csv(bin_path) # eg batch_01_samples.bin
    # read!(samples_file_path, falses(num_spins, num_measurements)
    arr = read!(bin_path, falses(25, 100000))
    println(typeof(arr)) # BitMatrix
    println(size(arr)) # (25, 100000)

    # println(arr)
    # println(typeof(Int.(permutedims(arr))))
    # println(size(Int.(permutedims(arr))))

    csv_path = replace(bin_path, r"(.*)\.bin" => s"\1.csv")
    open(csv_path, "w") do io
        writedlm(io, Int.(permutedims(arr)), ' ')
    end
    # julia is column major, python is row major; transpose

    println("$csv_path saved")
end

"""
Checks that all files for each configuration/directory 
are there. ie the QMC run has completed successfully.
"""
function check_dir(dir_path)
    for batch in 0:max_batch
        observables_path = joinpath(dir_path, "batch_$(lpad(batch, batch_digits, "0"))_raw_observables.csv")
        check_file(observables_path)
        samples_path = joinpath(dir_path, "batch_$(lpad(batch, batch_digits, "0"))_samples.bin")
        check_file(samples_path)
        save_as_csv(samples_path)
    end
    state_path = joinpath(dir_path, "batch_$(lpad(max_batch, batch_digits, "0"))_state.jld2")
    check_file(state_path)
    check_file(joinpath(dir_path, "energy_shift.csv"))
    check_file(joinpath(dir_path, "V_ij.csv"))
    println("$dir_path is complete; all csv files added.\n")
end

"""
Checks that a file exists, otherwise exits program.
"""
function check_file(file_path)
    # if !isfile(file_path)
    #     println(file_path," is missing")
    #     println("Program terminated")
    #     exit()
    # end
    if isfile(file_path)
        println(file_path," exists")
    else
        println(file_path," is missing")
        println("Program terminated")
        exit()
    end
end

###################### MAIN #############################

# "/home/hpcfung/qmc_test/L=11"
base_path = "/home/hpcfung/scratch/qmc_data/L=5"

# /home/hpcfung/scratch/qmc_data/L=5/Rb=1.05/omega=1.00/delta=-0.13/beta=0.5/seed=1234/batch_01_samples.bin

rb_values = ["1.05","1.15","1.30"]
delta_values = ["-0.36","-0.13","0.93","1.05","1.17","1.29","1.52","1.76","2.94","3.17"]
beta_values = ["0.5","1.0","2.0","4.0","8.0","16.0","32.0","48.0","64.0"]
omega = "1.00"
seed = "1234"
max_batch = 10
batch_digits = length(string(max_batch))

for rb in rb_values
    for delta in delta_values
        for beta in beta_values
            dir_path = joinpath(base_path,"Rb=$rb","omega=$omega",
                       "delta=$delta","beta=$beta","seed=$seed")
            check_dir(dir_path)
        end
    end
end

println("All files present. QMC run was complete.")
