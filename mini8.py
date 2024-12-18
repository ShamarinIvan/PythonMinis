def format_table(benchmarks, algos, results):
    len1 = max([len(el) for el in benchmarks])
    len2 = max([len(el) for el in algos])
    a = "| Benchmark" + " "*(len1-9)+" |"
    tempArr = [[len(str(el)) for el in list(column)] for column in zip(*results)]
    maximums = [max(el) for el in tempArr]
    for i in range(len(algos)):
        a += " " + str(algos[i]) + " "*(maximums[i]-len(algos[i]) if maximums[i] >= len(algos[i]) else 0) +" |"
    print(a)
    print("|" + (len(a)-2)*"-" + "|")
    for i in range(len(benchmarks)):
        a = "| " + str(benchmarks[i]) + " "*(len1-len(benchmarks[i]) if len1 >= 9 else 9-len(benchmarks[i]))+" |"
        for j in range(len(algos)):
            a += " " + str(results[i][j]) + ((maximums[j]-len(str(results[i][j]))) if maximums[j] >= len(algos[j]) else len(algos[j])-len(str(results[i][j])))*" " + " |"
        print(a)
format_table(["basdasdas", "wosasdasde", "the aasdasdse"], ["quick sort", "merge sort", "bubble sort", "the most genius sort"],[[15587876876876, 1.56,2.0, 2.22], [3.3, 2.9, 3.99999999999,2.22], [1.0,2.0,3.0,4.0]])
