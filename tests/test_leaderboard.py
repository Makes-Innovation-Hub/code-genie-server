from data_access_layer.leaderboard import add_user_points, check_user_points_existence, get_user_points, restore_db
import pytest


def test_add_user_points_success():
    data = {
        'user_id': '123',
        'topic': 'python',
        'difficulty': 'hard',
        'points': 8,
    }
    user_exist = check_user_points_existence(data)
    previous_points = 0
    if user_exist:
        previous_points = get_user_points(data)
    add_user_points(user_id=data['user_id'], topic=data['topic'], difficulty=data['difficulty'],
                    points=data['points'])
    assert check_user_points_existence(data)
    assert get_user_points(data) == 8 + previous_points
    data['points'] = 3
    add_user_points(user_id=data['user_id'], topic=data['topic'], difficulty=data['difficulty'],
                    points=data['points'])
    assert check_user_points_existence(data)
    assert get_user_points(data) == 11 + previous_points
    data['points'] = 11
    assert restore_db(data=data)
    if previous_points != 0:
        assert get_user_points(data) == previous_points
    assert check_user_points_existence(data) == user_exist
