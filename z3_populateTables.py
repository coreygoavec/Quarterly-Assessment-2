import sqlite3

# Connect to the database
conn = sqlite3.connect('QuizBowlDatabase.db')
cursor = conn.cursor()

# create a list of dictionaries with the questions and answers for Business Applications Development
questions = [
    {
        "id": 1,
        "question": "What is the primary purpose of a database in business applications development?",
        "option1": "Storage",
        "option2": "Processing",
        "option3": "Presentation",
        "option4": "Validation",
        "correct_answer": "Storage"
    },
    {
        "id": 2,
        "question": "Explain the significance of version control in the context of software development for business applications.",
        "option1": "Isolation",
        "option2": "Collaboration",
        "option3": "Segmentation",
        "option4": "Confrontation",
        "correct_answer": "Collabration"
    },
    {
        "id": 3,
        "question": "What role does user interface (UI) design play in enhancing the user experience of a business application?",
        "option1": "Complexity",
        "option2": "Usability",
        "option3": "Ambiguity",
        "option4": "Uncertainty",
        "correct_answer": "Usability"
    },
    {
        "id": 4,
        "question": "How does API (Application Programming Interface) integration contribute to the functionality of business applications?",
        "option1": "Isolation",
        "option2": "Interoperability",
        "option3": "Fragmentation",
        "option4": "Obstruction",
        "correct_answer": "Interoperability"
    },
    {
        "id": 5,
        "question": "Briefly describe the importance of testing in the software development life cycle for business applications.",
        "option1": "Verification",
        "option2": "Proliferation",
        "option3": "Stagnation",
        "option4": "Amputation",
        "correct_answer": "Verification"
    }
]
# Insert questions into the Business Applications Development table
for question in questions:
   pass
   cursor.execute('''INSERT INTO BusinessApplicationsDevelopment (id, question, option1, option2, option3, option4, correct_answer)
                     VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
                                                        question['option2'], question['option3'], question['option4'],
                                                        question['correct_answer']))
   conn.commit()

# use select query to check if your data properly populated the table
cursor.execute('''SELECT * FROM BusinessApplicationsDevelopment''')

# use select query to check if your data properly populated the table
cursor.execute('''SELECT * FROM BusinessApplicationsDevelopment''')

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the fetched rows
for row in rows:
   print(row)

# List of questions for Entrepreneurship course
entrepreneurship_questions = [
    {
        "id": 1,
        "question": "What is the primary goal of entrepreneurship?",
        "option1": "Job Security",
        "option2": "Innovation and Value Creation",
        "option3": "Following Trends",
        "option4": "Maintaining the Status Quo",
        "correct_answer": "Innovation and Value Creation"
    },
    {
        "id": 2,
        "question": "Which term refers to the funds contributed by the owner(s) of a business?",
        "option1": "Debt Financing",
        "option2": "Equity Financing",
        "option3": "Angel Investment",
        "option4": "Bootstrapping",
        "correct_answer": "Equit Financing"
    },
    {
        "id": 3,
        "question": "What does SWOT analysis stand for?",
        "option1": "Strengths, Weaknesses, Opportunities, Threats",
        "option2": "Sales, Workforce, Operations, Technology",
        "option3": "Strategy, Workflow, Objectives, Tactics",
        "option4": "Success, Wisdom, Organization, Tenacity",
        "correct_answer": "Strengths, Weaknesses, Opportunities, Threats"
    },
    {
        "id": 4,
        "question": "Which of the following is a characteristic of a successful entrepreneur?",
        "option1": "Fear of failure",
        "option2": "Resistance to change",
        "option3": "Risk-taking attitude",
        "option4": "Avoidance of challenges",
        "correct_answer": "Risk-taking attitude"
    },
    {
        "id": 5,
        "question": "What is the term for the process of turning an idea into a viable business?",
        "option1": "Market research",
        "option2": "Product development",
        "option3": "Entrepreneurship",
        "option4": "Strategic planning",
        "correct_answer": "Entrepreneurship"
    }  
]
# for loop to insert questions into the Entrepreneurship table
for question in entrepreneurship_questions:
    cursor.execute('''INSERT INTO Entrepreneurship (id, question, option1, option2, option3, option4, correct_answer)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
                                                         question['option2'], question['option3'], question['option4'],
                                                         question['correct_answer']))
    conn.commit()

