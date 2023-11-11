# TODO Напишите функцию find_common_participants
def find_common_participants(group_1, group_2, separator=","):
    group_1 = group_1.split(separator)
    group_2 = group_2.split(separator)
    intersection_group = set(group_1).intersection(group_2)
    intersection_group = list(intersection_group)
    intersection_group.sort()
    return intersection_group

participants_first_group = "Иванов/Петров/Сидоров"
participants_second_group = "Петров/Сидоров/Смирнов"
print(f"Общие участники: {find_common_participants(participants_first_group, participants_second_group, "/")}")
# TODO Провеьте работу функции с разделителем отличным от запятой
