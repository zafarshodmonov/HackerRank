import os
import random

from solution_hackerrank import hackerrank


class RandomTestcaseHackerRank:

    @staticmethod
    def solveMeFirst():
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        return a, b
    

class RandomTestcaseCodeWars:

    @staticmethod
    def f2(self):
        the_number_of_nucleotides_in_DNA = random.randint(1, 1000)
        DNA = ''
        nucleotides = {1: 'G', 2: 'C', 3: 'A', 4: 'T'}
        for i in range(the_number_of_nucleotides_in_DNA):
            ch = nucleotides[random.randint(1, 4)]
            DNA += ch
        return DNA

     
class TestcaseTxtToArgvaluesHackerRank:

    def input_F1(self, inputs: list[str]):
        return list(map(int, inputs[1].split()))
    
    def output_F1(self, outputs: list[str]) -> list[int]:
        return list(map(int, outputs[0].split()))

    def input_solveMeFirst(self, inputs: list[str]):
        a = int(inputs[0])
        b = int(inputs[1])
        return a, b

    def output_solveMeFirst(self, outputs: list[str]) -> int:
        n = int(outputs[0])
        return n


class TestcaseArgvaluesToTxtHackerRank:
    
    def input_solveMeFirst(self, zatuple: tuple):
        
        res = ''
        for i in zatuple:
            res += "{}{}".format(i, "\n")
        res = res[:-1]
        return res
    
    def output_solveMeFirst(self, zatuple: tuple):
        
        res = ''
        for i in zatuple:
            res += "{}{}".format(i, "\n")
        res = res[:-1]
        return res
    
    pass


def random_testcase(
        number_of_testcase: int, 
        input_value_function, 
        output_value_function) -> list[tuple]:

    argvalues = []

    for i in range(number_of_testcase):

        zain = input_value_function()
        m1 = type(zain) is tuple
        zaout = output_value_function(* zain) if m1 else output_value_function(zain)
        m2 = type(zaout) is tuple

        if m1 and m2:
            zatuple = (* zain, * zaout)
        elif m1 and not m2:
            zatuple = (* zain, zaout)
        elif not m1 and m2:
            zatuple = (zain, * zaout)
        else:
            zatuple = (zain, zaout)
        argvalues.append(zatuple)
    return argvalues

