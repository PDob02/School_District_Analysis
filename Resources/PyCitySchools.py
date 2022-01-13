#!/usr/bin/env python
# coding: utf-8

# In[122]:


# Add the Pandas dependency.
import pandas as pd


# In[123]:


# Files to load
school_data_to_load = "schools_complete.csv"
student_data_to_load = "students_complete.csv"


# In[124]:


# Read the school data file and store it in a Pandas DataFrame.
school_data_df = pd.read_csv(school_data_to_load)
school_data_df


# In[125]:


# Read the student data file and store it in a Pandas DataFrame.
student_data_df = pd.read_csv(student_data_to_load)
student_data_df.head()


# In[126]:


# Determine if there are any missing values in the school data.
school_data_df.count()


# In[127]:


# Determine if there are any missing values in the student data.
student_data_df.count()


# In[128]:


# Determine if there are any missing values in the school data.
school_data_df.isnull()


# In[129]:


# Determine if there are any missing values in the student data.
student_data_df.isnull()


# In[130]:


# Determine if there are any missing values in the student data.
student_data_df.isnull().sum()


# In[131]:


# Determine if there are not any missing values in the school data.
school_data_df.notnull()


# In[132]:


# Determine if there are not any missing values in the student data.
student_data_df.notnull().sum()


# In[133]:


# Determine data types for the school DataFrame.
school_data_df.dtypes


# In[134]:


# Determine data types for the student DataFrame.
student_data_df.dtypes


# In[135]:


# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]


# In[136]:


# Iterate through the words in the "prefixes_suffixes" list and replace them with an empty space, "".
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")


# In[137]:


# Combine the data into a single dataset.
school_data_complete_df = pd.merge(student_data_df, school_data_df, on=["school_name", "school_name"])
school_data_complete_df.head()


# In[138]:


# Get the total number of students.
student_count = school_data_complete_df.count()
student_count


# In[139]:


school_data_complete_df["Student ID"].count()


# In[140]:


# Calculate the total number of schools
school_count_2 = school_data_complete_df["school_name"].unique()
school_count_2


# In[141]:


# Calculate the total budget.
total_budget = school_data_df["budget"].sum()
total_budget


# In[142]:


# Calculate the average reading score.
average_reading_score = school_data_complete_df["reading_score"].mean()
average_reading_score


# In[143]:


# Calculate the average math score.
average_math_score = school_data_complete_df["math_score"].mean()
average_math_score


# In[144]:


passing_math = school_data_complete_df["math_score"] >= 70
passing_reading = school_data_complete_df["reading_score"] >= 70


# In[145]:


# Get all the students who are passing math in a new DataFrame.
passing_math = school_data_complete_df[school_data_complete_df["math_score"] >= 70]
passing_math.head()


# In[146]:


# Get all the students that are passing reading in a new DataFrame.
passing_reading = school_data_complete_df[school_data_complete_df["reading_score"] >= 70]


# In[147]:


# Calculate the number of students passing math.
passing_math_count = passing_math["student_name"].count()

# Calculate the number of students passing reading.
passing_reading_count = passing_reading["student_name"].count()


# In[148]:


print(passing_math_count)
print(passing_reading_count)


# In[168]:


# Calculate the percent that passed math.
passing_math_percentage = passing_math_count / float(student_count) * 100

# Calculate the percent that passed reading.
passing_reading_percentage = passing_reading_count / float(student_count) * 100


# In[150]:


# Calculate the students who passed both math and reading.
passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]

passing_math_reading.head()


# In[151]:


# Calculate the number of students who passed both math and reading.
overall_passing_math_reading_count = passing_math_reading["student_name"].count()
overall_passing_math_reading_count


# In[152]:


# Calculate the overall passing percentage.
overall_passing_percentage = overall_passing_math_reading_count / student_count * 100
overall_passing_percentage


# In[165]:


# Adding a list of values with keys to create a new DataFrame.
district_summary_df = pd.DataFrame(
          [{"Total Schools": school_count,
          "Total Students": student_count,
          "Total Budget": total_budget,
          "Average Math Score": average_math_score,
          "Average Reading Score": average_reading_score,
          "% Passing Math": passing_math_percentage,
         "% Passing Reading": passing_reading_percentage,
        "% Overall Passing": overall_passing_percentage}])
district_summary_df


# In[163]:


# Define a function that calculates the percentage of students that passed both 
# math and reading and returns the passing percentage when the function is called.

def passing_math_percent(pass_math_count, student_count):
    return pass_math_count / float(student_count) * 100


# In[166]:


passing_math_count = 29370
total_student_count = 39170


# In[167]:


# Call the function.
passing_math_percent(passing_math_count, total_student_count)

