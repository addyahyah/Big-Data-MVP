# Course Evaluation Data Analysis
## Synopsis
This project was started in Summer 2016 to promote the existence and usage of Big Data at Rose-Hulman Institute of Technology. To this end, Professor Yosi Shibberu agreed to release all of his Student Course Evaluation data for school years since 2004-05. Using the provided data as the basis, the files in this folder are an analysis tool for other professors of Rose-Hulman to visualize their Evaluation data either cumulatively or aggregated by year or course in the form of diverging stacked bar charts.

## Dependencies
Most of the below packages should come included with [Anaconda](https://www.continuum.io/downloads) unless otherwise noted:
- Python 3.5+
- [matplotlib](http://matplotlib.sourceforge.net)
- [pandas](http://pandas.pydata.org/)
- [jupyter notebook](http://jupyter.org/)
- [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/user_install.html) *must be installed separately*
Also, please make sure your data files have the same layout and format as the provided `Shibberu_CourseEvalData_Raw_20160616.csv` example file. Since the data usually comes as an .xlxs Excel file, open the given file and check the data headers, then save a .csv copy to this directory.

## Instructions
Within this folder, there are two main methods of running analysis on data:
### High-Level Dashboard
The `Course_Evaluation_Data_Dashboard.ipynb` file uses widget options to call the `data_analysis.ipynb` and `nbrun.py` files to do analysis on the data input. To add your own data, change the `filename` variable in the below cell to your own .csv data file within the worksheet:
```python
# MODIFY THIS CELL FIRST
filename = "Shibberu_CourseEvalData_Raw_20160616.csv" # Make sure this is a String
print("Evaluating data for: " + filename)
```
Then go to the `Cell` menu and choose `Run All` to select options and get chart outputs.
### Low-Level Data Analysis
Alternatively, the `data_analysis.ipynb` notebook can be used on its own, apart from the main dashboard, with working knowledge of the `pandas` data analysis library and the Course Evaluation data itself.  The data file, year, and course options can be changed manually in the Instructor Data Input cell:
```python
# INSTRUCTOR DATA INPUT
data = pd.DataFrame.from_csv('Shibberu_CourseEvalData_Raw_20160616.csv',index_col=None)
course = None # must be a String or None
year = None # must be a String or None
```
Modifying this cell also changes the defaults for `Course_Evaluation_Data_Dashboard.ipynb`. However, since the Dashboard depends on the code in this notebook, it would be safest to first **make a copy** of `data_analysis.ipynb` and **use the copy** for modifications beyond the Instructor Data Input cell and for custom analysis.

## License
The MIT License (MIT)  
Copyright (c) 2016 Anna Scott

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
