import problem_spider
import problem_list_spider

# Get the list of problems
problem_list = problem_list_spider.get_problem_list()

# Get the problem
for problem in problem_list:
    problem_spider.get_problem(problem)