import pandas as pd
# take instructor data input here
data = pd.DataFrame.from_csv('/home/jupyterflow/Documents/Big-Data-MVP/Teacher_Eval_Analysis/Shibberu_CourseEvalData_Raw_20160616.csv',index_col=None)
data = data[['SURVEY_NAME','COURSE','QUESTION_NO','RESPONSE_1_COUNT','RESPONSE_2_COUNT','RESPONSE_3_COUNT',
             'RESPONSE_4_COUNT','RESPONSE_5_COUNT']] # only taking the needed columns
data = data[data.QUESTION_NO < 4] # removed non-standard evaluation questions


def collectEvalByYear(year):
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
