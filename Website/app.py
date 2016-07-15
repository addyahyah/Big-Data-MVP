from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps
import pandas as pd

app = Flask(__name__)

# take instructor data input here
data = pd.DataFrame.from_csv('/home/jupyterflow/Documents/Big-Data-MVP/Teacher_Eval_Analysis/Shibberu_CourseEvalData_Raw_20160616.csv',index_col=None)

data = data[['SURVEY_NAME','COURSE','QUESTION_NO','RESPONSE_1_COUNT','RESPONSE_2_COUNT','RESPONSE_3_COUNT','RESPONSE_4_COUNT','RESPONSE_5_COUNT']] # only taking the needed columns
data = data[data.QUESTION_NO < 4] # removed non-standard evaluation questions

def collectEvalByYear(year, data):
	if year is not None:
		data = data[data.SURVEY_NAME.str.contains('_' + year)]
	return getDataCsv(data)

def collectEvalByCourse(course, data):
	if course is not None:
		data = data[data.COURSE.str.startswith(course)]
	return getDataCsv(data)

def getDataCsv(data):
	# question description dictionary
	questions = {1.04:'Quality of learning',
	             2.03:'Lab and course reinforce',
	             2.06:'Lighter Workload',
	             2.07:'Course overall',
	             3.02:'Professor well-prepared',
	             3.04:'Helpful teaching methods',
	             3.07:'Professor availability',
	             3.09:"Professor's interest in topic",
	             3.1:'Professor overall'}

	# total response counts/question
	lickert_counts = data.drop(['SURVEY_NAME','COURSE'],1).groupby('QUESTION_NO').sum()

	# order response columns 'worst' --> 'best'
	lickert_counts = lickert_counts[lickert_counts.columns[::-1]]

	# total responses per question (used for D3 percentages chart)
	lickert_counts['TOTAL'] = lickert_counts.sum(axis=1)
	lickert_counts = lickert_counts.reset_index()

	# Changing data labels for D3 integration
	lickert_counts['QUESTION_NO'] = lickert_counts['QUESTION_NO'].replace(questions)
	# Setting .csv file format
	lickert_counts.columns = ['Question','1','2','3','4','5','N']
	lickert_counts.set_index('Question')
	return lickert_counts.to_csv(index=False)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/byYear/<year>")
def byYear(year):
	if year == "all":
		year = "";
	return collectEvalByYear(year, data)

@app.route("/byCourse/<course>")
def byCourse(course):
	if course == "all":
		course = "";
	return collectEvalByCourse(course, data)

@app.route("/new_index.html")
def getEval():
    return render_template("new_index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)