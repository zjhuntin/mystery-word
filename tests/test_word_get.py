from mystery_word import word_get


small_list = "small_list.txt"

word_list = ["HIPPO",
             "MADDENING",
             "REGULAR",
             "HIPPOCAMPUS",
             "APPLE",
             "PENNYARCADE"]


def test_get_bigger_list():
    assert word_get(small_list, "E") in word_list


def test_easy_mode():
    easy_word_list = ["HIPPO", "APPLE"]
    assert word_get(small_list, "E") in easy_word_list


def test_medium_mode():
    medium_word_list = ["MADDENING", "REGULAR"]
    assert word_get(small_list, "M") in medium_word_list


def test_hard_mode():
    hard_word_list = ["PENNYARCADE", "HIPPOCAMPUS"]
    assert word_get(small_list, "H") in hard_word_list
