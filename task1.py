#Do Not use crtl+A to select code.  Only copy the code below this line.
#------------------------------------------------------------------------------------------------

total_slices =  party_pizza_mini + large + medium
print(f" Total Number of slices: {total_slices}")

people += 1
Slices_per_person = total_slices // people
Leftovers = total_slices % people
print(f" Each person gets: {Slices_per_person}")
print(f" Leftovers slices: {Leftovers}")

people += 2   #Eric and Brandon are coming too.
Slices_per_person = total_slices // people
Leftovers = total_slices % people
print(f" Each person gets: {Slices_per_person}")
print(f" Leftovers slices: {Leftovers}")

#Mom says "Wait, Brandon’s coming. We’re going to need more pizza. I’ll upgrade the mini to a party_pizza instead. It’s the same as 2 minis. Hopefully the leftovers will be enough to fill his hollow leg.”

total_slices = 2 * party_pizza_mini + large + medium
Slices_per_person = total_slices // people
Leftovers = total_slices % people
print(f" Each person gets: {Slices_per_person}")
print(f" Leftovers slices: {Leftovers}")
print("...for Mr. Hollow Leg")
