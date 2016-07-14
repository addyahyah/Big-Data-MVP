from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps
# import produce_D3_data
import pandas as pd

app = Flask(__name__)

# MONGODB_HOST = 'localhost'
# MONGODB_PORT = 27017
# DBS_NAME = 'donorschoose'
# COLLECTION_NAME = 'projects'
# FIELDS = {'school_state': True, 'resource_type': True, 'poverty_level': True, 'date_posted': True, 'total_donations': True, '_id': False}

def collectEvalByYear(year):
	# take instructor data input here
	data = pd.DataFrame.from_csv('/home/jupyterflow/Documents/Big-Data-MVP/Teacher_Eval_Analysis/Shibberu_CourseEvalData_Raw_20160616.csv',index_col=None)
	data = data[['SURVEY_NAME','COURSE','QUESTION_NO','RESPONSE_1_COUNT','RESPONSE_2_COUNT','RESPONSE_3_COUNT',
	             'RESPONSE_4_COUNT','RESPONSE_5_COUNT']] # only taking the needed columns
	data = data[data.QUESTION_NO < 4] # removed non-standard evaluation questions

	if year is not None:
		data = data[data.SURVEY_NAME.str.contains('_' + year)]
	# question description dictionary
	questions = {1.04:'Quality of learning',
	             2.03:'Lab and course reinforce',
	             2.06:'Workload',
	             2.07:'Course overall',
	             3.02:'Professor well-prepared',
	             3.04:'Helpful teaching methods',
	             3.07:'Professor availability',
	             3.09:"Professor's interest in topic",
	             3.1:'Professor overall'}

	# Creating .csv File of Raw Data Counts
	# total response counts/question
	lickert_counts = data.drop(['SURVEY_NAME','COURSE'],1).groupby('QUESTION_NO').sum()

	# order response columns 'worst' --> 'best'
	lickert_counts = lickert_counts[lickert_counts.columns[::-1]]

	# total responses per question (used for D3 percentages chart)
	lickert_counts['TOTAL'] = lickert_counts.sum(axis=1)
	lickert_counts = lickert_counts.reset_index()

	# Changing data labels for D3 integration
	lickert_counts['QUESTION_NO'] = lickert_counts['QUESTION_NO'].replace(questions)
	lickert_counts.columns = ['Question','1','2','3','4','5','N']
	lickert_counts.set_index('Question')
	return lickert_counts.to_csv(index=False)


@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/byYear/<year>")
def byYear(year):
	return collectEvalByYear(year)

@app.route("/new_index.html")
def getEval():
    return render_template("new_index.html")

# @app.route("/donorschoose/projects")
# def donorschoose_projects():
#     connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
#     collection = connection[DBS_NAME][COLLECTION_NAME]
#     projects = collection.find(projection=FIELDS, limit=100000)
#     #projects = collection.find(projection=FIELDS)
#     json_projects = []
#     for project in projects:
#         json_projects.append(project)
#     json_projects = json.dumps(json_projects, default=json_util.default)
#     connection.close()
#     return json_projects

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)