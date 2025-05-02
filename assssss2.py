users_db = {}

# Sample jobs data
jobs = {
    1: {
        "title": "Software Engineer",
        "company": "Infosys",
        "location": "Bangalore",
        "locality": ["Electronic City", "Whitefield"],
        "skills": ["python", "django"],
        "experience": 2
    },
    2: {
        "title": "Data Analyst",
        "company": "TCS",
        "location": "Mumbai",
        "locality": ["Andheri"],
        "skills": ["excel", "sql"],
        "experience": 1
    },
    3: {
        "title": "Frontend Developer",
        "company": "Google",
        "location": "Bangalore",
        "locality": ["Indiranagar"],
        "skills": ["javascript", "react"],
        "experience": 3
    }
}

print(" Welcome to Naukri Job Portal ")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Enter username: ")
        if username in users_db:
            print("Username already exists")
            continue
        password = input("Enter password: ")
        users_db[username] = {
            "password": password
        }
        print("Registration successful!")

    elif choice == "2":
        username = input("Enter username: ")
        if username not in users_db:
            print("User not found. Please register.")
            continue
        password = input("Enter password: ")
        if users_db[username]["password"] != password:
            print("Incorrect password")
            continue

        if "skills" not in users_db[username]:
            print("\nPlease complete your profile:")
            skills = input("Enter your skills (comma separated): ").lower().split(",")
            location = input("Enter your preferred job location (City): ").capitalize()
            experience = int(input("Enter your experience in years: "))
            companies = input("Enter preferred companies (comma separated): ").title().split(",")
            roles = input("Enter preferred job roles (comma separated): ").title().split(",")

            users_db[username]["skills"] = [s.strip() for s in skills]
            users_db[username]["location"] = location
            users_db[username]["experience"] = experience
            users_db[username]["companies"] = [c.strip() for c in companies]
            users_db[username]["roles"] = [r.strip() for r in roles]

            print("Profile completed successfully!")

        print(f"\nWelcome, {username}!")
        while True:
            print("\n1. View Recommended Jobs")
            print("2. Apply for Jobs")
            print("3. Logout")
            option = input("Choose an option: ")

            if option == "1":
                print("\nRecommended Jobs Based on Your Profile:")
                found = False
                for id, job in jobs.items():
                    if users_db[username]["location"] == job["location"] and users_db[username]["experience"] >= job["experience"]:
                        skill_match = any(skill in job["skills"] for skill in users_db[username]["skills"])
                        locality_match = "locality" in job and any(loc in users_db[username]["locality"] for loc in job.get("locality", []))
                        company_match = "company" in job and job["company"] in users_db[username]["companies"]
                        role_match = job["title"] in users_db[username]["roles"]

                        if skill_match and (locality_match or company_match or role_match):
                            found = True
                            print(f"{id}. {job['title']} at {job.get('company', 'N/A')} - Skills: {', '.join(job['skills'])} - Exp: {job['experience']} yrs")
                if not found:
                    print("No recommended jobs found based on your profile.")

            elif option == "2":
                print("\nAvailable Jobs:")
                for id, job in jobs.items():
                    print(f"{id}. {job['title']} at {job.get('company', 'N/A')} - {job['location']}/{', '.join(job.get('locality', []))} - Skills: {', '.join(job['skills'])} - Exp: {job['experience']} yrs")

                applied = []
                try:
                    ids = list(map(int, input("Enter job IDs you want to apply to (space separated): ").split()))
                    for id in ids:
                        if id in jobs:
                            applied.append(jobs[id])
                except ValueError:
                    print("Invalid input. Please enter job IDs as numbers.")
                    continue

                if applied:
                    print("\n----- Application Summary -----")
                    for job in applied:
                        print(f"- Applied to: {job['title']} at {job['company']} | Location: {job['location']} | Exp Required: {job['experience']} yrs")
                    confirm = input("Do you want to confirm these applications? (yes/no): ").lower()
                    if confirm == "yes":
                        print(" Application(s) Submitted Successfully! ")
                        cont = input("Do you want to apply to more jobs? (yes/no): ").lower()
                        if cont == "no":
                            print("Thank you for using Naukri, Good luck with your job hunt!")
                            exit()
                    else:
                        print("Application Cancelled")
                else:
                    print("No valid job IDs selected.")

            elif option == "3":
                print("Logged out successfully.")
                break

            else:
                print("Invalid option. Try again.")

    elif choice == "3":
        print("Thank you for visiting Naukri.")
        break

    else:
        print("Invalid choice, Try again.")
