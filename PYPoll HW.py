import os
import csv

electionCSV = os.path.join('..','Documents','election_data_2.csv')

candidates = ["Correy", "Khan", "Li", "O'Tooley"]

for candidates_to_check in candidates:
    
    candidate = []
    votes = []
    vote_percent = []
    county = []
    total_votes = []
    
    with open('Documents/election_data_2.csv') as csvfile:
    	readCSV = csv.reader(csvfile, delimiter=',')
    	total_votes = len(list(readcsv))
    
    print(total_votes)
        
        next(readCSV, None)
        
        for row in readCSV:
            
            votes.append(row[0])
            county.append(row[1])
            candidates.append(row[2])
            
            winPercent.append(int(row[0])/(int(row[0]
           
