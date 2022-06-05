volume_of_the_pool = int(input())
pipe_one = int(input())
pipe_twu = int(input())
worker_is_out = float(input())

debit_pipe_one = pipe_one * worker_is_out  # 300l
debit_pipe_twu = pipe_twu * worker_is_out  # 360l

field = debit_pipe_one + debit_pipe_twu  # 660l

percent_debit_p1 = debit_pipe_one / field * 100
percent_debit_p2 = debit_pipe_twu / field * 100
percent_field = field / volume_of_the_pool * 100

if field <= volume_of_the_pool:
    print(f"The pool is {percent_field:.2f}% full. Pipe 1: "
          f"{percent_debit_p1:.2f}%. Pipe 2: "
          f"{percent_debit_p2:.2f}%.")
else:
    print(f"For {worker_is_out} hours the pool overflows with"
          f" {(field - volume_of_the_pool):.2f} liters.")
