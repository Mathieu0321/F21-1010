
filepath = 'sample.txt'
with open(filepath) as fp:
    line = fp.readline()
    line_no = 0
    while line:
        line_no = line_no + 1

        # Process the line
        print("Line {}: {}".format(line_no, line.strip()))

        # Read in next line
        line = fp.readline()
