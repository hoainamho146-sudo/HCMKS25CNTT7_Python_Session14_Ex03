# Phân tích và thiết kế giải pháp

# display_students(student_list)
# Input: danh sách học viên
# Output: không trả về giá trị, chỉ hiển thị dữ liệu

# validate_score(score_input)
# Input: điểm người dùng nhập
# Output: True nếu điểm hợp lệ, False nếu không hợp lệ

# find_student_by_id(student_list, student_id)
# Input: danh sách học viên, mã học viên
# Output: dictionary học viên nếu tìm thấy, ngược lại trả về None

# add_student(student_list)
# Input: danh sách học viên
# Output: không trả về giá trị, thêm học viên vào danh sách

# update_score(student_list)
# Input: danh sách học viên
# Output: không trả về giá trị, cập nhật điểm học viên

# get_rank(average_score)
# Input: điểm trung bình
# Output: chuỗi xếp loại học lực

# evaluate_students(student_list)
# Input: danh sách học viên
# Output: không trả về giá trị, hiển thị kết quả đánh giá

# Việc tách chương trình thành nhiều hàm giúp:
# - Dễ đọc và dễ bảo trì
# - Tái sử dụng được code
# - Dễ kiểm tra và sửa lỗi
# - Tránh spaghetti code


students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]


def display_menu():
    """Hiển thị menu chức năng"""
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====")
    print("1. Hiển thị danh sách học viên")
    print("2. Thêm học viên mới")
    print("3. Cập nhật điểm thi theo mã học viên")
    print("4. Đánh giá học lực của toàn bộ học viên")
    print("5. Thoát chương trình")


def validate_score(score_input):
    score_input = score_input.strip()
    if score_input.replace(".", "", 1).isdigit():
        score = float(score_input)
        if 0 <= score <= 10:
            return True
    return False

def find_student_by_id(student_list, student_id):
    for student in student_list:
        if student["student_id"] == student_id:
            return student
    return None

def display_students(student_list):
    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
        return
    for index, student in enumerate(student_list, start=1):
        print(
            f"{index}. Mã: {student['student_id']} | "
            f"Tên: {student['name']} | "
            f"Toán: {student['math_score']} | "
            f"Anh: {student['english_score']}"
        )

def add_student(student_list):
    while True:
        student_id = input("Nhập mã học viên: ").strip().upper()
        if find_student_by_id(student_list, student_id):
            print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
        else:
            break

    while True:
        name = input("Nhập tên học viên: ").strip()
        if name != "":
            name = name.title()
            break
        print("Tên học viên không được để trống!")

    while True:
        math_score = input("Nhập điểm Toán: ")
        if validate_score(math_score):
            math_score = float(math_score)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
      
    while True:
        english_score = input("Nhập điểm Anh: ")
        if validate_score(english_score):
            english_score = float(english_score)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
    student = {
        "student_id": student_id,
        "name": name,
        "math_score": math_score,
        "english_score": english_score
    }
    student_list.append(student)
    print("Thêm học viên thành công!")


def update_score(student_list):
    student_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()
    student = find_student_by_id(student_list, student_id)
    if student is None:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return
    while True:
        math_score = input("Nhập điểm Toán mới: ")
        if validate_score(math_score):
            student["math_score"] = float(math_score)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")

    while True:
        english_score = input("Nhập điểm Anh mới: ")
        if validate_score(english_score):
            student["english_score"] = float(english_score)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
    print("Cập nhật điểm thành công!")


def get_rank(average_score):
    if average_score >= 8:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5:
        return "Trung bình"
    else:
        return "Yếu"

def evaluate_students(student_list):
    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
        return
    for student in student_list:
        average_score = (student["math_score"] + student["english_score"]) / 2
        rank = get_rank(average_score)
        print(
            f"Mã: {student['student_id']} | "
            f"Tên: {student['name']} | "
            f"ĐTB: {average_score:.2f} | "
            f"Xếp loại: {rank}"
        )


while True:
    display_menu()
    choice = input("Nhập lựa chọn: ").strip()
    match choice:
        case "1":
            display_students(students)
        case "2":
            add_student(students)
        case "3":
            update_score(students)
        case "4":
            evaluate_students(students)
        case "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
