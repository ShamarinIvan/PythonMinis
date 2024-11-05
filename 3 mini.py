def solution(a):
    matrix = []
    t = a.split(" | ")
    for i in range(len(t)):
        matrix.append([float(el) for el in t[i].split()])
    return matrix
if __name__ == "__main__":
    assert solution("1 2 3 | 4 5 6 | 7 8 9") == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert solution("1 2 | 3 4") == [[1, 2], [3, 4]]
