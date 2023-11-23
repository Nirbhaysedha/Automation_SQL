kpmg_questions = [
    {
        'Question': "How many employees work in the Finance department?",
        'SQLQuery': "SELECT COUNT(*) FROM Employees WHERE Department = 'Finance'",
        'Answer': "3"
    },
    {
        'Question': "What is the average salary of employees hired in 2023?",
        'SQLQuery': "SELECT AVG(Salary) FROM Employees WHERE YEAR(HireDate) = 2023",
        'Answer': "67600.00"
    },
    {
        'Question': "List employees who have managers and their manager's names.",
        'SQLQuery': "SELECT e.FirstName, e.LastName, m.FirstName AS Manager_FirstName, m.LastName AS Manager_LastName FROM Employees e LEFT JOIN Employees m ON e.ManagerID = m.EmployeeID WHERE e.ManagerID IS NOT NULL",
        'Answer': "Sample result set with employee names and their manager names"
    },
    {
        'Question': "How many employees were hired before January 1, 2022?",
        'SQLQuery': "SELECT COUNT(*) FROM Employees WHERE HireDate < '2022-01-01'",
        'Answer': "5"
    },
    {
        'Question': "Count the number of employees in each department.",
        'SQLQuery': "SELECT Department, COUNT(*) AS EmployeeCount FROM Employees GROUP BY Department",
        'Answer': "Sample result set with department names and employee counts"
    },
    {
        'Question': "Retrieve the email addresses and phone numbers of all employees.",
        'SQLQuery': "SELECT FirstName, LastName, Email, PhoneNumber FROM Employees",
        'Answer': "Sample result set with employee names, emails, and phone numbers"
    }
]
