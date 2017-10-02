#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print '数据点（人）数：', len(enron_data)
print '特征数：', len(enron_data[enron_data.keys()[0]])
print '特征数：', len(enron_data['METTS MARK'])

poi_num = 0
for key in enron_data:
    if enron_data.get(key)['poi'] == 1:
        poi_num = poi_num + 1
print 'POI数：', poi_num
