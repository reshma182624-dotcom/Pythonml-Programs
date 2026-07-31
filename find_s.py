import csv
data = []
with open('Trainingdata.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip header
    for row in reader:
        data.append(row)
print("Training Data:\n")
for row in data:
    print(row)

# Initialize the hypothesis
hypothesis = ['0'] * (len(data[0]) - 1)

print("\nInitial Hypothesis:")
print(hypothesis)

# Apply FIND-S Algorithm
for row in data:
    if row[-1].lower() == "yes":
        for i in range(len(hypothesis)):
            if hypothesis[i] == '0':
                hypothesis[i] = row[i]
            elif hypothesis[i] != row[i]:
                hypothesis[i] = '?'
print("Final Most Specific Hypothesis:")
print(hypothesis)
