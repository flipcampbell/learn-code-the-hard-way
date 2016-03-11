import time
def query():
    choice = raw_input("Are you smart? Y or N. ")
    if choice.upper() in {'Y', 'YES', 'YA', 'YEAH', 'YEA', 'YAH'}:
        print "You have selected \'%s\'. I'm going to assume you meant \'Y\'.\nYou are smart." % choice   
    elif choice.upper() in {'N', 'NO', 'NEGATIVE', 'NEIN', 'NOT', 'NAH', 'NAW'}:
        print "You have selected \'%s\'. I'm going to assume you meant \'N\'.\nYou are not smart." % choice
    else:
        print "\'%s\' is not a valid response. Try Again." % choice
        i = 0       
        while (i < 9):
            print '.'
            time.sleep(0.15)
            i = i + 1
        query()         
        
query()        
