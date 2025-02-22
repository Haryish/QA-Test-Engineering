def compose_cover_letter():
    """Compose a tailored cover letter based on user input."""

    # Collect required inputs
    your_name = input("Enter your full name: ")
    your_address = input("Enter your address: ")
    your_phone = input("Enter your phone number: ")
    your_email = input("Enter your email address: ")
    github_link = input("Enter your GitHub profile link (optional, leave blank if not applicable): ")
    date = input("Enter the date (e.g., December 2, 2024): ")
    hiring_manager_name = input("Enter the hiring manager's name (or leave blank if unknown): ")
    company_name = input("Enter the company name: ")
    company_address = input("Enter the company address (optional): ")
    position_title = input("Enter the position title: ")
    your_current_role = input("Enter your current role: ")
    your_current_company = input("Enter your current company name: ")
    key_contributions = input("Enter your key contributions or skills (e.g., Automation testing using Selenium, Defect management, etc.): ")
    company_specific_note = input("Enter a specific note about the company that excites you (optional): ")

    # Compose the cover letter
    cover_letter = f"""
{your_name}  
{your_address}  
{your_phone} | {your_email} {f"| {github_link}" if github_link else ""}  

{date}  

{f"{hiring_manager_name}" if hiring_manager_name else ""}  
{company_name}  
{company_address if company_address else ""}  

**Subject:** Application for the Role of {position_title}  

Dear {hiring_manager_name if hiring_manager_name else "Hiring Manager"},  

I am excited to apply for the {position_title} position at {company_name}. With over [X years] of experience in {your_current_role} at {your_current_company}, I bring a proven track record of ensuring the quality and reliability of software applications through comprehensive testing processes and cutting-edge tools.  

My expertise lies in {key_contributions}. Highlights of my contributions include:  

- **Defect Management**: Identifying and resolving software inconsistencies, maintaining test cases in Jira, and facilitating effective communication between developers and testers.  
- **Automation and Manual Testing**: Developing end-to-end test plans, scenarios, and cases while leveraging automation to streamline processes.  
- **Performance Optimization**: Successfully reducing validation time by implementing a JSON-to-Table converter tool, saving 4 hours per validation cycle.  

{f"My hands-on experience with tools like Jenkins for deployment, Dremio and Snowflake for database operations, and BrowserStack for mobile testing complements my technical acumen. Additionally, my mentorship role at {your_current_company} reflects my dedication to fostering growth and collaboration within teams." if 'tools' in key_contributions.lower() else ''}

I am particularly impressed by {company_specific_note if company_specific_note else f"{company_name}’s commitment to innovation and quality"}. I am eager to bring my passion for automation, attention to detail, and problem-solving skills to contribute to your organization’s success.  

I would welcome the opportunity to discuss how my skills and experience align with your needs. Thank you for considering my application. I look forward to the possibility of contributing to {company_name} and am available at your convenience for an interview.  

Warm regards,  
{your_name}  
    """
    print("\n### Your Cover Letter ###\n")
    print(cover_letter)

# Run the program
compose_cover_letter()
