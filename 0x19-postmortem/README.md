### Server Outage Incident Report

# Issue Summary:
On May 9th, 2023 at 2:30 PM WAT, our web stack debugging project experienced a 2-hour outage which affected 75% of our users. Users were unable to access the website and were receiving a "Server Not Found" error message.

# Timeline:
- 2:30 PM: The issue was detected when an engineer noticed an abnormally high number of error codes 500 being returned.  
- 2:35 PM: The DevOps team investigated the server logs and found no errors
- 2:45 PM: The engineering team was notified and began investigating the application code
- 3:00 PM: Initial assumption was made that the issue was due to a database connection error
- 3:10 PM: The database was checked, but no issues were found
- 3:20 PM: The team discovered that a new feature had been deployed earlier that day which caused the issue
- 3:30 PM: The incident was escalated to the web stack debugging team for decision making
- 3:45 PM: The decision was made to roll back the feature deployment
- 4:00 PM: The issue was restored by fixing a configuration issue with the backend. 

# Root Cause and Resolution:
The root cause of the issue was traced to a misconfigured server in the new feature that was deployed earlier that day. The endpoint was sending incorrect data to the database, causing the database connection to fail. To resolve the issue, the team rolled back the feature deployment to the previous version, which did not have the misconfigured server. Additionally, the team fixed the server configuration and thoroughly tested the new feature before redeploying it to the production environment.

# Corrective and Preventative Measures:
To prevent similar issues from occurring in the future, the following measures will be taken:
- Implement a more rigorous testing process for new feature deployments
- Enhance monitoring alerts to include server failures
-Create a process for quickly responding to any issues that are detected
- Improve documentation and communication between development and DevOps teams to ensure a quicker resolution of issues.

# Tasks to address the issue include:
- Conduct a thorough review of the testing process and make necessary improvements
- Add monitoring for server configuration failures to the system
- Conduct a training session for the development and DevOps teams on effective communication and issue resolution processes

In conclusion, the outage was caused by a misconfigured server in a new feature deployment. The issue was resolved by rolling back the deployment and fixing the endpoint configuration. To prevent similar issues from occurring in the future, the team will implement more rigorous testing and monitoring processes, as well as improve communication between teams.
