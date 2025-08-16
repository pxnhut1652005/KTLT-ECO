def greeting(name):                  # Định nghĩa hàm greeting với tham số name
    print("Hello,", name)            # In ra màn hình chuỗi "Hello, " kèm theo tên
import mymodule as mm                 # Import module mymodule và đặt tên tắt là mm
mm.greeting("Alan")                   # Gọi hàm greeting trong module, truyền vào "Alan"
