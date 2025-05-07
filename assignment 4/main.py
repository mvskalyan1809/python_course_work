import modules as m

def display_menu():
    print("\nSelect an option:")
    print("1. Star Pattern")
    print("2. Diamond Pattern")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")
    print("5. Centimeters to Inches")
    print("6. Degrees to Radians")
    print("7. Distance Between Two Points")
    print("8. Multiplication Table")
    print("9. Percentage of 5 Subjects")
    print("10. Power of a Number")
    print("11. Alphabetic Order of Words")
    print("12. Student Grade Calculation")
    print("13. Capitalize Alternate Word")
    print("14. Fibonacci Series Using Recursion")
    print("15. Strong Password Validator")
    print("16. Count and Replace Vowels")
    print("17. Custom Math Module")
    print("18. Word Length Filter")
    print("19. Count Digit Frequency")
    print("20. Exit")

while True:
    display_menu()
    option = int(input("\nEnter your choice: "))

    if option == 1:
        print(m.star_pattern())
    elif option == 2:
        print(m.diamond_pattern())
    elif option == 3:
        print(m.kms_to_miles())
    elif option == 4:
        print(m.miles_to_kms())
    elif option == 5:
        print(m.cms_to_inches())
    elif option == 6:
        print(m.degrees_to_radians())
    elif option == 7:
        print(m.distance_between_points())
    elif option == 8:
        print(m.multiplication_table())
    elif option == 9:
        print(m.percentage_of_5_subjects())
    elif option == 10:
        print(m.power_of_number())
    elif option == 11:
        print(m.alphabetic_order())
    elif option == 12:
        print(m.student_grade_calculation())
    elif option == 13:
        print(m.capitalize_alternate_word())
    elif option == 14:
        print(m.fibonacci_series_recursion())
    elif option == 15:
        print(m.strong_password_validator())
    elif option == 16:
        print(m.count_and_replace_vowels())
    elif option == 17:
        print(m.custom_math_module())
    elif option == 18:
        print(m.word_length_filter())
    elif option == 19:
        print(m.count_digit_frequency())
    elif option == 20:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
