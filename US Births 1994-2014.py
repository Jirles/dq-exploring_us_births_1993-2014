
# coding: utf-8

# ## CDC Births 1994-2003
# 
# Documents, challenges come from Dataquest Intro to Python course. This guided project including reading a csv file, calculating number of births per year, month, day of week, and day of month, and included additional challenges to tackle on my free time. The additional challenges will be listed below in a later write-up. A link to the solutions to this lab can be found [here](https://github.com/dataquestio/solutions/blob/master/Mission9Solutions.ipynb).
# 
# ### Structure of CSV File
# The csv file entitled `US_births_1994-2003_CDC_NCHS.csv`, besides containing comma-separated values, is also split by date by the newline symbol `\n`. The headers in this file are as follows:
# 
# - `year`: Four digits denoting year of birth at **index 0**
# - `month`: one to two digits denoting month of birth at **index 1**
# - `date_of_month`: one to two digits denoting the date of birth at **index 2**
# - `day_of_week`: one digits between one and seven, where one is Monday and seven is Sunday at **index 3**
# - `births`: one integer containing the number of births recorded on that day at **index 4**
# 
# Each instance of a date thus contains five (5) integers representing the date and the number of births that occurred separated by commas. To facilitate analysis, the file had to be split along the newline breaks and the header line was removed. The resulting list is then manipulated so that each string element representing the date and birth count are split at their commmas, converted into integers and inserted into a new list which is in turn appended to final list of lists that contains all the dates originally listed in the csv file. The code to accomplish this is below.

# In[1]:


def read_csv(file_name):
    f = open(file_name, 'r')
    a = f.read()
    newline = a.split('\n')
    string_list = newline[1:]
    final_list = []
    for string in string_list:
        int_fields = []
        string_fields = string.split(',')
        for value in string_fields:
            number = int(value)
            int_fields.append(number)
        final_list.append(int_fields)
    return final_list


cdc_list = read_csv('US_births_1994-2003_CDC_NCHS.csv')
cdc_list[0:10]


# In[2]:


#Calculating the number of births according to different parameters

def calc_counts(data, column):
    '''
    data is a list of lists
    column is an integer (index) representing the column by which the births should tallied
    function returns a dictionary where the keys are column values and the values are the total births
    '''
    calc_dict = {}
    for item in data:
        if item[column] in calc_dict.keys():
            calc_dict[item[column]] += item[4]
        else:
            calc_dict[item[column]] = item[4]
    return calc_dict

#births/year
cdc_year_births = calc_counts(cdc_list, 0)
#births/month
cdc_month_births = calc_counts(cdc_list, 1)
#births/day of the month
cdc_dom_births = calc_counts(cdc_list, 2)
#births/day of the week
cdc_dow_births = calc_counts(cdc_list, 3)


# In[3]:


cdc_year_births


# In[4]:


cdc_month_births


# In[5]:


cdc_dom_births[0:10]


# ## Additional Work
# 
# After conditioning the data and writing a function to total the births per column, Dataquest suggested work for further practice. Their suggestions are: 
# 
# 1. Write a function that can calculate the min and max values for any dictionary that's passed in.
# 
# 2. Write a function that extracts the same values across years and calculates the differences between consecutive values to show if number of births is increasing or decreasing.
#     1. For example, how did the number of births on Saturday change each year between 1994 and 2003?
# 
# 3. Find a way to combine the CDC data with the SSA data (another csv file downloaded with the CDC file, but which covers the years 2000-2014). Specifically, brainstorm ways to deal with the overlapping time periods in the datasets.
# 

# In[6]:


def minimum_calc(dict):
    temp = []
    for value in dict.values():
        temp.append(value)
    return min(temp)

def maximum_calc(dict):
    temp = []
    for value in dict.values():
        temp.append(value)
    return max(temp)

cdc_month_births_min = minimum_calc(cdc_month_births)


# In[7]:


cdc_month_births_min


# In[8]:


