
def help_1(c: str, v: str) -> str:

    return """
class {0}Test:
    pass
    

class {0}({0}Test):
    pass
    

{1} = {0}()
""".format(c, v)



PLATFORM = [
        ('CodeForces', 'codeforces'),
        ('CodeWars', 'codewars'),
        ('CodeByte', 'codebyte'),
        ('CodeChef', 'codechef'),
        ('RoboContest', 'robocontest'),
        ('ACMP', 'acmp')
]

for c, v in PLATFORM:
    # Open a file named test.py in write mode
    with open(f'solution_{v}.py', 'w') as file:
        # Write some Python code to the file
        file.write(help_1(c, v))
    

# The file is automatically closed when the with block is exited
