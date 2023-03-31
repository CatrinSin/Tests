# 4/1
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def find_russia(some_list):
    result_list = []
    for visit in some_list:
        if 'Россия' in list(visit.values())[0]:
            result_list.append(visit)
    return result_list

# 4/2
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def get_unique_id(some_dict):
    result = set()
    for i in some_dict.values():
      result.update(i)
    return result

# 4/3
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def get_max_value(some_dict):
    return max(some_dict, key = lambda k: some_dict[k])