cdc_month_births_max = maximum_calc(cdc_month_births)
cdc_month_births_max


# In[9]:


def percentage_change_calc(data, date_value, column_index):
    '''
    function that extracts the same values across years and calculates the differences between consecutive values 
    to show if number of births is increasing or decreasing
    
    data: list of lists
    date_value: integer that stands for the date value by which one wishes to calculate percentages; for example, 3
        would represent March if one was looking at months
    column_index: postive integer representing the column in which the constraint is located
    function returns a dictionary where the keys are years and the values are the percentage change between the key
    year and the year previous.
    '''
    totals = {}
    percentages = {}
    #iterate over data to get into each list containing date data
    for item in data:
        #find those dates that have the same year(at index 0) and constraint at the column index
        #will need to add totals together per year
        if item[column_index] == date_value:
            if item[0] in totals.keys():
                totals[item[0]] += item[4]
            else:
                totals[item[0]] = item[4]
    #then will need to go through totals to calculate percentages, add percentages, limit to 2 decimal places, to 
    #percentages according to year, note that the first year (1994 in this case) will not be included
    index = 0
    while index+1 < len(totals.keys()):
        #rounding percentages to 2 decimal places
        percentages[totals.keys()[index+1]] = round((totals[[totals.keys()[index+1]]] - totals[[totals.keys()[index]]])/totals[[totals.keys()[index]]], 2)
        index += 1
    return percentages
    
# initially trying to answer this question: 
# how did the number of births on Saturday change each year between 1994 and 2003
# Saturday = 6, dow = column (index) 3
cdc_Sat_percent_change = percentage_change_calc(cdc_list, 6, 3)


# In[10]:


#testing some key things to fix above function
test_keys = cdc_month_births.keys()
cdc_month_births


# In[11]:


test_keys


# In[12]:


test_keys[0]


# In[18]:


test_keys_array = []
for key in cdc_month_births.keys():
    test_keys_array.append(key)

test_keys_array
    


# In[23]:


list(cdc_month_births)


# In[19]:


def percentage_change_calc(data, date_value, column_index):
    '''
    function that extracts the same values across years and calculates the differences between consecutive values 
    to show if number of births is increasing or decreasing
    
    data: list of lists
    date_value: integer that stands for the date value by which one wishes to calculate percentages; for example, 3
        would represent March if one was looking at months
    column_index: postive integer representing the column in which the constraint is located
    function returns a dictionary where the keys are years and the values are the percentage change between the key
    year and the year previous.
    '''
    totals = {}
    percentages = {}
    #iterate over data to get into each list containing date data
    for item in data:
        #find those dates that have the same year(at index 0) and constraint at the column index
        #will need to add totals together per year
        if item[column_index] == date_value:
            if item[0] in totals.keys():
                totals[item[0]] += item[4]
            else:
                totals[item[0]] = item[4]
    #then will need to go through totals to calculate percentages, add percentages, limit to 2 decimal places, to 
    #percentages according to year, note that the first year (1994 in this case) will not be included
    totals_keys = list(totals) # creates list of keys that can be indexed into
    index = 0
    while index+1 < len(totals_keys):
        #rounding percentages to 2 decimal places
        percentages[totals_keys[index+1]] = round((totals[totals_keys[index+1]] - totals[totals_keys[index]])/totals[totals_keys[index]], 2)
        index += 1 
    return percentages
    
# initially trying to answer this question: 
# how did the number of births on Saturday change each year between 1994 and 2003
# Saturday = 6, dow = column (index) 3
cdc_Sat_percent_change = percentage_change_calc(cdc_list, 6, 3)


# In[20]:


cdc_Sat_percent_change


# In[24]:


cdc_dow_births


# In[25]:


#essentially the totals list from the percentage_change_ calc function
totals = {}   
for item in cdc_list:
    if item[3] == 6:
        if item[0] in totals.keys():
            totals[item[0]] += item[4]
        else:
            totals[item[0]] = item[4]
totals


# In[3]:


