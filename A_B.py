

def A(
        name: str, 
        n: int, 
        fin, 
        fout, 
        testcase_type = "sample", 
        start_name: int = 1
        ) -> list[tuple]:
    testcase_type = "_" if testcase_type == "sample" else ""
    path_input = "testcase/testcase_{}/input/".format(name)
    path_output = "testcase/testcase_{}/output/".format(name)
    input_list = []
    output_list = []
    for i in range(n):
        name_txt = start_name + i
        with open("{}input{}{}.txt".format(path_input, testcase_type, name_txt), "r") as infile:
            input_list.append(fin(list(map(lambda s: s.removesuffix("\n"), infile.readlines()))))
        with open("{}output{}{}.txt".format(path_output, testcase_type, name_txt), "r") as outfile:
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
         
def B(
        function_name: str, 
        testcase: list[tuple], 
        taqsim: tuple[int], 
        fin, 
        fout,
        type_of_test_case = 'R', 
        start_name = 1):
    
    types_of_test_cases = {
        'F': 'functional',
        'B': 'boundary',
        'E': 'edgecase',
        'P': 'performance',
        'R': 'randomized',
        'N': 'negative',
        'Re': 'regression',
        'C': 'comparison',
        'Cl': 'complexity'
    }

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
    
    path_input = "testcase/testcase_{}/input/".format(function_name)
    path_output = "testcase/testcase_{}/output/".format(function_name)
    
    n = len(testcase)
    for i, zatuple in enumerate(testcase):
        inarg, outarg = f(taqsim, zatuple)
        name_txt = start_name + i
        x = "{0}{1}/{1}_{2}.txt".format(path_input, types_of_test_cases[type_of_test_case], name_txt)
        
        y = "{0}{1}/{1}_{2}.txt".format(path_output, types_of_test_cases[type_of_test_case], name_txt)
        
        infile = open(x, "w")
        infile.writelines(fin(inarg))

        outfile = open(y, "w")
        outfile.write(fout(outarg))

        infile.close()
        outfile.close()
