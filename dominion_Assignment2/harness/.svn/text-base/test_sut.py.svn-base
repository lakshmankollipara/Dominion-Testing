import sut as SUT
import random
import time
import sys
import traceback
import argparse
import os
from collections import namedtuple

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--depth', type=int, default=100,
                        help='Maximum search depth (100 default).')
    parser.add_argument('-t', '--timeout', type=int, default=3600,
                        help='Timeout in seconds (3600 default).')
    parser.add_argument('-s', '--seed', type=int, default=None,
                        help='Random seed (default = None).')
    parser.add_argument('-m', '--maxtests', type=int, default=-1,
                        help='Maximum #tests to run (-1 = infinite default).')
    parsed_args = parser.parse_args(sys.argv[1:])
    return (parsed_args, parser)

def make_config(pargs, parser):
    """
    Process the raw arguments, returning a namedtuple object holding the
    entire configuration, if everything parses correctly.
    """
    pdict = pargs.__dict__
    # create a namedtuple object for fast attribute lookup
    key_list = pdict.keys()
    arg_list = [pdict[k] for k in key_list]
    Config = namedtuple('Config', key_list)
    nt_config = Config(*arg_list)
    return nt_config   
    
parsed_args, parser = parse_args()
config = make_config(parsed_args, parser)
print('Random testing using config={}'.format(config))

if config.seed != None:
    mrandom = random.Random(config.seed)
else:
    mrandom = random.Random()


start = time.time()
elapsed = time.time()-start

t = SUT.t()

MAX_FAILED_TESTS = 100
API_ERROR_COUNT = {'scoreFor': 0, 'endTurn': 0, 'whoseTurn': 0, 'isGameOver': 0, 'playCard': 0, 'buyCard': 0}

# Max errors allowed per API endpoint
MAX_ERRORS_PER_ENDPOINT = 2

def check_endpoint_errors_exceeded(action):
    """
    Dominion specific function: Most of the actions in our SUT are dominion api calls.
    This function checks the type of an action and checks whether the max errors have been exceeded for this action.
    It returns False for any non dominion action.
    """
    for api_endpoint in API_ERROR_COUNT.keys():
        if api_endpoint in action:
            if API_ERROR_COUNT[api_endpoint] > MAX_ERRORS_PER_ENDPOINT:
                del[api_endpoint]
                return True
            else:
                API_ERROR_COUNT[api_endpoint] += 1
    else:
        return False


ntests = 0
failed_tests = 0

while (config.maxtests == -1) or (ntests < config.maxtests):
    ntests += 1

    t.restart()
    test = []

    for s in xrange(0, config.depth):
        a = mrandom.choice(t.enabled())
        (current_action, guard, action) = a
        test.append(current_action)
#       print s,text
        
        try:
            action()
            pass
        except IndexError:
            pass
        except AttributeError:
            pass
        except:
                # If the same API endpoint has caused a lot of errors stop recording errors for that endpoint.
                # endpoint_error
                endpoint_error_exceeded = check_endpoint_errors_exceeded(current_action)
                if (endpoint_error_exceeded):
                    continue

                print "============ Failed Test %s ==========="%(test[-1],)
                print test[-1]
                for step in test:
                    print step
                print "------------ Traceback ----------"
                etype, ename ,tb = sys.exc_info()
                print(ename)
                traceback.print_tb(tb)
                print
                failed_tests += 1
                if failed_tests > MAX_FAILED_TESTS:
                    print "***************************************"
                    print "EXITING SINCE MAX FAILED TESTS CROSSED"
                    sys.exit(1)

        if not t.check():
            print "Property failed!"
            (_,_,tb) = t.failure()
            traceback.print_tb(tb)
            print "TEST:"
            for step in test:
                print step 
            print "EXITING DUE TO FAILED TEST"
            sys.exit(1)
            
        elapsed = time.time() - start
        if elapsed > config.timeout:
            print "EXITING DUE TO TIMEOUT"
            print ntests, "EXECUTED"
            t.report()
            sys.exit(2)

t.report()

print ntests, "EXECUTED"
