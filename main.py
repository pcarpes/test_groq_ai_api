from groq import Groq
from config import API_KEY

def draft_message(content, role="user"):
    return {
        "role":role,
        "content":content
    }

client = Groq(api_key=API_KEY)

messages = [
    {
        "role":"system",
        "content":"You are looking for a job"
    }]

job_title = "Data Analyst"

job_description = """ help desk analyst
Posted on September 19, 2024 by Employer detailsVlogic Soft Inc.

Job details
LocationGuelph, ON
Workplace informationOn site
Salary
36.50 to 37.50 hourly (To be negotiated) / 30 to 35 hours per week
Terms of employment
Permanent employment
Full time
Shift
Start dateStarts as soon as possible
vacancies1 vacancy
SourceJob Bank #3087548
Overview
Languages
English

Education
No degree, certificate or diploma
Experience
7 months to less than 1 year

On site
 Work must be completed at the physical location. There is no option to work remotely.

Responsibilities
Tasks
Respond to users experiencing difficulties with computer
Consult user guides, technical manuals and other documents to research and implement solutions
Provide advice and training to users in response to identified difficulties
Collect, organize and maintain a problems and solutions log for use by other technical support analysts
Participate in the redesign of applications and other software
Provide business systems, network and Internet support to users in response to identified difficulties
Set up equipment for employee use, performing or ensuring proper installation of cables, operating systems, or appropriate software
Additional information
Work conditions and physical capabilities
Fast-paced environment
Personal suitability
Accurate
Initiative
Organized
"""

resume = """Pedro Carpes
•	Over 8 years of professional experience as a Data Analyst in diverse industry sectors, such as supply chain, logistics, maritime, and healthcare. Extensive experience collaborating with different departments, including the Board of Directors.
•	Proficiency in programming languages like Python, SQL, Golang, and JavaScript.
•	MBA in Project Management. Successfully managed and delivered multiple projects, applying agile methodologies, problem-solving, critical thinking, and teamwork skills. 
•	Flexible, adaptable, high achiever, and focused on results. Strong interest in new challenges and opportunities in the data science field.
•	Ability to communicate effectively in a multicultural environment – English, Portuguese and Spanish.

Experience
Associate Data Analyst	March 2024 – September 2024
Expeditors – United States
•	Initiate troubleshooting, bug triage, and additional activities to ensure system health. Data validation and testing involving multiple data sources – CSV, XML files, and external APIs. Collaborating with QA leads to identifying major areas of the product for automation. Create and execute automated test cases/scenarios, and perform tests including functional, integration, regression, and performance. Thoroughly test the application as requested to ensure smooth operation of all features. Analyze test results and generate subsequent test reports for stakeholders. Collaboration with development tech leads to coordinate releases. 
"""

prompt = f'Write a short winning cover letter to secure a interview for a {job_description} job based on my resume: {resume}'
messages.append(draft_message(prompt))

print(messages)

chat_completion = client.chat.completions.create(
    temperature=1.0,
    n=1,
    model="mixtral-8x7b-32768",
    max_tokens=10000,
    messages=messages
)

print(chat_completion.usage.total_tokens)
result = chat_completion.choices[0].message.content
print(result)
