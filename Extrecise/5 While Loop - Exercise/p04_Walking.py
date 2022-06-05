steps_to_rich = 10000
steps_cnt = 0
new_steps = 0

while True:
    command = input()

    if command != "Going home":
        new_steps = int(command)
        steps_cnt += new_steps

        if steps_cnt >= steps_to_rich:
            print("Goal reached! Good job!")
            print(f"{steps_cnt - steps_to_rich} steps over the goal!")
            break
    else:
        command = input()
        new_steps = int(command)
        steps_cnt += new_steps

        if steps_cnt >= steps_to_rich:
            print("Goal reached! Good job!")
            print(f"{steps_cnt - steps_to_rich} steps over the goal!")
            break
        else:
            print(f"{steps_to_rich - steps_cnt} more steps to reach goal.")
            break
