def format_table(benchmarks, algos, results):
    len1 = max([len(el) for el in benchmarks])
    len2 = max([len(el) for el in algos])
    a = "| Benchmark" + " "*(len1-9)+" |"
    for i in range(len(algos)):
        a += " " + str(algos[i]) + " |"
    print(a)
    print("|" + (len(a)-2)*"-" + "|")
    for i in range(len(benchmarks)):
        a = "| " + str(benchmarks[i]) + " "*(len1-len(benchmarks[i]))+" |"
        for j in range(len(algos)):
            a += " " + str(results[i][j]) + (len(algos[j])-len(str(results[i][j])))*" " + " |"
        print(a)
format_table(["best case", "worst case", "the best case"], ["quick sort", "merge sort", "bubble sort", "the most genius sort"],[[1.23, 1.56,2.0, 2.22], [3.3, 2.9, 3.9,2.22], [1.0,2.0,3.0,4.0]])