#after some calculations with the calculator to check code, changing percentage_change_calc function to 
#round to 4 decimal places and multiplying by 100 to get proper percentage
#also deleting a lot of pseudocode 
def percentage_change_calc(data, date_value, column_index):
    '''
    function that extracts the same values across years and calculates the differences between consecutive values 
    to show if number of births is increasing or decreasing
    
    data: list of lists
    date_value: integer that stands for the date value by which one wishes to calculate percentages; for example, 3
        would represent March if one was looking at months
    column_index: postive integer representing the column in which the constraint is located
    
    function returns a dictionary where the keys are years and the values are the percentage change between the key
    year and the year previous
    '''
    totals = {}
    percentages = {}
    for item in data:
        if item[column_index] == date_value:
            if item[0] in totals.keys():
                totals[item[0]] += item[4]
            else:
                totals[item[0]] = item[4]
    totals_keys = list(totals) # creates list of keys that can be indexed into
    index = 0
    while index+1 < len(totals_keys):
        #rounding percentages to 3 decimal places
        percentages[totals_keys[index+1]] = round((totals[totals_keys[index+1]] - totals[totals_keys[index]])/totals[totals_keys[index]], 3)*100
        index += 1 
    return percentages

# Saturday = 6, dow = column (index) 3
cdc_Sat_percent_change = percentage_change_calc(cdc_list, 6, 3)


# In[4]:


cds_data_list = read_csv('US_births_1994-2003_CDC_NCHS.csv')


# ## Merging Data Sets
# 
# The final task from the Dataquest mission was to find a way to merge the cdc and ssa datasets:
# 
# * Find a way to combine the CDC data with the SSA data (another csv file downloaded with the CDC file, but which covers the years 2000-2014). **Specifically, brainstorm ways to deal with the overlapping time periods in the datasets.**
# 
# #### Ideas
# 
# 1. Use current functions to create dictionaries of the two data sets then play around with the years that overlap. 
#     1. Could average the two results. (I like this one best)
#     2. Could display values as a range.
#     3. Could have one of the datasets be dominant. (I don't really like this option)
# 2. Alter lists in beginning so that the cdc and ssa data are read into the same file.
#     1. But would that be problematic from a data providence point of view? I still have the csv's...

# In[5]:


#Function reload. 
def read_csv(file_name):
    f = open(file_name, 'r')
    a = f.read()
    newline = a.split('\n')
    string_list = newline[1:]
    final_list = []
    for string in string_list:
        int_fields = []
        string_fields = string.split(',')
        for value in string_fields:
            number = int(value)
            int_fields.append(number)
        final_list.append(int_fields)
    return final_list

def calc_counts(data, column):
    '''
    data is a list of lists
    column is an integer (index) representing the column by which the births should tallied
    function returns a dictionary where the keys are column values and the values are the total births
    '''
    calc_dict = {}
    for item in data:
        if item[column] in calc_dict.keys():
            calc_dict[item[column]] += item[4]
        else:
            calc_dict[item[column]] = item[4]
    return calc_dict

def minimum_calc(dict):
    temp = []
    for value in dict.values():
        temp.append(value)
    return min(temp)

def maximum_calc(dict):
    temp = []
    for value in dict.values():
        temp.append(value)
    return max(temp)

def percentage_change_calc(data, date_value, column_index):
    '''
    function that extracts the same values across years and calculates the differences between consecutive values 
    to show if number of births is increasing or decreasing
    
    data: list of lists
    date_value: integer that stands for the date value by which one wishes to calculate percentages; for example, 3
        would represent March if one was looking at months
    column_index: postive integer representing the column in which the constraint is located
    
    function returns a dictionary where the keys are years and the values are the percentage change between the key
    year and the year previous
    '''
    totals = {}
    percentages = {}
    for item in data:
        if item[column_index] == date_value:
            if item[0] in totals.keys():
                totals[item[0]] += item[4]
            else:
                totals[item[0]] = item[4]
    totals_keys = list(totals) # creates list of keys that can be indexed into
    index = 0
    while index+1 < len(totals_keys):
        #rounding percentages to 3 decimal places
        percentages[totals_keys[index+1]] = round((totals[totals_keys[index+1]] - totals[totals_keys[index]])/totals[totals_keys[index]], 3)*100
        index += 1 
    return percentages


