#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to change the path if needed.)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read the School Data and Student Data and store into a Pandas DataFrame
school_data_df = pd.read_csv(school_data_to_load)
student_data_df = pd.read_csv(student_data_to_load)

# Cleaning Student Names and Replacing Substrings in a Python String
# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]

# Iterate through the words in the "prefixes_suffixes" list and replace them with an empty space, "".
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")

# Check names.
student_data_df.head(10)


# ## Deliverable 1: Replace the reading and math scores.
# 
# ### Replace the 9th grade reading and math scores at Thomas High School with NaN.

# In[121]:


# Install numpy using conda install numpy or pip install numpy. 
# Step 1. Import numpy as np.
import numpy as np


# In[130]:


# Step 2. Use the loc method on the student_data_df to select all the reading scores from the 9th grade at Thomas High School and replace them with NaN.
student_data_df.loc[(student_data_df["school_name"] == "Thomas High School") & (student_data_df["grade"] == "9th")], [:, "reading_score"]]=np.NaN} #,[:, "reading_score"]= np.NaN
#student_data_df.loc[:, "reading_score"]= np.NaN


# In[123]:


#  Step 3. Refactor the code in Step 2 to replace the math scores with NaN.
student_data_df.loc[:, "math_score"]= np.NaN


# In[126]:


#  Step 4. Check the student data for NaN's. 
student_data_df.tail(10)


# ## Deliverable 2 : Repeat the school district analysis

# ### District Summary

# In[6]:


# Combine the data into a single dataset
school_data_complete_df = pd.merge(student_data_df, school_data_df, how="left", on=["school_name", "school_name"])
school_data_complete_df.head()


# In[7]:


# Calculate the Totals (Schools and Students)
school_count = len(school_data_complete_df["school_name"].unique())
student_count = school_data_complete_df["Student ID"].count()

# Calculate the Total Budget
total_budget = school_data_df["budget"].sum()


# In[8]:


# Calculate the Average Scores using the "clean_student_data".
average_reading_score = school_data_complete_df["reading_score"].mean()
average_math_score = school_data_complete_df["math_score"].mean()


# In[9]:


# Step 1. Get the number of students that are in ninth grade at Thomas High School.
# These students have no grades. 


# Get the total student count 
student_count = school_data_complete_df["Student ID"].count()


# Step 2. Subtract the number of students that are in ninth grade at 
# Thomas High School from the total student count to get the new total student count.


# In[10]:


# Calculate the passing rates using the "clean_student_data".
passing_math_count = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)].count()["student_name"]
passing_reading_count = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)].count()["student_name"]


# In[11]:


# Step 3. Calculate the passing percentages with the new total student count.


# In[12]:


# Calculate the students who passed both reading and math.
passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)
                                               & (school_data_complete_df["reading_score"] >= 70)]

# Calculate the number of students that passed both reading and math.
overall_passing_math_reading_count = passing_math_reading["student_name"].count()


# Step 4.Calculate the overall passing percentage with new total student count.


# In[14]:


# Create a DataFrame
district_summary_df = pd.DataFrame(
          [{"Total Schools": school_count, 
          "Total Students": student_count, 
          "Total Budget": total_budget,
          "Average Math Score": average_math_score, 
          "Average Reading Score": average_reading_score,
          "% Passing Math": passing_math_percentage,
         "% Passing Reading": passing_reading_percentage,
        "% Overall Passing": overall_passing_percentage}])



# Format the "Total Students" to have the comma for a thousands separator.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)
# Format the "Total Budget" to have the comma for a thousands separator, a decimal separator and a "$".
district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)
# Format the columns.
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)
district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)
district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.1f}".format)
district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.1f}".format)
district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.1f}".format)

# Display the data frame
district_summary_df


# ##  School Summary

# In[15]:


# Determine the School Type
per_school_types = school_data_df.set_index(["school_name"])["type"]

# Calculate the total student count.
per_school_counts = school_data_complete_df["school_name"].value_counts()

# Calculate the total school budget and per capita spending
per_school_budget = school_data_complete_df.groupby(["school_name"]).mean()["budget"]
# Calculate the per capita spending.
per_school_capita = per_school_budget / per_school_counts

