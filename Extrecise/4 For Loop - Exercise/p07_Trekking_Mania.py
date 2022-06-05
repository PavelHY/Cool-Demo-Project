groups_num = int(input())

g1 = 0  # groip <=5
g2 = 0  # groip <=12
g3 = 0  # groip <=25
g4 = 0  # groip <=40
g5 = 0  # groip > 41
ppl_cnt = 0
for i in range(0, groups_num):
    ppl_num_in_group = int(input())
    if ppl_num_in_group <= 5:
        g1 += ppl_num_in_group
    elif ppl_num_in_group <= 12:
        g2 += ppl_num_in_group
    elif ppl_num_in_group <= 25:
        g3 += ppl_num_in_group
    elif ppl_num_in_group <= 40:
        g4 += ppl_num_in_group
    else:
        g5 += ppl_num_in_group

    ppl_cnt += ppl_num_in_group

print(f"{g1 / ppl_cnt * 100 :.2f}%")
print(f"{g2 / ppl_cnt * 100 :.2f}%")
print(f"{g3 / ppl_cnt * 100 :.2f}%")
print(f"{g4 / ppl_cnt * 100 :.2f}%")
print(f"{g5 / ppl_cnt * 100 :.2f}%")
