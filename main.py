from api_tests import GetBooksTest, CreateUserTest, DeleteUserTest, PutTest
from ui_tests import LoginTest, ButtonTest
from api_tests.get_books_test import GetBooksTest
from api_tests.create_user_test import CreateUserTest
from api_tests.delete_user_test import DeleteUserTest
from api_tests.put_test import PutTest
from ui_tests.login_test import LoginTest
from ui_tests.collection_test import ButtonTest

def main():
    base_url = "https://demoqa.com"
    token = "YOUR_ACCESS_TOKEN"
    driver_path = "msedgedriver.exe" #chromela falan değiştiririz bunu 

    print("Select an option:")
    print("1. Run API Get Books Test")
    print("2. Run API Create User Test")
    print("3. Run API Delete User Test")
    print("4. Run API Update User Test")
    print("5. Run UI Login Test")
    print("6. Run UI Button Test")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        test = GetBooksTest(base_url)
        test.get_books()
    elif choice == 2:
        test = CreateUserTest(base_url)
        username = input("Enter username: ")
        password = input("Enter password: ")
        test.create_user(username, password)
    elif choice == 3:
        test = DeleteUserTest(base_url, token)
        user_id = input("Enter user ID to delete: ")
        test.delete_user(user_id)
    elif choice == 4:
        test = PutTest(base_url, token)
        user_id = input("Enter user ID to update: ")
        new_data = {"userName": input("Enter new username: ")}
        test.update_user(user_id, new_data)
    elif choice == 5:
        test = LoginTest(driver_path)
        url = f"{base_url}/login"
        username = input("Enter username: ")
        password = input("Enter password: ")
        test.login(url, username, password)
    elif choice == 6:
        test = ButtonTest(driver_path)
        url = f"{base_url}/buttons"
        test.test_buttons()
    elif choice == 0:
        print("Exiting...")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
# bu demoqa.com daki bookstore apı da deniyorum vakti olan https://demoqa.com/swagger/ şurdan baksın biraz https://demoqa.com/login burası da var totali düzenli gibi de hala
# problemleri var 