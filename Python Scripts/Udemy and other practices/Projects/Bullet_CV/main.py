"""
Title: CV Bullets
Author: Franco Nepomuceno
Date: 9/22/24
Rev: A
"""

# Initialize an empty dictionary to store job titles and resume bullets
resume = {}

# Function to add a job and its bullet points to the resume
def add_job (job_title, bullets):
    # Add the job and its bullets to the resume dictionary
    resume[job_title] = bullets

# Function to display all job titles and their bullets
def display_resume():
    for job_title, bullets in resume.items():
        print(f"Job Title: {job_title}")
        for i, bullet in enumerate(bullets, 1):
            print(f"  {i}. {bullet}")
        print()

# Function to remove a job by title
def remove_job(job_title):
    if job_title in resume:
        del resume[job_title]
        print(f"Removed job: {job_title}")
    else:
        print(f"No job found with title: {job_title}")

# Example usage:
# Adding jobs with bullets
add_job("Electrical Engineer", 
[
    "Developed and maintained web applications using Python and Django.",
    "Collaborated with cross-functional teams to deliver software solutions.",
    "Led the migration of legacy systems to cloud-based infrastructure."
])

add_job("Sales Engineer", [
    "Performed data analysis using Python and SQL.",
    "Generated reports and dashboards for stakeholders.",
    "Optimized data collection processes to improve efficiency."
])

add_job("Process Technician", [
    "Performed data analysis using Python and SQL.",
    "Generated reports and dashboards for stakeholders.",
    "Optimized data collection processes to improve efficiency."
])

add_job("Manufacturing Engineer", [
    "Performed data analysis using Python and SQL.",
    "Generated reports and dashboards for stakeholders.",
    "Optimized data collection processes to improve efficiency."
])


