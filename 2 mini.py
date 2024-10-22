def solution(a,b):
    l1 = len(a)
    l2 = len(b)
    result = []
    r = min(l1,l2)
    for i in range(r):
        result.append((a[i],b[i]))
    return result
if __name__ == "__main__":
    assert solution([1, 2, 3], ["a", "b"]) == [(1, "a"), (2, "b")]
    assert solution([1, 2, 3], ["a", "b", "c"]) == [(1, "a"), (2, "b"), (3, "c")]
    assert solution([1, 2, 3], ["a", "b", "c", "d"]) == [(1, "a"), (2, "b"), (3, "c")]
