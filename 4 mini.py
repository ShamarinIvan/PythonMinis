def reverse_dict(d):
    reversed_dict = {}
    for key, value in d.items():
        if value in reversed_dict:
            if isinstance(reversed_dict[value], tuple):
                reversed_dict[value] = reversed_dict[value] + (key,)
            else:
                reversed_dict[value] = (reversed_dict[value], key)
        else:
            reversed_dict[value] = key
    return reversed_dict
reversed_dict = reverse_dict({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832})
if __name__ == "__main__":
    assert reverse_dict({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}) == {97832: ("Ivanov", "Kuznecov"), 55521: "Petrov"}
    assert reverse_dict({"Ivanov": 97832, "Petrov": 97832, "Kuznecov": 97832}) == {97832: ("Ivanov", "Petrov", "Kuznecov")}
    assert reverse_dict({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": [97832, 55521]})
