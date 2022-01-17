# School_District_Analysis

## 1.  **Overview of the school district analysis:** 
The purpose of this analysis is to take a cross-section of charter & district schools in an area based on a number of factors including spending per student, reading & math scores, total school budget & size. There were 15 schools involved in the analysis and close to 40,000 students. We also had an important instance where we had to rule out 461 9th grader's math and reading scores at Thomas High School (enrollment 1635) and then rerun our data with some of those scored omitted. This led to slight change to that charter school and the overall dataset.Please note, all of this scrubbed data was completed in the PyCitySchools_Challenge_2.ipynb file. 

Thomas High School 1st Analysis:
![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/Thomas%20High%20School%20Before%20Analysis.png)

Thomas High School Challenge Analysis (redacted 9th grade):
![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/Thomas%20High%20School%20After%20Analysis.png)
    
## 3.  **Results:**  Using bulleted lists and images of DataFrames as support, address the following questions: 

###### How is the district summary affected? 

The district summary was not significantly affected by the removal of 461 student's scores. There are different numbers in the charter row but they are only slightly changed.
Average Math Score Charter
![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/Charter%20School%20Analysis%20Before.png)

![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/Charter%20School%20Analysis%20After.png)

Average Math Score Charter
![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/Charter%20School%20Analysis%20After.png)
    ###### How is the school summary affected?

    ###### How does replacing the ninth graders’ math and reading scores affect Thomas High School’s performance relative to the other schools? The replacement of 461 students in the dataset for Thomas High School was not significant to the overall dataset. It is considered a Charter school and one of the top schools for Overall Passing %. 
    - 
    ###### How does replacing the ninth-grade scores affect the following:
        ###### Math and reading scores by grade
        ###### Scores by school spending: 
        ###### School spending was not affected when accounting for rounding. The dollars spent were still spend on the same students and one grade was not enough to change the dataset
        ###### Scores by school Size:
		Since Thomas High School was a medium sized school with an enrollment in the 1600s the only data that was affected was the minor decimal points as illustrated below. 
		![This is an image](https://github.com/PDob02/School_District_Analysis/blob/main/Resources/Charter%20School%20Analysis%20After.png)
        ###### Scores by school type

## 4.  **Summary:**  Summarize four changes in the updated school district analysis after reading and math scores for the ninth grade at Thomas High School have been replaced with NaNs.
		The most significant statistical change to the data lies within the Thomas school data itself. This is where the largest deviation on averages stood, though in most cases it was not statitiscally significant to the untrained eye or average parent. 
