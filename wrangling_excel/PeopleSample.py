import os 
import pandas as pd 
import xlrd


# Tutorial: https://medium.com/@tanyashapiro_72192/scraping-excel-data-with-python-41725308d9b0


print("clean PeopleSample.xlsx")

wb = xlrd.open_workbook('PeopleSample.xlsx')

#To get sheet by index (starts with 0)
ws = wb.sheet_by_index(0)

print(ws)


#get list of values in row
row6 = ws.row_values(6)
print("row6: " + str(row6))
#get list of values in column
col0 = ws.col_values(0)
print("column0: " + str(col0))



def get_value(worksheet, attribute_column, attribute_name):
    attributes = worksheet.col_values(attribute_column)
    if attribute_name in attributes:
        attribute_index = attributes.index(attribute_name)
        #assume value is in the adjacent column where attribute is stored
        values = worksheet.col_values(attribute_column+1)
        value = values[attribute_index]
        return value
    else:
        return None

# Get column 0 from row which contains first name...
func_out = get_value(ws,0,'First Name')
print("column 0 of first name: " + str(func_out))




# ========== loop through all files in current directory ======

for root, dirs, files in os.walk('.'):
    attributes = ['First Name', 'Last Name', 'Sex','City','State']
    #initialized dictionary, create empty list for attributes with dict comprehension
    data = {attribute: [] for attribute in attributes}
    #append a key:value for File, will use this as unique identifier/index
    data.update({"File": []})
    
    for file_name in files:
        print(file_name)
        if file_name == "Peoplesample.xlsx":
            wb = xlrd.open_workbook(file_name)
            ws = wb.sheet_by_index(0)
            data['File'].append(file_name)
            for attribute in attributes:
                data[attribute].append(get_value(ws,0,attribute))

df = pd.DataFrame.from_dict(data)
print(df)