# List of questions for Organizational Leadership course
organizational_leadership_questions = [
    {
        "id": 1,
        "question": "What does the term 'delegation' refer to in organizational leadership?",
        "option1": "Micromanaging tasks",
        "option2": "Avoiding responsibility",
        "option3": "Assigning tasks and authority to others",
        "option4": "Strict supervision of employees",
        "correct_answer": "Assigning tasks and authority to others"
    },
    {
        "id": 2,
        "question": "Which leadership style is characterized by a leader who seeks input from team members before making decisions?",
        "option1": "Autocratic",
        "option2": "Laissez-faire",
        "option3": "Democratic",
        "option4": "Transformational",
        "correct_answer": "Democratic"
    },
    {
        "id": 3,
        "question": "What is the primary focus of situational leadership?",
        "option1": "Consistency in leadership style",
        "option2": "Adapting leadership style to the situation",
        "option3": "Maintaining a rigid hierarchy",
        "option4": "Ignoring situational factors",
        "correct_answer": "Adapting leadership style to the situation"
    },
    {
        "id": 4,
        "question": "What does the term 'emotional intelligence' refer to in the context of leadership?",
        "option1": "The ability to manipulate emotions",
        "option2": "Ignoring emotions in the workplace",
        "option3": "Understanding and managing one's emotions and the emotions of others",
        "option4": "Being emotionally detached from team members",
        "correct_answer": "Understanding and managing one's emotions and the emotions of others"
    },
    {
        "id": 5,
        "question": "What is a key benefit of effective communication in organizational leadership?",
        "option1": "Confusion and misunderstanding",
        "option2": "Increased employee engagement",
        "option3": "Limited information flow",
        "option4": "Lack of transparency",
        "correct_answer": "Increased employee engagement"
    }
]
# Insert questions into the OrganizationalLeadership table
for question in organizational_leadership_questions:
    cursor.execute('''INSERT INTO OrganizationalLeadership (id, question, option1, option2, option3, option4, correct_answer)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
                                                         question['option2'], question['option3'], question['option4'],
                                                         question['correct_answer']))
    conn.commit()

# List of questions for Business Intelligence and Analytics Capstone course
bi_analytics_questions = [
    {
        "id": 1,
        "question": "What is the primary goal of data warehousing in the context of Business Intelligence (BI)?",
        "option1": "Real-time data analysis",
        "option2": "Storing and managing historical data",
        "option3": "Data visualization",
        "option4": "Predictive modeling",
        "correct_answer": "Storing and managing historical data"
    },
    {
        "id": 2,
        "question": "What does the term 'data mining' refer to in the field of Business Intelligence and Analytics?",
        "option1": "Extracting data from a database",
        "option2": "Analyzing data patterns to discover meaningful information",
        "option3": "Deleting unnecessary data",
        "option4": "Securing data in transit",
        "correct_answer": "Analyzing data patterns to discover meaningful information"
    },
    {
        "id": 3,
        "question": "What is the purpose of a Key Performance Indicator (KPI) in business analytics?",
        "option1": "Managing employee performance",
        "option2": "Measuring the success of a project",
        "option3": "Tracking business expenses",
        "option4": "Storing raw data",
        "correct_answer": "Measuring the success of a project"
    },
    {
        "id": 4,
        "question": "What does the term 'predictive analytics' involve in the context of business intelligence?",
        "option1": "Analyzing past events",
        "option2": "Forecasting future trends and outcomes based on historical data",
        "option3": "Real-time data visualization",
        "option4": "Descriptive data analysis",
        "correct_answer": "Forecasting future trends and outcomes based on historical data"
    },
    {
        "id": 5,
        "question": "In the realm of Business Intelligence and Analytics, what does the term 'OLAP' stand for?",
        "option1": "Online Analytical Processing",
        "option2": "Operational Level Agreement Process",
        "option3": "Overhead Labor Allocation Plan",
        "option4": "Outsourced Logistics and Analytics Platform",
        "correct_answer": "Online Analytical Processing"
    }
]

# use a for loop to insert questions into the AnalyticsCapstone table
for question in bi_analytics_questions:
    cursor.execute('''INSERT INTO AnalyticsCapstone (id, question, option1, option2, option3, option4, correct_answer)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
                                                         question['option2'], question['option3'], question['option4'],
                                                         question['correct_answer']))
    conn.commit()

