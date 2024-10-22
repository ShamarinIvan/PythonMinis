def solution(a):
    matrix = []
    t = a.split(" | ")
    for i in range(len(t)):
        matrix.append(t[i].split())
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = float(matrix[i][j])
    return matrix
if __name__ == "__main__":
    assert solution("1 2 3 | 4 5 6 | 7 8 9") == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert solution("1 2 | 3 4") == [[1, 2], [3, 4]]
