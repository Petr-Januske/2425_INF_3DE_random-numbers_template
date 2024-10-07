import random



def generate_schedule(seed):
    
    random.seed(seed)
    
    subjects = ("CJL", "AJ", "OBN", "MA", "TEV", "INF", "ASW", "POS", "PRG", "MIT", "MSW", "VAP" , " ")
    schedule = []

    for day in range(5):
        schedule.append([])
        for _ in range(10):
            schedule[day].append(random.choice(subjects))

    return schedule

print("1  2  3  4  5  6  7  8  9  10")
print(generate_schedule(29))
