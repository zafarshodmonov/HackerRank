
def A(name: str, n: int, fin, fout) -> list[tuple]:
    path_input = "testcase/testcase_{}/input/".format(name)
    path_output = "testcase/testcase_{}/output/".format(name)
    input_list = []
    output_list = []
    for i in range(1, n + 1):
        with open("{}input_{}.txt".format(path_input, i), "r") as infile:
            input_list.append(fin(list(map(lambda s: s.removesuffix("\n"), infile.readlines()))))
        with open("{}output_{}.txt".format(path_output, i), "r") as outfile:
            output_list.append(fout(list(map(lambda s: s.removesuffix("\n"), outfile.readlines()))))
    rel = []
    for i in range(n):
        x = input_list[i]
        y = output_list[i]
        a = type(x) is tuple
        b = type(y) is tuple
        if a and b:
            rel.append(x + y)
        elif not a and b:
            rel.append((x, * y))
        elif a and not b:
            rel.append((* x, y))
        else:
            rel.append((x, y))
    return rel
         
def B(name: str, testcase: list[tuple], taqsim: tuple[int], fin, fout):

    def f(taqsim: tuple[int], zatuple: tuple):
        inarg = []
        outarg = []
        x = 0
        for i in range(taqsim[0]):
            inarg.append(zatuple[i])
            x = i
        for i in range(x + 1, x + 1 + taqsim[1]):
            outarg.append(zatuple[i])
        return tuple(inarg), tuple(outarg)
    
    path_input = "testcase/testcase_{}/input/".format(name)
    path_output = "testcase/testcase_{}/output/".format(name)
    
    n = len(testcase)
    for i, zatuple in enumerate(testcase):
        inarg, outarg = f(taqsim, zatuple)
        with open("{}input{}.txt".format(path_input, i + 1), "w") as infile:
            infile.writelines(fin(inarg))
        with open("{}output{}.txt".format(path_output, i + 1), "w") as outfile:
            outfile.write(fout(outarg))
