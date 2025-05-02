def count_total_messages(messages):
    return len(messages)

def identify_unique_users(messages):
    users = set()
    for msg in messages:
        user = msg.split(':')[0].strip()
        users.add(user)
    return users

def count_total_words(messages):
    word_count = 0
    for msg in messages:
        words = msg.split(':')[1].strip().split()
        word_count += len(words)
    return word_count

def average_words_per_message(messages):
    if not messages:
        return 0
    total_words = count_total_words(messages)
    return round(total_words / len(messages), 2)

def find_longest_message(messages):
    if not messages:
        return None
    longest = max(messages, key=lambda x: len(x.split(':')[1].strip().split()))
    return longest

def most_active_user(messages):
    user_counts = {}
    for msg in messages:
        user = msg.split(':')[0].strip()
        user_counts[user] = user_counts.get(user, 0) + 1
    if not user_counts:
        return None
    most_active = max(user_counts.items(), key=lambda x: x[1])
    return most_active

def message_count_for_user(messages, username):
    count = 0
    for msg in messages:
        user = msg.split(':')[0].strip()
        if user.lower() == username.lower():
            count += 1
    return count

def most_frequent_word_by_user(messages, username):
    word_counts = {}
    for msg in messages:
        user, content = msg.split(':', 1)
        user = user.strip()
        if user.lower() == username.lower():
            words = content.strip().lower().split()
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1
    if not word_counts:
        return None
    most_frequent = max(word_counts.items(), key=lambda x: x[1])
    return most_frequent[0]

def first_last_message_by_user(messages, username):
    first = None
    last = None
    for msg in messages:
        user = msg.split(':')[0].strip()
        if user.lower() == username.lower():
            if first is None:
                first = msg
            last = msg
    return first, last

def check_user_presence(messages, username):
    for msg in messages:
        user = msg.split(':')[0].strip()
        if user.lower() == username.lower():
            return True
    return False

def find_common_repeated_words(messages, min_count=2):
    word_counts = {}
    all_words = set()
    for msg in messages:
        words = msg.split(':')[1].strip().lower().split()
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
    common_words = {word for word, count in word_counts.items() if count >= min_count}
    return common_words

def user_with_longest_avg_message(messages):
    user_stats = {}
    for msg in messages:
        user, content = msg.split(':', 1)
        user = user.strip()
        words = content.strip().split()
        if user not in user_stats:
            user_stats[user] = {'total_words': 0, 'count': 0}
        user_stats[user]['total_words'] += len(words)
        user_stats[user]['count'] += 1
    
    if not user_stats:
        return None
    
    avg_lengths = {user: stats['total_words']/stats['count'] 
                  for user, stats in user_stats.items()}
    longest_user = max(avg_lengths.items(), key=lambda x: x[1])
    return longest_user[0], round(longest_user[1], 2)

def count_messages_mentioning_user(messages, username):
    count = 0
    for msg in messages:
        content = msg.split(':')[1].strip().lower()
        if username.lower() in content.lower():
            count += 1
    return count

def remove_duplicate_messages(messages):
    unique_messages = []
    seen = set()
    for msg in messages:
        if msg not in seen:
            seen.add(msg)
            unique_messages.append(msg)
    return unique_messages

def sort_messages_alphabetically(messages):
    return sorted(messages)

def extract_questions(messages):
    questions = []
    for msg in messages:
        content = msg.split(':')[1].strip()
        if '?' in content:
            questions.append(msg)
    return questions

def calculate_reply_ratio(messages, user1, user2):
    reply_count = 0
    prev_user = None
    for msg in messages:
        current_user = msg.split(':')[0].strip()
        if prev_user == user1 and current_user == user2:
            reply_count += 1
        prev_user = current_user
    return reply_count

def check_deleted_messages(messages):
    deleted = 0
    for msg in messages:
        content = msg.split(':')[1].strip()
        if content.lower() == "this message was deleted":
            deleted += 1
    return deleted

