from StringIO import StringIO
import csv

def getCsv(headers, results):
    # Header
    
    # CSV Stream
    csvstream = StringIO()
    writer = csv.writer(csvstream, dialect='excel',quoting=csv.QUOTE_NONNUMERIC)
    
    # Data Rows
    writer.writerow(headers)
    for row in results:
        line = [str(variable).encode("utf-8") for variable in row]
        writer.writerow(line)
    
    contents = csvstream.getvalue()
    csvstream.close()    
    return contents
