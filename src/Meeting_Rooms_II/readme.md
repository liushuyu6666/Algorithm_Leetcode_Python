# types
## get in and get off
Think of it as entering a bus, exiting the bus, and counting the remaining passengers. The concept is straightforward: when a new meeting begins, eliminate meeting rooms that have already ended before the start time of the new meeting. Various algorithms can be applied based on how the end times of the meetings are stored.

# algorithms
## min heap
Utilizing a min-heap to manage the end times of meeting rooms, we check whether the earliest end time (top value) precedes the start time of a new meeting. If so, we can close an existing meeting room by popping its end time and adding the end time of the new meeting. If not, we simply add a new element to the heap, representing the end time of the new meeting. 

The min-heap here is solely responsible for storing and efficiently retrieving the earliest close time. The underlying concept remains consistent: close a meeting room if possible when a new meeting is scheduled.

## sorted array
Utilizing two sorted arrays is a straightforward approach. Simply sort arrays for start times and end times. Refer to the code for further details.

## differences array
This solution draws parallels with the approach in [car pooling](../Car_Pooling/readme.md#differences-array).