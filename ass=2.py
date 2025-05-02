users_db = {}

print(" Welcome to Naukri Job Portal ")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Enter username: ")
        if username in users_db:
            print("Username already exists!")
            continue
        password = input("Enter password: ")
        users_db[username] = {
            "password": password
            # Profile info will be added later after login
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

        # Check if profile info is missing
        if "skills" not in users_db[username]:
            print("\nPlease complete your profile:")
            skills = input("Enter your skills (comma separated): ").lower().split(",")
            location = input("Enter your preferred job location: ").capitalize()
            experience = int(input("Enter your experience in years: "))
            users_db[username]["skills"] = [s.strip() for s in skills]
            users_db[username]["location"] = location
            users_db[username]["experience"] = experience
            print("Profile completed successfully!")

        # jobs data inside login
        jobs = {
            1: {"title": "Data Analyst", "location": "Hyderabad", "skills": ["excel", "sql", "powerbi"], "experience": 1},
            2: {"title": "Software Engineer", "location": "Bangalore", "skills": ["java", "python", "dsa"], "experience": 2},
            3: {"title": "Web Developer", "location": "Delhi", "skills": ["html", "css", "javascript"], "experience": 1},
            4: {"title": "ML Engineer", "location": "Hyderabad", "skills": ["python", "ml", "pandas"], "experience": 2},
            5: {"title": "Backend Developer", "location": "Chennai", "skills": ["nodejs", "mongodb", "api"], "experience": 3}
        }

        print(f"\nWelcome, {username}!")
        while True:
            print("\n1. View Recommended Jobs")
            print("2. Apply for Jobs")
            print("3. Logout")
            option = input("Choose an option: ")

            if option == "1":
                print("\nRecommended Jobs Based on Your Profile:")
                for id, job in jobs.items():
                    if users_db[username]["location"] == job["location"] and users_db[username]["experience"] >= job["experience"]:
                        for skill in users_db[username]["skills"]:
                            if skill in job["skills"]:
                                print(f"{id}. {job['title']} - {job['location']} - Skills: {', '.join(job['skills'])} - Exp: {job['experience']} yrs")
                                break

            elif option == "2":
                print("\nAvailable Jobs:")
                for id, job in jobs.items():
                    print(f"{id}. {job['title']} - {job['location']} - Skills: {', '.join(job['skills'])} - Exp: {job['experience']} yrs")
                
                applied = []
                ids = list(map(int, input("Enter job IDs you want to apply to (space separated): ").split()))
                for id in ids:
                    if id in jobs:
                        applied.append(jobs[id])
                
                if applied:
                    print("\n----- Application Summary -----")
                    for job in applied:
                        print(f"- Applied to: {job['title']} at {job['location']} | Required Exp: {job['experience']} yrs")
                    confirm = input("Do you want to confirm these applications? (yes/no): ").lower()
                    if confirm == "yes":
                        print(" Application(s) Submitted Successfully! ")
                        cont = input("Do you want to apply to more jobs? (yes/no): ").lower()
                        if cont == "no":
                            print("Thank you for using Naukri, Good luck with your job hunt")
                            exit()
                    else:
                        print("Application Cancelled")
                else:
                    print("No valid job IDs selected")

            elif option == "3":
                print("Logged out successfully")
                break

    elif choice == "3":
        print("Thank you for visiting Naukri")
        break

    else:
        print("Invalid choice, Try again")
