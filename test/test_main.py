from main import find_russia, get_unique_id, get_max_value


class TestLectureFour:
    def test_geo_logs(self):
        list_of_visits = [
    {'visit1': ['Лондон', 'Англия']},
    {'visit2': ['Пермь', 'Россия']},
    {'visit3': ['Прага', 'Чехия']},
    {'visit4': ['Париж', 'Франция']},
    {'visit5': ['Иваново', 'Россия']},
    {'visit6': ['Екатеринбург', 'Россия']},
    {'visit7': ['Милан', 'Италия']}
]
        result = find_russia(list_of_visits)
        expected = [
    {'visit2': ['Пермь', 'Россия']},
    {'visit5': ['Иваново', 'Россия']},
    {'visit6': ['Екатеринбург', 'Россия']},
]
        assert result == expected


    def test_uniq_id(self):
        dict_of_ids = {'user1': [312, 15, 312, 15, 17],
       'user2': [45, 95, 515, 515, 515],
       'user3': [312, 95, 2, 312]}
        result = get_unique_id(dict_of_ids)
        expected = {2, 515, 45, 15, 17, 312, 95}
        assert result == expected


    def test_max_value(self):
        dict_of_stats = {'facebook': 120, 'yandex': 45, 'vk': 99, 'google': 150, 'email': 98, 'ok': 42}
        result = get_max_value(dict_of_stats)
        expected = 'google'
        assert result == expected
