# Disk Scheduling Algorithms

Name: Jeffrey

NIM : 2602118484

Class: L4AC

## Algorithm Explanation

- #### FCFS (First Come, First Served)

    Disc requests are handled by the FCFS algorithm in the sequence they arrive. It moves, independent of the head position at the moment, from one request to the next in order to compute the total head motions.

- #### SCAN (Elevator Algorithm)

    The disc head is moved towards one end of the disc by the SCAN algorithm, which then reverses direction at the end to service requests in the other direction. It minimises overall head movements by guaranteeing that every request is fulfilled by making a full pass from one end to the other.

- #### Optimized SCAN

    Similar to SCAN, the optimised SCAN algorithm determines the direction depending on the starting head position in an intelligent manner, therefore reducing head movements even further. Processing requests on one side of the head first, it then proceeds to the other end and finishes with the remaining demands.

- #### C-SCAN (Circular Scan)
    
    Using the disc as a circular list, the C-SCAN algorithm services queries in a single direction only—usually towards the outer edge—before returning to the start to handle requests again. Though it requires more head motions than SCAN, this guarantees a more consistent wait time for requests.

- #### Optimized C-SCAN
    
    While using the same circular method as C-SCAN, the optimised C-SCAN algorithm further reduces head movements by processing requests in a way that minimises unnecessary leaps. It arranges and processes the requests to guarantee effective use of the disc head's trip.

## File Structure

- diskScheduling.py: program containing the implementation of all disk scheduling algorithms in Python language
- generateRandom.py: program containing code to generate a random series of 1000 cylinder requests (from 0 to 4999)
- requests.txt: file containing all the requests (separated by line)

## How to Run

Run this command to generate a random series of 1000 cylinder requests (ranging from 0 to 4999)

```python3 generateRandom.py```

Run this command to run and see the output of the program

```python3 diskScheduling.py <initial_head> requests.txt```

## Screenshot of the Output

![Screenshot of the Output](/output.png)