# List of questions for Business Strategy course
business_strategy_questions = [
    {
        "id": 1,
        "question": "What is the central focus of a SWOT analysis in business strategy?",
        "option1": "Project timelines",
        "option2": "Competitive pricing",
        "option3": "Internal and external factors affecting a company",
        "option4": "Employee performance metrics",
        "correct_answer": "Internal and external factors affecting a company"
    },
    {
        "id": 2,
        "question": "How would you define the term 'competitive advantage' in the context of business strategy?",
        "option1": "Achieving average industry performance",
        "option2": "Outperforming rivals and gaining a distinctive edge",
        "option3": "Collaborating with competitors for mutual benefit",
        "option4": "Reducing product quality to cut costs",
        "correct_answer": "Outperforming rivals and gaining a distinctive edge"
    },
    {
        "id": 3,
        "question": "What does the term 'core competency' refer to in business strategy?",
        "option1": "Basic operational tasks",
        "option2": "Unique capabilities that provide a competitive advantage",
        "option3": "External market conditions",
        "option4": "Short-term financial goals",
        "correct_answer": "Unique capabilities that provide a competitive advantage"
    },
    {
        "id": 4,
        "question": "In strategic management, what is the purpose of a mission statement?",
        "option1": "Outlining financial projections",
        "option2": "Communicating the organization's purpose and values",
        "option3": "Listing daily operational tasks",
        "option4": "Addressing customer complaints",
        "correct_answer": "Communicating the organization's purpose and values"
    },
    {
        "id": 5,
        "question": "What does the term 'market segmentation' involve in the context of business strategy?",
        "option1": "Reducing product variety to target a broad audience",
        "option2": "Targeting specific customer groups with tailored marketing approaches",
        "option3": "Expanding operations into new markets",
        "option4": "Lowering prices to attract a larger customer base",
        "correct_answer": "Targeting specific customer groups with tailored marketing approaches"
    }
]

# for loop to insert questions into the BusinessStrategy table
for question in business_strategy_questions:
    cursor.execute('''INSERT INTO BusinessLaw (id, question, option1, option2, option3, option4, correct_answer)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
                                                         question['option2'], question['option3'], question['option4'],
                                                         question['correct_answer']))
    conn.commit()

#Fetch and display data from each table
tables = ['BusinessStrategy', 'BusinessApplicationsDevelopment', 'Entrepreneurship', 'AnalyticsCapstone', 'OrganizationalLeadership']
for table in tables:
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    print(f"Contents of {table} table:")
    for row in rows:
        print(row)
    print()

def add_new_question(table, id, question, option1, option2, option3, option4, correct_answer):
    try:
        # Connect to the database
        conn = sqlite3.connect('QuizBowlDatabase.db')
        cursor = conn.cursor()

        # Insert the new question into the specified category table(add 1 to previous id )
        cursor.execute(f"INSERT INTO {table} (id, question, option1, option2, option3, option4, correct_answer) "
                       "VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (id, question, option1, option2, option3, option4, correct_answer))
        
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        
        print("New question added successfully!")

    except sqlite3.Error as error:
        print("Error adding new question:", error)
add_new_question('BusinessStrategy',6,'What general strategy targets a specific subset of a market and focuses on uniqueness?','Cost Leadership','Focused Cost Leadership','Differentiation','Focused Differentiation','Focused Differentiation')