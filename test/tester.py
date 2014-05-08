#!/usr/bin/env python2.7

import importlib
import logging
import os
import subprocess
import sys
import time

# set PYTHONPATH
sys.path.append(os.getcwd()[0:-len('/test')])

from src.py.custom import tools, excepts


# Tweakable Parameters
test_runs = 10  # loops, for average
max_solve_time = 60  # seconds
prob_num_len = 3  # NNN


global dirs, user, lang, test_type, problems
global logger


def get_answer(file_path, file_name):
    
    def py_answer():
        
        # setup module info
        module_name = file_name.split('.')[0]
        problem_num = module_name[0:prob_num_len]
        
        # import solution as module
        solution = importlib.import_module('src.py.solutions.%s.%s' \
                                           % (problem_num, module_name))
        # run module
        answer = str(solution.main())
        
        return answer
    
    def cpp_answer():
        
        # compile .cpp source
        compile_cmd = 'g++ -o %s/ans.out %s/%s' % (file_path, file_path, file_name)
        subprocess.check_output(compile_cmd.split(' '))
        
        # run .out executable
        run_cmd = '%s/ans.out' % (file_path)
        answer = subprocess.check_output(run_cmd.split(' '))
        
        return answer
    
    def java_answer():
        
        # compile .java source
        compile_cmd = 'javac %s/%s' % (file_path, file_name)
        subprocess.check_output(compile_cmd.split(' '))
        
        # run .class
        run_cmd = 'java -cp %s %s' % (file_path, file_name[0:-len('.java')])
        answer = subprocess.check_output(run_cmd.split(' '))
        
        return answer
    
    options = {'py': py_answer, 'cpp': cpp_answer, 'java': java_answer}
    
    answer = options[lang]().strip()
    
    return answer


def validation():
    
    def validator(prob):
        
        # setup paths
        prob_dir_path = '%s/%s' % (dirs['solutions'], prob)
        if lang == 'java':
            usr_file_name = '_%s_%s.%s' % (prob, user, lang)
        else:
            usr_file_name = '%s_%s.%s' % (prob, user, lang)
        usr_file_path = '%s/%s' % (prob_dir_path, usr_file_name)
        ans_file_path = '%s/%s.txt' % (dirs['answers'], prob)
        
        # validate problem solution
        try:  # handle missing solution
            with open(usr_file_path, 'r'):
                pass
        except IOError:
            return 'Solution file does not exist!\n'
        
        try:  # handle slow solutions
            with tools.Timeout(max_solve_time):
                solution_out = get_answer(prob_dir_path, usr_file_name)
        except excepts.TimeoutError:
            return 'Timed out!\n'
        
        try:  # handle invalid output
            float(solution_out)  # all answers are floats
            str(solution_out)  # filter out error msgs
        except (ValueError, TypeError):
            return 'Invalid output!\n'
        
        try:  # handle non-existent answer.txt
            with open(ans_file_path, 'r') as ansf:
                expect_ans = str(ansf.read()).strip()
        except IOError:
            return 'Answer file does not exist!\n'
        
        user_ans = str(solution_out)
        
        if user_ans == expect_ans:
            return 'Valid Answer!\n'
        else:
            return 'Invalid Answer!\n'
    
    
    # validate all solutions
    for prob in problems:
        print '%s:' % (prob),
        print validator(prob)


