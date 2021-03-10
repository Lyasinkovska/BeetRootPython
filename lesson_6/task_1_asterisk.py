"""
Сделайте словарь дней недели {1: "Monday", 2:... } в общем словарь. И потом "переверните" чтоб было {"Monday": 1, ...
"""
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# option 1
days_of_week = {i: day for i, day in zip(range(1, 8), days)}
print(days_of_week)

# option 2
week_days = {i: day for i, day in enumerate(days, start=1)}
print(week_days)

reversed_dict = {value: key for key, value in days_of_week.items()}
print(reversed_dict)
