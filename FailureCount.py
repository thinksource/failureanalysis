import json
import heapq as hq
from dateutil import parser


class ErrorCollection(object):
    '''
    The error structure:
    -----------------------------------------------
    | trace_id(key) | heap_queue of details erorr
    -----------------------------------------------
    The heap queue is sorted with timestamp
    '''
    def __init__(self, filename):
        with open(filename) as f:
            self.data = json.load(f)
        self.extra_failures()

    def extra_failures(self):
        self.errors={}
        for d in self.data:
            if "response" in d and d["response"] >= 400:
                if d["trace_id"] not in self.errors:
                    self.errors[d["trace_id"]] = []
                dtime=parser.parse(d['time'])
                # heaq is ordered so after heap push it will keep order by dtime
                hq.heappush(self.errors[d["trace_id"]],(dtime, d['msg'],d['component']))
        return self.errors

    def get_error_count(self):
        return len(self.errors)

    def print_error_detail(self):
        cause = " caused by "
        for key, value in self.errors.items():
            re = "trace_id : {}".format(key) + "\n"
            # as time reverse for output the largest timestamp first
            tmp=""
            for e in hq.nlargest(len(value),value):
                tmp += cause + e[1] + "; in component " + e[2] + ";"
            print(re+ tmp[len(cause):-1])
                