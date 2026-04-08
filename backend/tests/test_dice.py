from backend.dice import roll, get_face

def test_roll_in_range():
    for _ in range(100):
        assert 1 <= roll() <= 6

def test_face_valid():
    for i in range(1, 7):
        assert get_face(i) in "⚀⚁⚂⚃⚄⚅"