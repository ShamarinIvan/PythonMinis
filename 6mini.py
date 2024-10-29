def flatten(array, depth = 1):
    ans = array
    for i in range(depth):
        ans1 = []
        for el in ans:
            if not isinstance(el, list):
                ans1.append(el)
            else:
                ans1.extend(el)
        ans = ans1
    return ans
if __name__ == "__main__":
    assert(flatten([1,2,3,[4],5])) == [1,2,3,4,5]
    assert(flatten([1,2,[4,5,[6,7,8]],9,[10]], 2)) == [1,2,4,5,6,7,8,9,10]
    assert(flatten([1,2,[4,5,[6,7,8]],9,[10]])) == [1,2,4,5,[6,7,8],9,10]