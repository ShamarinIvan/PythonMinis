def flatten(array, depth=None):
    def _flatten(arr, current_depth):
        for el in arr:
            if isinstance(el, list) and (current_depth is None or current_depth > 0):
                yield from _flatten(el, None if current_depth is None else current_depth - 1)
            else:
                yield el
    return list(_flatten(array, depth))
if __name__ == "__main__":
    assert(flatten([1,2,3,[4],5])) == [1,2,3,4,5]
    assert(flatten([1,2,[4,5,[6,7,8]],9,[10]], 2)) == [1,2,4,5,6,7,8,9,10]
    assert(flatten([1,2,[4,5,[6,7,8]],9,[10]])) == [1,2,4,5,6,7,8,9,10]