def testcase_txt_to_argvalues(
        platform_name: str,
        function_name: str, 
        testcase_type: str,
        number_of_tests: int, 
        input_value_function, 
        output_value_function, 
        start_index_of_tests: int
        ) -> list[tuple]:
    
    PLATFORM = {
        'LC': 'leetcode',
        'CF': 'codeforces',
        'HR': 'hackerrank',
        'CW': 'codewars',
        'CB': 'codebyte',
        'CC': 'codechef',
        'RC': 'robocontest',
        'AC': 'acmp'
    }

    platform_name = PLATFORM[platform_name] if (platform_name in PLATFORM) else platform_name

    TESTCASE_TYPE = {
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

    testcase_type = TESTCASE_TYPE[testcase_type] if (testcase_type in TESTCASE_TYPE) else testcase_type

    path_input = f"testcase_database/platform_{platform_name}/function_{function_name}/input/{testcase_type}/{testcase_type}_"
    path_output = f"testcase_database/platform_{platform_name}/function_{function_name}/output/{testcase_type}/{testcase_type}_"

    input_list = []
    output_list = []

    for i in range(start_index_of_tests, start_index_of_tests + number_of_tests):
        
        with open(f"{path_input}{i}.txt", "r") as infile:
            input_list.append(input_value_function(list(map(lambda s: s.removesuffix("\n"), infile.readlines()))))

        with open(f"{path_output}{i}.txt", "r") as outfile:
            output_list.append(output_value_function(list(map(lambda s: s.removesuffix("\n"), outfile.readlines()))))

    argvalues = []

    for i in range(number_of_tests):

        x = input_list[i]
        y = output_list[i]

        a = type(x) is tuple
        b = type(y) is tuple

        if a and b:
            argvalues.append(x + y)
        elif not a and b:
            argvalues.append((x, * y))
        elif a and not b:
            argvalues.append((* x, y))
        else:
            argvalues.append((x, y))
    
    return argvalues
         
def testcase_argvalues_to_txt(
        platform_name: str,
        function_name: str, 
        testcase_type: str,
        input_value_function, 
        output_value_function, 
        start_index_of_tests: int,
        argvalues: list[tuple], 
        taqsim: tuple[int]):
    
       
    PLATFORM = {
        'LC': 'leetcode',
        'CF': 'codeforces',
        'HR': 'hackerrank',
        'CW': 'codewars',
        'CB': 'codebyte',
        'CC': 'codechef',
        'RC': 'robocontest',
        'AC': 'acmp'
    }

    platform_name = PLATFORM[platform_name] if (platform_name in PLATFORM) else platform_name

    TESTCASE_TYPE = {
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

    testcase_type = TESTCASE_TYPE[testcase_type] if (testcase_type in TESTCASE_TYPE) else testcase_type

    path_input = f"testcase_database/platform_{platform_name}/function_{function_name}/input/{testcase_type}/{testcase_type}"
    path_output = f"testcase_database/platform_{platform_name}/function_{function_name}/output/{testcase_type}/{testcase_type}"


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
     
    number_of_tests = len(argvalues)

    for i, zatuple in enumerate(argvalues):

        inarg, outarg = f(taqsim, zatuple)
        name_txt = start_index_of_tests + i
        
        infile = open(f"{path_input}{name_txt}.txt", "w")
        infile.writelines(input_value_function(inarg))

        outfile = open(f"{path_output}{name_txt}.txt", "w")
        outfile.write(output_value_function(outarg))

        infile.close()
        outfile.close()
    
    return None

def testcase_file_remove(
        platform_name: str,
        function_name: str, 
        testcase_type: str, 
        start_index_of_tests: int,
        number_of_tests: int
        ):
     
    PLATFORM = {
        'LC': 'leetcode',
        'CF': 'codeforces',
        'HR': 'hackerrank',
        'CW': 'codewars',
        'CB': 'codebyte',
        'CC': 'codechef',
        'RC': 'robocontest',
        'AC': 'acmp'
    }

    platform_name = PLATFORM[platform_name] if (platform_name in PLATFORM) else platform_name

    TESTCASE_TYPE = {
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

    testcase_type = TESTCASE_TYPE[testcase_type] if (testcase_type in TESTCASE_TYPE) else testcase_type

    path_input = f"testcase_database/platform_{platform_name}/function_{function_name}/input/{testcase_type}/{testcase_type}"
    path_output = f"testcase_database/platform_{platform_name}/function_{function_name}/output/{testcase_type}/{testcase_type}"

    def remove_file(file_path: str):

        try:
            os.remove(file_path)
            print(f"{file_path} has been deleted.")
        except FileNotFoundError:
            print(f"The file {file_path} does not exist.")
        except PermissionError:
            print(f"Permission denied: Unable to delete {file_path}.")
        except Exception as e:
            print(f"An error occurred: {e}")


    for i in range(start_index_of_tests, start_index_of_tests + number_of_tests):
        remove_file(f"{path_input}{i}")
        remove_file(f"{path_output}{i}")
    
    return None

random_testcase_hackerrank = RandomTestcaseHackerRank()
testcase_txt_to_argvalues_hackerrank = TestcaseTxtToArgvaluesHackerRank()
testcase_argvalues_to_txt_hackerrank = TestcaseArgvaluesToTxtHackerRank()

#argvalues = testcase_txt_to_argvalues('HR', 'F1', 'F', 1, testcase_txt_to_argvalues_hackerrank.input_F1, testcase_txt_to_argvalues_hackerrank.output_F1, 1)
