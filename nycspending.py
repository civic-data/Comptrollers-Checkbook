import Comptroller
from lxml import etree
from io import StringIO, BytesIO

object = Comptroller.Spending('API ID' , 'API Key')


#print object
#help(object)

# spending.
object.add_response_column('name')
object.add_response_column('spending_category')
object.add_response_column('check_amount')
### 
###        object.create_response_column('name')
###  |      agency, fiscal_year, spending_category,
###  |      document_id, payee_name, check_amount,
###  |      department, expense_category,
###  |      calendar_year, contract_id, purpose,
###  |      issue_date, capital_project
### 
xml=object.getSpending()
root = etree.fromstring(xml)
result=etree.tostring(root,pretty_print=True,method='xml')
print result
