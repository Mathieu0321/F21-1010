
filepath = 'sample.txt'
with open(filepath) as fp:
   line = fp.readline()
   line_no = 1
   while line:
       print("Line {}: {}".format(line_no, line.strip()))
       line = fp.readline()
       line_no = line_no + 1