def main():
    # Input messages
    num_messages = int(input("Enter the number of messages: "))
    messages = []
    for i in range(num_messages):
        message = input(f"Message {i+1}: ")
        messages.append(message)
    
    # Menu system
    while True:
        print("\nAnalysis Options:")
        print("1. Count total number of messages")
        print("2. Identify unique users in the chat")
        print("3. Count total words in the chat")
        print("4. Calculate average words per message")
        print("5. Find the longest message sent")
        print("6. Find the most active user")
        print("7. Get message count for a specific user")
        print("8. Find the most frequently used word by a specific user")
        print("9. Retrieve the first and last message sent by a user")
        print("10. Check if a user is present in the chat")
        print("11. Find commonly repeated words")
        print("13. Identify the user with the longest average message length")
        print("14. Count how many messages mention a specific user")
        print("15. Remove duplicate messages")
        print("16. Sort messages alphabetically")
        print("17. Extract all questions asked in the chat")
        print("18. Calculate the reply ratio between two users")
        print("19. Check for deleted messages")
        print("20. Exit")
        
        choice = input("Enter your choice (1-20): ")
        
        if choice == '1':
            print(f"Total messages: {count_total_messages(messages)}")
        
        elif choice == '2':
            print(f"Unique users in the chat: {identify_unique_users(messages)}")
        
        elif choice == '3':
            print(f"Total words in the chat: {count_total_words(messages)}")
        
        elif choice == '4':
            avg = average_words_per_message(messages)
            print(f"Average words per message: {avg}")
        
        elif choice == '5':
            print(f"Longest message: {find_longest_message(messages)}")
        
        elif choice == '6':
            user, count = most_active_user(messages)
            print(f"Most active user: {user} ({count} messages)")
        
        elif choice == '7':
            username = input("Enter username to count messages: ")
            count = message_count_for_user(messages, username)
            print(f"Messages sent by {username}: {count}")
        
        elif choice == '8':
            username = input("Enter username to find frequent word: ")
            word = most_frequent_word_by_user(messages, username)
            if word:
                print(f"Most frequent word used by {username}: \"{word}\"")
            else:
                print(f"No messages found for {username}")
        
        elif choice == '9':
            username = input("Enter username to get first/last messages: ")
            first, last = first_last_message_by_user(messages, username)
            if first:
                print(f"First message by {username}: \"{first}\"")
                print(f"Last message by {username}: \"{last}\"")
            else:
                print(f"No messages found for {username}")
        
        elif choice == '10':
            username = input("Enter username to check: ")
            if check_user_presence(messages, username):
                print(f"User '{username}' found in the chat.")
            else:
                print(f"User '{username}' not found in the chat.")
        
        elif choice == '11':
            common_words = find_common_repeated_words(messages)
            print(f"Common repeated words: {common_words}")
        
        elif choice == '13':
            user, avg = user_with_longest_avg_message(messages)
            print(f"User with longest average message: {user} (avg {avg} words)")
        
        elif choice == '14':
            username = input("Enter username to count mentions: ")
            count = count_messages_mentioning_user(messages, username)
            print(f"Messages mentioning '{username}': {count}")
        
        elif choice == '15':
            unique_msgs = remove_duplicate_messages(messages)
            print(f"Unique messages count: {len(unique_msgs)}")
            if len(unique_msgs) < len(messages):
                print("Unique messages:")
                for msg in unique_msgs:
                    print(msg)
        
        elif choice == '16':
            sorted_msgs = sort_messages_alphabetically(messages)
            print("Messages sorted alphabetically:")
            for msg in sorted_msgs:
                print(msg)
        
        elif choice == '17':
            questions = extract_questions(messages)
            print("Questions found in chat:")
            for q in questions:
                print(q)
        
        elif choice == '18':
            user1 = input("Enter first user: ")
            user2 = input("Enter second user: ")
            ratio = calculate_reply_ratio(messages, user1, user2)
            print(f"Reply ratio from {user2} to {user1}: {ratio} replies")
        
        elif choice == '19':
            deleted = check_deleted_messages(messages)
            print(f"Deleted messages found: {deleted}")
        
        elif choice == '20':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()