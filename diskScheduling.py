import sys

#####################################
#               FCFS                #
#####################################
def fcfs(head, requests):
    total_head_movements = 0
    for req in requests:
        # calculate absolute distance and add to total
        total_head_movements += abs(req - head)  
    
        # update head position to the current request
        head = req  
    return total_head_movements

#####################################
#              SCAN                 #
#####################################
def scan(start, requests, total_cylinders):
    head_movements = 0
    current_position = start
    req_list = sorted(requests)

    # split requests into those lower and higher than the initial head position
    lower_requests = [r for r in req_list if r < current_position]
    upper_requests = [r for r in req_list if r >= current_position]

    # process upper requests in ascending order
    for request in upper_requests:
        head_movements += abs(current_position - request)
        current_position = request
    if lower_requests:
        # move head to the outermost cylinder before processing lower requests
        head_movements += abs(current_position - total_cylinders)
        current_position = total_cylinders
        # process lower requests in reverse order
        for request in reversed(lower_requests):
            head_movements += abs(current_position - request)
            current_position = request

    return head_movements

#####################################
#         OPTIMIZED SCAN            #
#####################################
def optimized_scan(requests, start, total_cylinders):
    head_movements = 0
    # set current position to the starting head position
    current_position = start

    # sort the requests in ascending order
    req_list = sorted(requests) 

    # split requests into lower and upper based on the current head position
    lower_requests = [r for r in req_list if r < current_position]
    upper_requests = [r for r in req_list if r >= current_position]

    # check if the starting position is closer to 0 or the maximum cylinder
    if current_position <= total_cylinders / 2:
        # process lower requests in reverse order
        for request in reversed(lower_requests):
            head_movements += abs(current_position - request)
            current_position = request
        if upper_requests:
            # move head to the innermost cylinder (0) before processing upper requests
            head_movements += abs(current_position - 0)
            current_position = 0
        # process upper requests in ascending order    
        for request in upper_requests:
            head_movements += abs(current_position - request)
            current_position = request
    else:
        # process upper requests in ascending order
        for request in upper_requests:
            head_movements += abs(current_position - request)
            current_position = request
        if lower_requests:
            # move head to the outermost cylinder before processing lower requests
            head_movements += abs(current_position - total_cylinders)
            current_position = total_cylinders
            # process lower requests in reverse order
            for request in reversed(lower_requests):
                head_movements += abs(current_position - request)
                current_position = request

    return head_movements

#####################################
#              C-SCAN               #
#####################################
def c_scan(start, requests, total_cylinders):
    head_movements = 0
    # set current position to the starting head position
    current_position = start

    # sort the requests in ascending order
    req_list = sorted(requests) 

    # split requests into lower and upper based on the current head position
    lower_requests = [r for r in req_list if r < current_position]
    upper_requests = [r for r in req_list if r >= current_position]

    # check if the starting position is closer to 0 or the maximum cylinder
    if current_position <= total_cylinders / 2:
        # process upper requests in ascending order
        for request in upper_requests:
            head_movements += abs(current_position - request)
            current_position = request
        if lower_requests:
            # move head to the innermost cylinder (0) before processing lower requests
            head_movements += abs(current_position - 0)
            current_position = 0
        # process lower requests in ascending order
        for request in lower_requests:
            head_movements += abs(current_position - request)
            current_position = request
    else:
        # process lower requests in reverse order
        for request in lower_requests:
            head_movements += abs(current_position - request)
            current_position = request
        if upper_requests:
            # move head to the outermost cylinder before processing upper requests
            head_movements += abs(current_position - total_cylinders)
            current_position = total_cylinders
            # process upper requests in ascending order
            for request in upper_requests:
                head_movements += abs(current_position - request)
                current_position = request

    return head_movements

#####################################
#        OPTIMIZED C-SCAN           #
#####################################
def optimized_c_scan(start, requests, total_cylinders):
    head_movements = 0
    current_position = start
    req_list = sorted(requests)

    # split requests into those lower and higher than the initial head position
    lower_requests = [r for r in req_list if r < current_position]
    upper_requests = [r for r in req_list if r >= current_position]

    # process upper requests first
    for request in upper_requests:
        head_movements += abs(current_position - request)
        current_position = request

    # move to the end of the cylinder if there are lower requests
    if lower_requests:
        head_movements += abs(current_position - total_cylinders)
        current_position = 0

        for request in lower_requests:
            head_movements += abs(current_position - request)
            current_position = request

    return head_movements

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 diskScheduling.py <initial_position> <input_file>")
        return

    initial_position = int(sys.argv[1])
    input_file = sys.argv[2]

    with open(input_file, 'r') as file:
        requests = [int(line.strip()) for line in file.readlines()]

    # Task 1: Service requests as they appear in the file
    fcfs_head_movements = fcfs(initial_position, requests)
    scan_head_movements = scan(initial_position, requests, 5000)
    c_scan_head_movements = c_scan(initial_position, requests, 5000)
    
    # display total head movements
    print("Task 1:")
    print("FCFS:", fcfs_head_movements)
    print("SCAN:", scan_head_movements)
    print("C-SCAN:", c_scan_head_movements)

    # Task 2: rearrange requests to minimize head movements
    optimized_fcfs_head_movements = fcfs(initial_position, sorted(requests))
    optimized_scan_head_movements = optimized_scan(requests, initial_position, 5000)
    optimized_c_scan_head_movements = optimized_c_scan(initial_position, requests, 5000)

    # display total head movements
    print("\nTask 2:")
    print("Optimized FCFS:", optimized_fcfs_head_movements)
    print("Optimized SCAN:", optimized_scan_head_movements)
    print("Optimized C-SCAN:", optimized_c_scan_head_movements)


if __name__ == "__main__":
    main()
