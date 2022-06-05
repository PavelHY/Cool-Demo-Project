length = float(input())
width = float(input())
height = float(input())
percent = float(input()) / 100

volume_aquarium = length * width * height
volume_aquarium_liters = volume_aquarium * 0.001

water_needed = volume_aquarium_liters - (volume_aquarium_liters * percent)

print(water_needed)