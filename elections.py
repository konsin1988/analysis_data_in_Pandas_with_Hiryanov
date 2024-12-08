with open('students.txt', encoding='utf8') as file:
    students_set = {line.strip() for line in file}
print(students_set)

candidates_votes = {}
with open('elections.txt') as file:
    for line in file:
        candidate = line.strip()
        if candidate not in students_set:
            continue
        if candidate not in candidates_votes:
            candidates_votes[candidate] = 1
        else:
            candidates_votes[candidate] += 1

print(candidates_votes)