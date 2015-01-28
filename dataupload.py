#!/usr/bin/env python
__author__ = 'nitin'

#Example: python dataupload.py gensql --datafile csvfile1.csv --dbtype MSSQL --outfile datascript1.sql --table Emp

import aaargh
import csv

app = aaargh.App(description='CSV Data Uploader')

@app.cmd
@app.cmd_arg('--datafile', help='Path to the CSV file')
@app.cmd_arg('--dbtype', help='Type of database', default='MSSQL')
@app.cmd_arg('--outfile', help='Path to the output file', default='datascript.sql')
@app.cmd_arg('--table', help='Type of database', default='Table1')
def gensql(datafile, dbtype, outfile, table):
    if datafile is None:
        print('A datafile containing the input CSV must be specified')
        exit(-1)
    print('Datafile is %s, DB Type is %s, Outfile is %s' % (datafile, dbtype, outfile))
    #print(datafile)


def action_gensql(datafile, dbtype, outfile, table):
    with open(datafile, 'r') as fh:
        csvread = csv.reader(fh)
        is_first_row = True
        sqltxt = ''
        colnamecsv = ''
        colnamearr = None
        for row in csvread:
            if is_first_row:
                is_first_row = False
                colnamearr = row
                colnamecsv = ','.join(colnamearr)
                continue
            dataarr = row
            for i in len(dataarr):
                #If it is not numeric, add quotes
                pass
            valcsv = '\'' + '\',\''.join(dataarr) + '\''
            #valcsv = ','.join(dataarr)
            sqltxt += 'insert into %s (%s) values (%s);' % (table, colnamecsv, valcsv)
            sqltxt += '\r\n'


if __name__ == '__main__':
    app.run()