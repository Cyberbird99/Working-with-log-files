# Prompt for a file to anaylze
log = input("Name a file to analyze.")

# Open the file
f = open(log, "r")

# Read the file line by line
while True:
    line = f.read(line)
    if not line:
        break
    #Check for 403
    if "403" in line:
        print(line.strip())
              
# close the file
f.close()