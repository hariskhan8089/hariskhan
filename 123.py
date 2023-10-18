def get_user_data():
    user_data = set()
    while True:
        data = input("Enter data (or type 'quit' to exit): ")
        if data.lower() == 'quit':
            break
        user_data.add(data)
    return user_data

def main():
    user_data = get_user_data()
    print("User data:")
    for data in user_data:
        print(data)

if __name__ == "__main__":
    main()