#!/usr/bin/env python
import sys
import Comptroller
from lxml import etree
from lxml import objectify
from io import StringIO, BytesIO
import csv

object = Comptroller.Spending('API ID' , 'API Key')

#print object
#help(object)

csvwriter = csv.writer(sys.stdout,delimiter=',', quotechar='"')

object.add_response_column('name')
object.add_response_column('spending_category')
object.add_response_column('check_amount')

for i in range(0,10809437,1000):
#for i in range(0,1000000,1000):
# spending.

    object.delete_criteria('record_from')
    object.add_criteria('record_from',i)

### 
###        object.create_response_column('name')
###  |      agency, fiscal_year, spending_category,
###  |      document_id, payee_name, check_amount,
###  |      department, expense_category,
###  |      calendar_year, contract_id, purpose,
###  |      issue_date, capital_project
### 
    xml=object.getSpending()
# print xml

    xml=xml.replace('Status Code: 200','')
    root = etree.fromstring(xml)

#root = objectify.fromstring(xml)
#print root

    result=etree.tostring(root,pretty_print=True,method='xml')
#print result
# objects = objectify.dump(root)
# print objects
### for item in objects:
###     print item
### for item in root:
###     print item.tag,item

    first=True

    for b in root.iterfind(".//transaction"):
        header=[]
        row=[]
        #print b.tag,b.items(),b.itertext(),b.keys(),b.findall('*')
        for c in b.findall('*'):
            if first:
                header.append(c.tag)
            row.append(c.text)

        if first:
            first=False
            csvwriter.writerow(header)
        csvwriter.writerow(row)
