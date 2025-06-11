
# Python Assignment (Full Solution)

import random
import string
import time
import matplotlib.pyplot as plt

# Helper function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

---------------------------------------------
#Q1. List Operations
L = [11, 12, 13, 14]

L.append(50)
L.append(60)
print("Q1(i):", L)

L.remove(11)
L.remove(13)
print("Q1(ii):", L)

L.sort()
print("Q1(iii):", L)

L.sort(reverse=True)
print("Q1(iv):", L)

print("Q1(v):", 13 in L)

print("Q1(vi):", len(L))

print("Q1(vii):", sum(L))

print("Q1(viii):", sum(i for i in L if i % 2 != 0))

print("Q1(ix):", sum(i for i in L if i % 2 == 0))

print("Q1(x):", sum(i for i in L if is_prime(i)))

L.clear()
print("Q1(xi):", L)

del L
# Q1(xii): List deleted

---------------------------------------------
# Q2. Dictionary Operations
D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}

D[8] = 8.8
print("Q2(i):", D)

D.pop(2)
print("Q2(ii):", D)

print("Q2(iii):", 6 in D)

print("Q2(iv):", len(D))

print("Q2(v):", sum(D.values()))

D[3] = 7.1
print("Q2(vi):", D)

D.clear()
print("Q2(vii):", D)

---------------------------------------------
# Q3. Set Operations
S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}

S1.add(55)
S1.add(66)
print("Q3(i):", S1)

S1.discard(10)
S1.discard(30)
print("Q3(ii):", S1)

print("Q3(iii):", 40 in S1)

print("Q3(iv):", S1.union(S2))

print("Q3(v):", S1.intersection(S2))

print("Q3(vi):", S1.difference(S2))

---------------------------------------------
# Q4. Programs

print("Q4(i): 100 Random Strings (length 6 to 8):")
for _ in range(100):
    print(''.join(random.choices(string.ascii_letters, k=random.randint(6, 8))))

print("Q4(ii): Prime Numbers between 600 and 800:")
for i in range(600, 801):
    if is_prime(i):
        print(i)

print("Q4(iii): Numbers between 100 and 1000 divisible by 7 and 9:")
for i in range(100, 1001):
    if i % 7 == 0 and i % 9 == 0:
        print(i)

---------------------------------------------
# Q5. Random List Operations
list1 = random.sample(range(10, 31), 10)
list2 = random.sample(range(10, 31), 10)

print("Q5: List1:", list1)
print("Q5: List2:", list2)

print("Q5(i): Common:", list(set(list1) & set(list2)))
print("Q5(ii): Unique:", list(set(list1) ^ set(list2)))
print("Q5(iii): Min list1:", min(list1), "| Min list2:", min(list2))
print("Q5(iv): Max list1:", max(list1), "| Max list2:", max(list2))
print("Q5(v): Sum list1:", sum(list1), "| Sum list2:", sum(list2))

---------------------------------------------
# Q6. 100 Random Numbers between 100 and 900
nums = [random.randint(100, 900) for _ in range(100)]
odds = [n for n in nums if n % 2 != 0]
evens = [n for n in nums if n % 2 == 0]
primes = [n for n in nums if is_prime(n)]

print("Q6(i): Odd numbers:", odds)
print("Q6(ii): Even numbers:", evens)
print("Q6(iii): Prime numbers:", primes)

---------------------------------------------
# Q7. Read and Write Dictionary to File
D = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five"}
with open("Q7_output.txt", "w") as file:
    for k, v in D.items():
        file.write(f"{k}, {v}\n")

---------------------------------------------
# Q8. Count Lengths and Write to File
L = ["One", "Two", "Three", "Four", "Five"]
with open("Q8_output.txt", "w") as file:
    for item in L:
        file.write(f"{item}, {len(item)}\n")

---------------------------------------------
# Q9. Write 100 Random Strings (length 10 to 15) to File
with open("Q9_output.txt", "w") as file:
    for _ in range(100):
        rand_str = ''.join(random.choices(string.ascii_letters, k=random.randint(10, 15)))
        file.write(rand_str + "\n")

---------------------------------------------
# Q10. Write Prime Numbers (600–800) to File
with open("Q10_output.txt", "w") as file:
    for i in range(600, 801):
        if is_prime(i):
            file.write(str(i) + "\n")

---------------------------------------------
# Q11. Measure Time Taken by a Program
start = time.time()
total = sum(range(1, 1000000))
end = time.time()
print("Q11: Time taken:", end - start)

---------------------------------------------
# Q12. Sort and Plot Time
sizes = [5000, 10000, 15000, 20000, 25000]
times = []

for size in sizes:
    data = [random.randint(1, 100000) for _ in range(size)]
    start = time.time()
    sorted_data = sorted(data)
    end = time.time()
    times.append(end - start)

print("Q12: Sizes vs Time:", list(zip(sizes, times)))

plt.plot(sizes, times, marker='o')
plt.title("List Sorting Time")
plt.xlabel("Number of Elements")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.show()

---------------------------------------------
# Q13. Student Marks Dictionary and Max/Min Average
students = {
    "Alice": [88, 76, 90, 85, 92],
    "Bob": [70, 60, 65, 58, 72],
    "Charlie": [95, 98, 97, 96, 94],
    "Diana": [80, 85, 82, 79, 81],
    "Eve": [60, 63, 59, 61, 62]
}

averages = {name: sum(marks)/len(marks) for name, marks in students.items()}
max_student = max(averages, key=averages.get)
min_student = min(averages, key=averages.get)

print("Q13: Student with max average:", max_student, averages[max_student])
print("Q13: Student with min average:", min_student, averages[min_student])