def get_time(file_path, file_name):
    
    def py_time():
        
        # setup module info
        module_name = file_name.split('.')[0]
        problem_num = module_name[0:prob_num_len]
        
        # import solution as module
        solution = importlib.import_module('src.py.solutions.%s.%s' \
                                           % (problem_num, module_name))
        
        # time main() for test_runs, to get avg time
        overall_time = 0.0  # seconds
        for _ in xrange(test_runs):
            
            start_time = time.clock()
            
            solution.main()
            
            overall_time += (time.clock() - start_time)
        
        # calculate average runtime
        avg_time = overall_time / test_runs
        
        return avg_time
    
    def cpp_time():
        
        def parse_source():
            
            try:
                with open('temp.cpp', 'w+') as tempf:
                    
                    # copy part 1 of timer source
                    with open(cpptimer_p1_file_path, 'r') as partf1:
                        tempf.write(partf1.read())
                    
                    # copy solution source
                    with open(sol_file_path, 'r') as solf:
                        
                        logger.info('parsing source of <%s>:\n' % (file_name))
                        
                        # start reading source code
                        sol_code = solf.xreadlines()
                        code_line = next(sol_code)
                        logger.info('START')
                        
                        # ignore authorship comments
                        while '//' in code_line:
                            code_line = next(code_line)
                        logger.info('authorship comments parsed')
                        
                        # ignore preprocessor lines
                        while 'include' in code_line:
                            code_line = next(sol_code)
                        logger.info('preprocessor lines parsed')
                        
                        # ignore namespace line
                        while 'namespace' not in code_line:
                            code_line = next(sol_code)
                        logger.info('namespace line parsed')
                        
                        # move to start of actual source
                        while '(' not in code_line:
                            code_line = next(sol_code)
                        logger.info('blank lines parsed')
                        logger.info('reached main function, at line: <%s>' \
                                     % (code_line.strip()))
                        
                        code_line = next(sol_code)  # skip main() def
                        code_line = next(sol_code)  # skip { def
                        
                        logger.info('starting real code parse, at line: <%s>' \
                                     % (code_line.strip()))
                        # write rest of of source to temp
                        while 'cout' not in code_line:
                            tempf.write(code_line)
                            code_line = next(sol_code)
                        logger.info('stopping real code parse, before line: <%s>' \
                                     % (code_line.strip()))
                        
                        logger.info('STOP\n')
                    
                    # copy part 2 of timer source
                    with open(cpptimer_p2_file_path, 'r') as partf2:
                        tempf.write(partf2.read())
                    
            except Exception:
                    logger.exception('Caught exception after: <%s>' % (code_line))
                    with open('temp.cpp', 'r') as tempf:
                        logger.debug('temp.cpp contents:\n' + tempf.read())
        
        
        # setup paths
        sol_file_path = '%s/%s' % (file_path, file_name)
        cpptimer_dir_path = '%s/cpp-timer' % (dirs['misc'])
        cpptimer_p1_file_path = '%s/part1.txt' % (cpptimer_dir_path)
        cpptimer_p2_file_path = '%s/part2.txt' % (cpptimer_dir_path)
        
        # parse and create timable source
        parse_source()
        
        # compile source
        compile_cmd = 'g++ -o temp.out temp.cpp'
        subprocess.check_output(compile_cmd.split(' '))
        
        # run executable
        run_cmd = './temp.out'
        avg_time = subprocess.check_output(run_cmd.split(' ')).strip()
        
        return avg_time
    
    def java_time():
        return 'Not supported!'
    
    options = {'py': py_time, 'cpp': cpp_time, 'java': java_time}
    
    avg_time = options[lang]()
    
    time_info = '%s s' % (avg_time)
    
    return time_info


def timing():
    
    def timer(prob):
        
        # setup paths
        prob_dir_path = '%s/%s' % (dirs['solutions'], prob)
        timings_file_path = '%s/timings.txt' % (prob_dir_path)
        
        # store timings for each solution
        with open(timings_file_path, 'w+') as timef:
            
            # store runtime info
            run_time = time.strftime('%d %b %Y %H:%M:%S GMT\n', time.gmtime())
            tester_run_info = '%s @ %s\n' % (user, run_time)
            timef.write(tester_run_info)
            
            # filter and create solutions list
            solutions = [sol_file for sol_file in os.listdir(prob_dir_path) \
                         if sol_file.split('.')[1] == lang \
                         and prob in sol_file]
            
            # sort for cleaner testing
            solutions.sort()
            
            # time all solutions
            for sol_file in solutions:
                
                # get username of contributor
                user_name = sol_file.split('_')[1].split('.')[0]
                
                # get timing info for solution
                try:  # handle slow solutions
                    with tools.Timeout(max_solve_time*test_runs):
                        timing_info = get_time(prob_dir_path, sol_file)
                except excepts.TimeoutError:
                    timing_info = 'Timed out!'
                
                exec_info = '%s - %s\n' % (user_name, timing_info)
                timef.write(exec_info)
                yield exec_info[0:-len('\n')]
    
    
    # time all solutions
    for prob in problems:
        print '%s:' % (prob)
        for run_info in timer(prob):
            print run_info
        print ''


