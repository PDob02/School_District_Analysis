# School_District_Analysis

## 1.  **Overview of the school district analysis:** 
The purpose of this analysis is to take a cross-section of charter & district schools in an area based on a number of factors including spending per student, reading & math scores, total school budget & size. There were 15 schools involved in the analysis and close to 40,000 students. We also had an important instance where we had to rule out 461 9th grader's math and reading scores at Thomas High School (enrollment 1635) and then rerun our data with some of those scored omitted. This led to slight change to that charter school and the overall dataset.Please note, all of this scrubbed data was completed in the PyCitySchools_Challenge_2.ipynb file. 

Thomas High School 1st Analysis:
![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/Thomas%20High%20School%20Before%20Analysis.png)

Thomas High School Challenge Analysis (redacted 9th grade):
![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/Thomas%20High%20School%20After%20Analysis.png)
    
## 3.  **Results:**  Using bulleted lists and images of DataFrames as support, address the following questions: 

###### How is the district summary affected? 

The district summary was not significantly affected by the removal of 461 student's scores. There are different numbers in the charter row but they are only slightly changed.This is because the average calculation was spread out amongst a large student base. This was a small around ~1% adjustment that had to be made. 
Average Math Score Charter
![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/Charter%20School%20Analysis%20Before.png)
![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/Charter%20School%20Analysis%20After.png)

Average Math Score Charter
![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/Charter%20School%20Analysis%20After.png)
    
###### How is the school summary affected?

###### How does replacing the ninth graders’ math and reading scores affect Thomas High School’s performance relative to the other schools? 
	The replacement of 461 students in the dataset for Thomas High School was not significant to the overall dataset. It is considered a Charter school and one of the top schools for Overall Passing %. If anything prior to the data being scrubbed the school scored slightly higher in math, reading, and overall but it was not a dramatic difference.
  
###### How does replacing the ninth-grade scores affect the following:
###### Math and reading scores by grade:
This is one of the more significant findings since NaN will show up for 9th graders at Thomas High School
Reading Scores:
![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/Reading%20Scores%20by%20Grade.png)
Math Scores:
![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/Scores%20by%20Grade.png)
###### Scores by school spending:
	School spending was not affected when accounting for rounding. The dollars spent were still spend on the same students and one grade was not enough to change the dataset
Before:
![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/Spending%20Per%20Student%20Before.png)
After:
![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/Spending%20Per%20Student%20After.png)
###### Scores by school Size:
	Since Thomas High School was a medium sized school with an enrollment in the 1600s the only data that was affected was the minor decimal points as illustrated below. 
![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/By%20School%20Size%20Before.png)
![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/By%20School%20Size%20After.png)
###### Scores by school type:
	Though not affected by the Thomas School, the largest gap in the data is the % Overall passing in Charter Schools (90%) vs. District Schools at (54%). 

## 4.  **Summary:**  Summarize four changes in the updated school district analysis after reading and math scores for the ninth grade at Thomas High School have been replaced with NaNs.
The most significant statistical change to the data lies within the Thomas school data itself. This is where the largest deviation on averages stood, though in most cases it was not statitiscally significant to the untrained eye or average parent. Their school's reading and math scores dipped slightly as well as their overall passing percentage. Also, all of the data for ninth graders will populate as NaN or "not a number" in reports now since there were some questions brought up by that school's school board. 

![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/Thomas%20High%20School%20After%20Overall.png)
###### Before Analysis:
  ![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/Thomas%20High%20School%20Before%20Overall.png)