# In[6]:


cdc_data = read_csv('US_births_1994-2003_CDC_NCHS.csv')
ssa_data = read_csv('US_births_2000-2014_SSA.csv')


# In[7]:


cdc_data[0:10]


# In[8]:


ssa_data[0:10]


# In[28]:


def calc_total_sec_arg(data, group_by_index, count_index, count_value):
    '''
    data: list of lists
    group_by_index: integer, index by which to group data totals, serve as keys in totals dictionary; name take from 
    GROUP BY SQL command
    count_index: integer, secondary index by which totals are calculated; name taken from COUNT SQL command
    count_value: integer, condition to be met to supplement totals; name taken from COUNT SQL command
    
    function returns a dictionary a totals calculated by the count_value and grouped by the group_by_index. 
    function should be used in lieu of calc_counts when an additional arg is needed to parse data, e.g. calculating
        how many births occured in Jan between 1994 and 2003.
    '''
    totals = {}
    for item in data:
        if item[count_index] == count_value:
            if item[group_by_index] in totals.keys():
                totals[item[group_by_index]] += item[4]
            else:
                totals[item[group_by_index]] = item[4]
    return totals


# In[37]:


def percentage_change_test(input_dict):
    '''
    function that extracts the same values across years and calculates the differences between consecutive values 
    to show if number of births is increasing or decreasing
    
    data: list of lists
    date_value: integer that stands for the date value by which one wishes to calculate percentages; for example, 3
        would represent March if one was looking at months
    column_index: postive integer representing the column in which the constraint is located
    
    function returns a dictionary where the keys are years and the values are the percentage change between the key
    year and the year previous
    '''
    percentages = {}
    keys_list = list(input_dict) # creates list of keys that can be indexed into
    index = 0
    while index+1 < len(keys_list):
        #rounding percentages to 3 decimal places
        percentages[keys_list[index+1]] = round((input_dict[keys_list[index+1]] - input_dict[keys_list[index]])/input_dict[keys_list[index]], 3)*100
        index += 1 
    return percentages


# In[36]:


# Saturday = 6, dow = column (index) 3
cdc_Sat_percent_current = percentage_change_calc(cdc_data, 6, 3)
cdc_Sat_percent_current


# In[39]:


cdc_Sat_percent_test = percentage_change_test(calc_total_sec_arg(cdc_data, 0, 3, 6))


# In[40]:


cdc_Sat_percent_test


# In[41]:


#updating function list to include calc_total_sec_arg (really ugly-ass name) 
#simplifies calculating percentage changes function so that it only takes in a dictionary
def percentage_change_calc(input_dict):
    '''
    function that extracts the same values across years and calculates the differences between consecutive values 
    to show if number of births is increasing or decreasing
    
    data: list of lists
    date_value: integer that stands for the date value by which one wishes to calculate percentages; for example, 3
        would represent March if one was looking at months
    column_index: postive integer representing the column in which the constraint is located
    
    function returns a dictionary where the keys are years and the values are the percentage change between the key
    year and the year previous
    '''
    percentages = {}
    keys_list = list(input_dict) # creates list of keys that can be indexed into
    index = 0
    while index+1 < len(keys_list):
        #rounding percentages to 3 decimal places
        percentages[keys_list[index+1]] = round((input_dict[keys_list[index+1]] - input_dict[keys_list[index]])/input_dict[keys_list[index]], 3)*100
        index += 1 
    return percentages


# In[42]:


#updated list of functions thus far: 
def read_csv(file_name):
    f = open(file_name, 'r')
    a = f.read()
    newline = a.split('\n')
    string_list = newline[1:]
    final_list = []
    for string in string_list:
        int_fields = []
        string_fields = string.split(',')
        for value in string_fields:
            number = int(value)
            int_fields.append(number)
        final_list.append(int_fields)
    return final_list

