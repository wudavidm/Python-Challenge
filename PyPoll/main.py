# Operating System
import os

# import file
import csv

csvpath = os.path.join("..", "PyPoll", "polldata.csv")

# set variables
votes = []
percent = {}
khan = 0
correy = 0
li = 0
otooley = 0

# Open the CSV
with open('polldata.csv') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")

    # Loop and read lines in CSV
    for row in csvreader:
        # Create list for Voters
        votes.append(row['Voter ID'])
        # Set rules for outcomes and add to counter
        if row['Candidate'] == 'Khan':
            khan = khan + 1
        elif row['Candidate'] == 'Correy':
            correy = correy + 1
        elif row['Candidate'] == 'Li':
            li = li + 1
        else:
            otooley = otooley + 1

    # Calculate
    pk = (khan/len(votes))
    pc = (correy/len(votes))
    pl = (li/len(votes))
    po = (otooley/len(votes))

    # Add to dictionary
    percent['Khan'] = pk
    percent['Correy'] = pc
    percent['Li'] = pl
    percent["O'Toole"] = po





# Print results
print('Total Votes:', len(votes))
print('Khan:', "{:.1%}".format(pk), khan)
print('Correy:', "{:.1%}".format(pc), correy)
print('Li:', "{:.1%}".format(pl), li)
print("O'Tooley", "{:.1%}".format(po), otooley)
print(max(percent, key=percent.get))


# Write to text file
with open('pypollmain.txt', 'w') as f:
    f.write('"Total Votes:", len(votes)\n')
    f.write('"Khan:", "{:.1%}".format(pk), khan\n')
    f.write('"Correy:", "{:.1%}".format(pc), correy\n')
    f.write('"Li:", "{:.1%}".format(pl), li\n')
    f.write('"OTooley", "{:.1%}".format(po), otooley\n')
    f.write('max(percent, key=percent.get)\n')
