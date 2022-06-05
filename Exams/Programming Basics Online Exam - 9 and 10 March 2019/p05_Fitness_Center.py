back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0

customer = int(input())
for _ in range(customer):
    fitness_activity = input()
    if fitness_activity == "Back":
        back += 1
    elif fitness_activity == "Chest":
        chest += 1
    elif fitness_activity == "Legs":
        legs += 1
    elif fitness_activity == "Abs":
        abs += 1
    elif fitness_activity == "Protein shake":
        protein_shake += 1
    elif fitness_activity == "Protein bar":
        protein_bar += 1
gim_product = protein_bar + protein_shake
work_out_ppl = back + chest + legs + abs

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{work_out_ppl / customer * 100:.2f}% - work out")
print(f"{gim_product / customer * 100:.2f}% - protein")
