# READ ME
## enviornment
Base on python 3.6
The main function is in FailureCount.py class ErrorCollection


## Target json data
successful:
```
{
    "time":"2018-07-22T04:32:53+10:00",
    "level":"debug",
    "msg":"retrieved user profile for4e55fe7b-82eb-4d84-a40b-aeba2f7b2b2c",
    "app":"svc-app2",
    "component":"userRepo.Fetch()",
    "response":200,
    "env":"prod",
    "span_id":"2acf4395-2c98-468d-ba8d-96fe9484253a",
    "trace_id":"e261afb3-584f-41d9-92de-bea1c5a15e8c"
}
```
failure:
```
{
    "time":"2018-07-22T00:18:43+10:00",
    "level":"debug",
    "msg":"unable to retrieve user profile: host 145.222.50.173 not reachable",
    "app":"svc-app2",
    "component":"userRepo.Fetch()",
    "response":500,
    "env":"prod",
    "span_id":"d0d8fcaff2be-4cc3-91a4-3840c05fd361",
    "trace_id":"933ecf49-705f-4903-a2d3-913316fd7010"
}
```
## Assumption:
1. the response code over 400 is indicate there is an error
2. every item has special column 'time' for time string and it can parse to timestamp 
3. every item has msg column to give error message or response
4. every item has component to indicate which module running
5. if the trace_id is same, it will regard as same error
6. if the trace_id is the same the later one is cause by the early errors, which means the later error will output at first.
7. Although, I writing the some failure caused by other failure, but it is not sure for that, just the second error is earlier than the first one.

## complex analysis

(https://github.com/python/cpython/blob/3.6/Lib/heapq.py)

Assume the item length is X, there would be only n errors, and in every errors the arraay length is K
### Time complex
for is just one loop for visit every items, there would be O(X) complexity
for heap insert the worst case complex one item insert is lg2(K), so the worst total insert O(n*K*lg2(K))
the print_error_details function will visit every item and for every item the nlargest complex is O(K*lg2(K))
(There are four step for nlargest function and the complex compute detail you can see the link above)
So, the print_error_details function complex is O(n*K*lg2(K))
### Space complex
The json analysis need space X, the errors store need space n. So, the complex space is O(X)+O(n)


