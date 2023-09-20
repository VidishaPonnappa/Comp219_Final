import pandas as pd

# Read data from job_data.csv
data = pd.read_csv('job_data.csv')

# Compute the average of num_of_salaries for specific job titles
job_titles = ["Data Architect", "Senior Business Analyst", "Data Scientist", "Machine Learning Engineer", "Senior Data Engineer"]

for title in job_titles:
    avg_salary = data[data['job_title'] == title]['num_of_salaries'].mean()
    print(f"Average num_of_salaries for {title}: {avg_salary}")
