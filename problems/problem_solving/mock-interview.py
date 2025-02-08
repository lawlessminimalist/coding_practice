"""
A software developer needs to secure server-generated log files. Each log file is a long string of digits, with each digit representing an event type. To protect the log data, the log file must be encoded into a secure format.

Given a string, logFile, of length n that consists of digits (0-9), encode the log file securely. The encoding process for each digit x is as follows:

Count the occurrences of x from the current position to the end of the string.

Append the count plus the digit x to the encoded string.

Generate the encoded log file by following these steps for each digit in the string.

**Note:**

The count should consider only the original digits, not those added during the encoding.

The encoded string should preserve the order of the original digits with their respective counts prepended

**Example**

Given logFile = "12727"
"""

def encodeTheLogFile(logFile):
    encoded_string = []
    seen = {}
    length = len(logFile)
    for index in range(length):
        count=0
        previous_cal = seen.get(logFile[index])
        if previous_cal is not None:
            encoded_string.append(str(previous_cal-1))
            encoded_string.append(logFile[index])
            seen.update({logFile[index]:previous_cal-1})
        else:
            for sub_index in range(index,length):
                if logFile[index] == logFile[sub_index]:
                    count+=1
            encoded_string.append(str(count))
            encoded_string.append(logFile[index])
            seen.update({logFile[index]:count})

    return ''.join(encoded_string)


input = "12727"
print(encodeTheLogFile(input))