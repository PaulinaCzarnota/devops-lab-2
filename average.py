numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
avg = sum(numbers) / len(numbers)
print("Average:", avg)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

