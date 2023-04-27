import gekko_solver

equations = []
equations_file = '_Equations.txt'
with open(equations_file, 'r') as f:
    for line in f:
        equations.append(line.strip())

s = gekko_solver.Solution()

# write answers to file 
answers_file = '_Answers.txt'
answers = s.solution(equations, len(equations))

with open(answers_file, 'w') as f:
    for key, value in answers.items():
        var_name = key
        var_value = value[0]
        # write to the file
        f.write(f'{var_name} = {var_value}\n')