def run_test():
    
    run_time = time.strftime('%d %b %Y %H:%M:%S GMT', time.gmtime())
    
    run_info = '%s in %s, at %s:\n' % (user, lang, run_time)
    
    logger.info(run_info)
    
    print run_info
    
    print '%s started!\n' % (test_type['name'])
    
    test_type['function']()
    
    print '%s complete!\n' % (test_type['name'])


def setup_test():
    
    global dirs, user, lang, test_type, problems
    
    def get_dirs():
        
        # setup working directory structure
        dirs = {}
        dirs['test'] = os.getcwd()
        dirs['project'] = dirs['test'][0:-len('/test')]
        dirs['source'] = '%s/src' % (dirs['project'])
        dirs['data'] = '%s/data' % (dirs['project'])
        dirs['info'] = '%s' % (dirs['data'])
        dirs['misc'] = '%s/misc' % (dirs['data'])
        dirs['answers'] = '%s/answers' % (dirs['data'])
        
        return dirs
    
    def get_info(data):
        
        info_file_path = '%s/%s.txt' % (dirs['info'], data['filename'])
        # obtain data
        try:  # check if data is already saved
            with open(info_file_path, 'r') as infof:
                req_info = str(infof.read()).strip()
        except IOError:  # ask for data
            print data['prompt']
            req_info = raw_input('>')
            print ''
            
            # save data for future use
            with open(info_file_path, 'w+') as infof:
                infof.write(req_info)
        
        return req_info
    
    def get_test_type():
        
        # obtain testing action
        print 'Choose action: [v - Validate, t - Time]'
        to_run = raw_input('>')
        print ''
        
        # setup info_params
        
        options = {'v': {'name': 'Validation', 'function': validation}, \
                   't': {'name': 'Timing', 'function': timing}}
        
        try:  # validate choice
            test_type = options[to_run]
        except KeyError:  # try again
            print 'Invalid choice!'
            print 'Try again...\n'
            return get_test_type()
        
        return test_type
    
    def get_problems():
        
        # obtain problems to test
        print 'Enter problems: [NNN or all]'
        probs_list = raw_input('>')
        print ''
        
        # choose problems list source
        if probs_list == 'all':
            prob_nums_list = os.listdir(dirs['solutions'])
        else:
            prob_nums_list = probs_list.split(' ')
        
        # create problem list
        problems = [prob_num.zfill(prob_num_len) for prob_num in prob_nums_list \
                    if prob_num.isdigit()]
        
        # sort for cleaner testing
        problems.sort()
        
        # check if problems list is empty
        if not problems:
            print 'No valid problems to test!'
            print 'Try again...\n'
            return get_problems()
        
        return problems
    
    
    # setup working directories
    dirs = get_dirs()
    
    # setup user info
    
    options = {'user': {'prompt': 'Enter username:', 'filename': 'user'}, \
               'lang': {'prompt': 'Choose programming language: [py, cpp]', \
                        'filename': 'lang'}}
    
    user = get_info(options['user'])
    
    lang = get_info(options['lang'])
    
    # set solutions directory
    dirs['solutions'] = '%s/%s/solutions' % (dirs['source'], lang)
    
    # setup test parameters
    test_type = get_test_type()
    problems = get_problems()


def init_test():
    
    global logger
    
    # open logfile, for debug
    with open('debug.log', 'w+'):
        pass  # clear pre-existing debug_log
    
    # create logger
    logger = logging.getLogger('tester')
    logger.setLevel(logging.DEBUG)
    
    # add debug_log handler
    debug_log = logging.FileHandler('debug.log')
    debug_log.setLevel(logging.DEBUG)
    
    # create logger info formatter
    log_format = logging.Formatter('%(levelname)s: %(message)s')
    debug_log.setFormatter(log_format)
    
    # connect logger and log file
    logger.addHandler(debug_log)


def main():
    
    print 'Test started!\n'
    
    init_test()
    setup_test()
    run_test()
    
    print 'Test complete!'


if __name__ == '__main__':
    main()
