sample_file = input("Enter a file name: ")
open(sample_file)
# The following function takes a file from the command line as the input, reads
# and splits each line, and converts the string values of each line into float values.
# Then, the function adds the float values for each line and returns the sum of the two values
# for each line as the output.
with open(sample_file) as file:
    try:
        for line in file:
            numbers = line.split()
            sum = float(numbers[0]) + float(numbers[1])
            print(sum)
    except:
        print("An error occurred.")
        exit

# Test results:
# 1. The file sample_1 was the first file called. The function returned 6.0,
# 12.0, -2.0, and 10.0, successfully adding the numbers on each line accurately.
# 2. The file sample_2 was the second file called. The function returned 18.0
# for the first line and then returned "An error occurred." when reading the second line.
# This was the expected output.
# The two tests were successful.