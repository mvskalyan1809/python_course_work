num_msgs = int(input("Enter total number of messages: "))
chat_log = {}
for i in range(num_msgs):
    person, message = input().split(":", 1)
    person = person.strip()
    message = message.strip()
    if person in chat_log:
        chat_log[person].append(message)
    else:
        chat_log[person] = [message]

print(chat_log)
print(chat_log.keys())

def show_menu():
    options = [
        "Exit", "Total message count", "Unique users list", "Total word count",
        "Avg words per message", "Longest message overall",
        "Most active person", "Messages from a user",
        "Top word by a user", "First & last message by user",
        "Is user in chat?", "Repeated words",
        "User with longest avg message", "Count mentions of someone",
        "Delete duplicate messages", "Alphabetical messages",
        "List all questions", "Reply count between users", "Deleted messages count"
    ]
    for i in range(len(options)):
        print(f"{i}. {options[i]}")

def count_total_messages(chat):
    total = 0
    for msg_list in chat.values():
        total += len(msg_list)
    return total

def list_unique_users(chat):
    users = set()
    for person in chat:
        users.add(person)
    return f"{len(users)} users: {users}"

def count_all_words(chat):
    words = 0
    for msg_list in chat.values():
        for msg in msg_list:
            words += len(msg.split())
    return words

def calc_avg_words(chat):
    msg_total = 0
    word_total = 0
    for msg_list in chat.values():
        msg_total += len(msg_list)
        for msg in msg_list:
            word_total += len(msg.split())
    if msg_total == 0:
        return 0
    return word_total / msg_total

def find_longest_msg(chat):
    longest = ""
    for msg_list in chat.values():
        for msg in msg_list:
            if len(msg) > len(longest):
                longest = msg
    return longest

def top_person(chat):
    max_count = 0
    top_user = ""
    for user in chat:
        user_count = len(chat[user])
        if user_count > max_count:
            max_count = user_count
            top_user = user
    return top_user

def user_msg_count(chat):
    name = input("Enter username: ")
    if name in chat:
        return len(chat[name])
    return 0

def most_common_word(chat):
    name = input("Enter username: ")
    if name not in chat:
        return "User not found"
    word_map = {}
    for msg in chat[name]:
        for word in msg.split():
            if word in word_map:
                word_map[word] += 1
            else:
                word_map[word] = 1
    top_word = ""
    top_count = 0
    for w in word_map:
        if word_map[w] > top_count:
            top_word = w
            top_count = word_map[w]
    return top_word

def get_first_last(chat):
    name = input("Enter username: ")
    if name in chat and len(chat[name]) > 0:
        return f"First: {chat[name][0]}, Last: {chat[name][-1]}"
    return "No messages or user not found"

def check_user(chat):
    name = input("Enter username: ")
    if name in chat:
        return "Present"
    return "Absent"

def find_repeated_words(chat):
    all_words = {}
    for msg_list in chat.values():
        for msg in msg_list:
            for word in msg.split():
                if word in all_words:
                    all_words[word] += 1
                else:
                    all_words[word] = 1
    duplicates = []
    for word in all_words:
        if all_words[word] > 1:
            duplicates.append(word)
    return duplicates

def longest_avg_user(chat):
    max_avg = 0
    top_user = ""
    for user in chat:
        total_len = 0
        msg_count = 0
        for msg in chat[user]:
            total_len += len(msg)
            msg_count += 1
        if msg_count > 0:
            avg = total_len / msg_count
            if avg > max_avg:
                max_avg = avg
                top_user = user
    return top_user

def count_mentions(chat):
    target = input("Enter name to check mentions: ")
    mention_count = 0
    for msg_list in chat.values():
        for msg in msg_list:
            if target in msg:
                mention_count += 1
    return f"{target} mentioned {mention_count} times"

def clean_duplicates(chat):
    for user in chat:
        seen = set()
        clean = []
        for msg in chat[user]:
            if msg not in seen:
                seen.add(msg)
                clean.append(msg)
        chat[user] = clean
    return "Duplicates removed"

def sort_all_messages(chat):
    collected = []
    for msg_list in chat.values():
        for msg in msg_list:
            collected.append(msg)
    collected.sort()
    return collected

def get_questions(chat):
    q_list = []
    for msg_list in chat.values():
        for msg in msg_list:
            if "?" in msg:
                q_list.append(msg)
    return q_list

def reply_count(chat):
    names = input("Enter two users (e.g. A and B): ").split(" and ")
    user1 = names[0].strip()
    user2 = names[1].strip()
    reply_cnt = 0
    if user2 in chat:
        for msg in chat[user2]:
            if user1 in msg:
                reply_cnt += 1
    return f"{user2} replied to {user1} {reply_cnt} times"

def count_deleted(chat):
    deleted_total = 0
    for msg_list in chat.values():
        for msg in msg_list:
            if "deleted" in msg:
                deleted_total += 1
    return deleted_total

while True:
    print("="*45)
    print("Menu:")
    show_menu()
    print("="*45)
    choice = int(input("Choose an option: "))
    if choice == 0:
        break
    elif choice == 1:
        print(f"Total messages: {count_total_messages(chat_log)}")
    elif choice == 2:
        print(list_unique_users(chat_log))
    elif choice == 3:
        print(f"Total words: {count_all_words(chat_log)}")
    elif choice == 4:
        print(f"Avg words per message: {calc_avg_words(chat_log):.2f}")
    elif choice == 5:
        print(f"Longest message: {find_longest_msg(chat_log)}")
    elif choice == 6:
        print(f"Most active user: {top_person(chat_log)}")
    elif choice == 7:
        print(f"Messages by user: {user_msg_count(chat_log)}")
    elif choice == 8:
        print(f"Top word by user: {most_common_word(chat_log)}")
    elif choice == 9:
        print(get_first_last(chat_log))
    elif choice == 10:
        print(check_user(chat_log))
    elif choice == 11:
        print(f"Repeated words: {find_repeated_words(chat_log)}")
    elif choice == 12:
        print(f"User with longest avg msg: {longest_avg_user(chat_log)}")
    elif choice == 13:
        print(count_mentions(chat_log))
    elif choice == 14:
        print(clean_duplicates(chat_log))
    elif choice == 15:
        print(f"Alphabetical messages: {sort_all_messages(chat_log)}")
    elif choice == 16:
        print(f"Questions found: {get_questions(chat_log)}")
    elif choice == 17:
        print(reply_count(chat_log))
    elif choice == 18:
        print(f"Deleted messages found: {count_deleted(chat_log)}")
    else:
        print("Invalid choice")
