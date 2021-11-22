from utils import add

def tests():
    res = add(1,2)
    expected = 3
    assert res == expected 
    print("add(1, 2) = ", res, "\nPass")

    res = add(2,5)
    expected = 7
    assert res == expected 
    print("add(2, 5) = ", res, "\nPass")


if __name__ == "__main__":
    try:
        tests()
    except Exception as e:
        print('Errors encountered')
        print(str(e))
