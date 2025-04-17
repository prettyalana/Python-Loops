sample_string = "Hej, hur mår du? Jag mår bra! Tack!"

sample_string_length = len(sample_string)

counter = 0

while counter < sample_string_length :
      
    if counter % 2 == 0 and sample_string[counter] != " "  :
        print(sample_string[counter])
        
    counter += 1
    