def calc_counts(data, column):
    '''
    data is a list of lists
    column is an integer (index) representing the column by which the births should tallied
    function returns a dictionary where the keys are column values and the values are the total births
    '''
    calc_dict = {}
    for item in data:
        if item[column] in calc_dict.keys():
            calc_dict[item[column]] += item[4]
        else:
            calc_dict[item[column]] = item[4]
    return calc_dict

def calc_total_sec_arg(data, group_by_index, count_index, count_value):
    '''
    data: list of lists
    group_by_index: integer, index by which to group data totals, serve as keys in totals dictionary; name take from 
    GROUP BY SQL command
    count_index: integer, secondary index by which totals are calculated; name taken from COUNT SQL command
    count_value: integer, condition to be met to supplement totals; name taken from COUNT SQL command
    
    function returns a dictionary a totals calculated by the count_value and grouped by the group_by_index. 
    function should be used in lieu of calc_counts when an additional arg is needed to parse data, e.g. calculating
        how many births occured in Jan between 1994 and 2003.
    '''
    totals = {}
    for item in data:
        if item[count_index] == count_value:
            if item[group_by_index] in totals.keys():
                totals[item[group_by_index]] += item[4]
            else:
                totals[item[group_by_index]] = item[4]
    return totals

def minimum_calc(dict):
    temp = []
    for value in dict.values():
        temp.append(value)
    return min(temp)

def maximum_calc(dict):
    temp = []
    for value in dict.values():
        temp.append(value)
    return max(temp)

def percentage_change_calc(input_dict):
    '''
    function that extracts the same values across years and calculates the differences between consecutive values 
    to show if number of births is increasing or decreasing
    
    data: list of lists
    date_value: integer that stands for the date value by which one wishes to calculate percentages; for example, 3
        would represent March if one was looking at months
    column_index: postive integer representing the column in which the constraint is located
    
    function returns a dictionary where the keys are years and the values are the percentage change between the key
    year and the year previous
    '''
    percentages = {}
    keys_list = list(input_dict) # creates list of keys that can be indexed into
    index = 0
    while index+1 < len(keys_list):
        #rounding percentages to 4 decimal places
        percentages[keys_list[index+1]] = round((input_dict[keys_list[index+1]] - input_dict[keys_list[index]])/input_dict[keys_list[index]], 4)*100
        index += 1 
    return percentages


# In[44]:


#back to the problem at hand: dealing with the two data sets
def merge_results(dict1, dict2):
    '''
    dict1, dict2: dictionaries with integer values and some overlapping keys
    
    function returns a dictionary that has combined the two datasets together; where keys from both dicts overlap, an
    average of the original values is returned
    '''
    # copy one dictionary to the result dictionary
    result = dict1.copy()
    # add dict2 in one entry at a time, 
    for key in dict2:
        if key in result:
            #add an average of the values from both datasets, round to 4 digits
            result[key] = round((result[key] + dict2[key]) / 2, 4)
        else:
            #else just add the item to the result dictionary
            result[key] = dict2[key]
    return result


# In[46]:


#testing merge_results with simple dictionaries
test_dict1 = {1: 1, 2: 2, 3: 3, 4: 4}
test_dict2 = {3: 5, 4: 2, 5: 4, 6: 7}

#expected to return: {1:1, 2:2, 3:4, 4:2, 5:4, 6:7}
test_merge = merge_results(test_dict1, test_dict2)
test_merge


# In[47]:


cdc_year_births = calc_counts(cdc_data, 0)
ssa_year_births = calc_counts(ssa_data, 0)


# In[48]:


cdc_year_births


# In[49]:


cdc_year_births


# In[50]:


cdc_ssa_year_births = merge_results(cdc_year_births, ssa_year_births)


# In[51]:


cdc_ssa_year_births

