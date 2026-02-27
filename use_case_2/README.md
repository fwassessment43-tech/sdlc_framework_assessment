# Prompt:

> ```
> # Create a ticket management web application in Python
> 
> ## Requirements:
> 
> ### General Description:
> - Create a ticket management web application for a university campus.
> - Allow users to report:
> - Facility management problems.
> - Technical IT issues.
> - Services complaints.
> - Allow users to report and modify problems.
> - Enable interaction between users and helpdesk staff handling the issue.
> - Use a database to store all application data.
> - Allow helpdesk staff to visualize data and select analyses to perform.
> - Use Python as the programming language.
> 
> ### Login Page:
> - Generate a GUI that allows users to enter the application either as helpdesk staff or as a simple user.
> - Do not implement any login and user management system.
> 
> ### Ticket Management System:
> - Generate a GUI that enables the following ticket management functionalities:
>   - Simple users can:
>     - Insert a new ticket.
>     - View all 'open' and 'active' tickets.
>     - Modify all 'open' and 'active' tickets.
>   - Helpdesk users can:
>     - View all 'open', 'active', and 'closed' tickets.
>     - Change ticket status from 'open' to 'active'.
>     - Change ticket status from 'active' to 'closed'.
>   - Under each ticket:
>     - Helpdesk users and simple users can exchange messages related to that ticket.
> 
> ### Ticket Attributes:
> - Each ticket has a status assigned:
>   - A newly created ticket has the status 'open' by default.
>   - Helpdesk users can change status:
>     - From 'open' to 'active'.
>     - From 'active' to 'closed'.
> - Each ticket has:
>   - A free text description field.
>   - An automatically assigned category among:
>     - Facility management (e.g., elevator not working).
>     - Technical IT (e.g., WiFi malfunctioning).
>     - Services complaints (e.g., canteen food complaints).
>   - Opening date.
>   - Last modification date.
>   - Closing date.
> 
> ### Database:
> - Implement a database to store:
>   - Tickets.
>   - User interaction data (messages).
> - Implement basic database functionalities:
>   - Insert data.
>   - Modify data.
>   - Persist and retrieve data.
> 
> ### Microservices Architecture:
> - Implement a microservices architecture that interacts with the ticket management application.
> - Provide helpdesk users with data visualization and analysis functionalities.
> - Enable database interaction via API.
> - Implement the following services:
> 
> #### Service 1:
> - Allow the user to choose a period (last X hours/days).
> - Display the number of tickets opened in the selected period that have not yet been closed.
> 
> #### Service 2:
> - Compute the average ticket resolution time.
> - Display results grouped by ticket opening month.
> 
> #### Service 3:
> - Cluster tickets by category.
> - Display the number of active tickets per category.
> ```

# RQ1 – UC2 Results

**Performance of different LLMs without frameworks and combined with different frameworks (UC2).**  
Notation:  
- **CG (Y/N)**: Code Generated  
- **CE (Y/N)**: Code Executed  
- **RT**: Runtime (seconds)  
- **RM**: Requirements Met (out of 12)

| Scenario | CG | CE | RT (s) | RM |
|----------|----|----|--------|----|
| qwen_32b_q4 | Y | N | 32.00 | 0 |
| qwen_32b_q4 + MetaGPT | Y | Y | 304.31 | 1 |
| qwen_32b_q4 + ChatDev | Y | Y | 7059.00 | 3 |
| qwen_32b_q4 + AgileCoder | Y | N | 24065.00 | 0 |
| qwen_32b_q4 + HyperAgent | Y | Y | 975.00 | 1 |
| gemma_27b_fp16 | Y | Y | 951.00 | 2 |
| gemma_27b_fp16 + MetaGPT | Y | N | 14757.52 | 0 |
| gemma_27b_fp16 + ChatDev | Y | Y | 12924.00 | 4 |
| gemma_27b_fp16 + AgileCoder | Y | Y | 27643.00 | 1 |
| gemma_27b_fp16 + HyperAgent | Y | N | 3021.44 | 0 |
| codellama_7b_fp16 | N | N | 15.00 | 0 |
| codellama_7b_fp16 + MetaGPT | N | N | 9349.82 | 0 |
| codellama_7b_fp16 + ChatDev | N | N | 437.00 | 0 |
| codellama_7b_fp16 + AgileCoder | Y | Y | 2955.00 | 1 |
| codellama_7b_fp16 + HyperAgent | N | N | 19.20 | 0 |
| qwen2_7b_q4 | Y | Y | 16.00 | 2 |
| qwen2_7b_q4 + MetaGPT | Y | N | 1857.86 | 0 |
| qwen2_7b_q4 + ChatDev | N | N | 118.00 | 0 |
| qwen2_7b_q4 + AgileCoder | Y | N | 1829.00 | 0 |
| qwen2_7b_q4 + HyperAgent | Y | Y | 342.56 | 2 |
| llama3_3b_fp16 | Y | N | 17.00 | 0 |
| llama3_3b_fp16 + MetaGPT | Y | N | 219.26 | 0 |
| llama3_3b_fp16 + ChatDev | N | N | 199.00 | 0 |
| llama3_3b_fp16 + AgileCoder | N | N | 187.00 | 0 |
| llama3_3b_fp16 + HyperAgent | Y | Y | 244.64 | 1 |
| qwen2_3b_q4 | Y | N | 28.00 | 0 |
| qwen2_3b_q4 + MetaGPT | Y | N | 219.26 | 0 |
| qwen2_3b_q4 + ChatDev | N | N | 80.00 | 0 |
| qwen2_3b_q4 + AgileCoder | Y | N | 855.00 | 0 |
| qwen2_3b_q4 + HyperAgent | Y | Y | 59.55 | 2 |
| gpt_oss_20b | Y | Y | 29.00 | 2 |
| gpt_oss_20b + MetaGPT | N | N | 1691.21 | 0 |
| gpt_oss_20b + ChatDev | N | N | 492.00 | 0 |
| gpt_oss_20b + AgileCoder | Y | Y | 309.00 | 2 |
| gpt_oss_20b + HyperAgent | N | N | 307.25 | 0 |
| llama3_70b_q3 | Y | Y | 225.00 | 7 |
| llama3_70b_q3 + MetaGPT | Y | N | 2523.00 | 0 |
| llama3_70b_q3 + ChatDev | Y | N | 2997.00 | 0 |
| llama3_70b_q3 + AgileCoder | Y | N | 29235.00 | 0 |
| llama3_70b_q3 + HyperAgent | Y | N | 2163.13 | 0 |
| llama3_70b_q4 | Y | Y | 418.00 | 6 |
| llama3_70b_q4 + MetaGPT | Y | N | 2805.44 | 0 |
| llama3_70b_q4 + ChatDev | Y | N | 5185.00 | 0 |
| llama3_70b_q4 + AgileCoder | N | N | ND | 0 |
| llama3_70b_q4 + HyperAgent | Y | Y | 2055.44 | 2 |
| devstral_24b_fp16 | Y | Y | 483.00 | 4 |
| devstral_24b_fp16 + MetaGPT | Y | N | 5275.86 | 0 |
| devstral_24b_fp16 + ChatDev | Y | Y | 3315.00 | 1 |
| devstral_24b_fp16 + AgileCoder | Y | N | 36398.00 | 0 |
| devstral_24b_fp16 + HyperAgent | Y | Y | 417.43 | 0 |