# Calculate the average test scores.
per_school_math = school_data_complete_df.groupby(["school_name"]).mean()["math_score"]
per_school_reading = school_data_complete_df.groupby(["school_name"]).mean()["reading_score"]

# Calculate the passing scores by creating a filtered DataFrame.
per_school_passing_math = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)]
per_school_passing_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)]

# Calculate the number of students passing math and passing reading by school.
per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]
per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]

# Calculate the percentage of passing math and reading scores per school.
per_school_passing_math = per_school_passing_math / per_school_counts * 100
per_school_passing_reading = per_school_passing_reading / per_school_counts * 100

# Calculate the students who passed both reading and math.
per_passing_math_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)
                                               & (school_data_complete_df["math_score"] >= 70)]

# Calculate the number of students passing math and passing reading by school.
per_passing_math_reading = per_passing_math_reading.groupby(["school_name"]).count()["student_name"]

# Calculate the percentage of passing math and reading scores per school.
per_overall_passing_percentage = per_passing_math_reading / per_school_counts * 100


# In[16]:


# Create the DataFrame
per_school_summary_df = pd.DataFrame({
    "School Type": per_school_types,
    "Total Students": per_school_counts,
    "Total School Budget": per_school_budget,
    "Per Student Budget": per_school_capita,
    "Average Math Score": per_school_math,
    "Average Reading Score": per_school_reading,
    "% Passing Math": per_school_passing_math,
    "% Passing Reading": per_school_passing_reading,
    "% Overall Passing": per_overall_passing_percentage})


# per_school_summary_df.head()


# In[17]:


# Format the Total School Budget and the Per Student Budget
per_school_summary_df["Total School Budget"] = per_school_summary_df["Total School Budget"].map("${:,.2f}".format)
per_school_summary_df["Per Student Budget"] = per_school_summary_df["Per Student Budget"].map("${:,.2f}".format)

# Display the data frame
per_school_summary_df


# In[18]:


# Step 5.  Get the number of 10th-12th graders from Thomas High School (THS).


# In[19]:


# Step 6. Get all the students passing math from THS


# In[20]:


# Step 7. Get all the students passing reading from THS


# In[21]:


# Step 8. Get all the students passing math and reading from THS


# In[22]:


# Step 9. Calculate the percentage of 10th-12th grade students passing math from Thomas High School. 


# In[23]:


# Step 10. Calculate the percentage of 10th-12th grade students passing reading from Thomas High School.


# In[24]:


# Step 11. Calculate the overall passing percentage of 10th-12th grade from Thomas High School. 


# In[25]:


# Step 12. Replace the passing math percent for Thomas High School in the per_school_summary_df.


# In[26]:


# Step 13. Replace the passing reading percentage for Thomas High School in the per_school_summary_df.


# In[27]:


# Step 14. Replace the overall passing percentage for Thomas High School in the per_school_summary_df.


# In[28]:


# per_school_summary_df


# ## High and Low Performing Schools 

# In[29]:


# Sort and show top five schools.


# In[30]:


# Sort and show top five schools.


# ## Math and Reading Scores by Grade

# In[31]:


# Create a Series of scores by grade levels using conditionals.


# Group each school Series by the school name for the average math score.


# Group each school Series by the school name for the average reading score.


# In[32]:


# Combine each Series for average math scores by school into single data frame.


# In[33]:


# Combine each Series for average reading scores by school into single data frame.


# In[34]:


# Format each grade column.


# In[35]:


# Remove the index.


# Display the data frame


# In[36]:


## Remove the index.


# Display the data frame


# ## Scores by School Spending

# In[37]:


# Establish the spending bins and group names.


# Categorize spending based on the bins.


# In[38]:


# Calculate averages for the desired columns. 


# In[39]:


# Create the DataFrame


# In[40]:


# Format the DataFrame 


# ## Scores by School Size

# In[41]:


# Establish the bins.

# Categorize spending based on the bins.


# In[42]:


# Calculate averages for the desired columns. 


# In[43]:


# Assemble into DataFrame. 


# In[44]:


# Format the DataFrame  


# ## Scores by School Type

# In[45]:


# Calculate averages for the desired columns. 


# In[46]:


# Assemble into DataFrame. 


# In[47]:


# # Format the DataFrame 


# In[ ]:




