from lxml import etree

# --- Đọc file XML ---
tree = etree.parse("sinhvien.xml")
root = tree.getroot()

# --- 1. Lấy tất cả sinh viên ---
students = root.xpath("//student")
print("1. Tất cả sinh viên:")
for s in students:
    print(etree.tostring(s, pretty_print=True).decode())

# --- 2. Liệt kê tên tất cả sinh viên ---
names = root.xpath("//student/name/text()")
print("\n2. Tên tất cả sinh viên:", names)

# --- 3. Lấy tất cả id sinh viên ---
ids = root.xpath("//student/id/text()")
print("\n3. ID sinh viên:", ids)

# --- 4. Lấy ngày sinh SV01 ---
dob_sv01 = root.xpath("//student[id='SV01']/date/text()")
print("\n4. Ngày sinh SV01:", dob_sv01)

# --- 5. Lấy các khóa học ---
courses = root.xpath("//enrollment/course/text()")
print("\n5. Danh sách khóa học:", courses)

# --- 6. Thông tin sinh viên đầu tiên ---
first_student = root.xpath("//student[1]")
print("\n6. Thông tin sinh viên đầu tiên:")
print(etree.tostring(first_student[0], pretty_print=True).decode())

# --- 7. Mã sinh viên đăng ký môn 'Vatly203' ---
sv_vatly = root.xpath("//enrollment[course='Vatly203']/studentRef/text()")
print("\n7. Sinh viên học Vatly203:", sv_vatly)

# --- 8. Tên sinh viên học 'Toan101' ---
sv_toan = root.xpath("//student[id=//enrollment[course='Toan101']/studentRef]/name/text()")
print("\n8. Sinh viên học Toan101:", sv_toan)

# --- 9. Tên sinh viên học 'Vatly203' ---
sv_vatly_name = root.xpath("//student[id=//enrollment[course='Vatly203']/studentRef]/name/text()")
print("\n9. Sinh viên học Vatly203:", sv_vatly_name)

# --- 10. Ngày sinh SV01 (lặp lại) ---
print("\n10. Ngày sinh SV01:", dob_sv01)

# --- 11. Tên và ngày sinh sinh năm 1997 ---
sv_1997 = root.xpath("//student[starts-with(date, '1997')]")
print("\n11. Sinh viên sinh năm 1997:")
for s in sv_1997:
    name = s.findtext("name")
    date = s.findtext("date")
    print(f" - {name} ({date})")

# --- 12. Tên sinh viên có ngày sinh trước 1998 ---
sv_truoc_1998 = root.xpath("//student[number(substring(date,1,4)) < 1998]/name/text()")
print("\n12. Sinh viên sinh trước 1998:", sv_truoc_1998)

# --- 13. Đếm tổng số sinh viên ---
count_sv = root.xpath("count(//student)")
print("\n13. Tổng số sinh viên:", int(count_sv))

# --- 14. Sinh viên chưa đăng ký môn nào ---
sv_no_course = root.xpath("//student[not(id = //enrollment/studentRef)]/name/text()")
print("\n14. Sinh viên chưa đăng ký môn học:", sv_no_course)

# --- 15. Phần tử <date> anh em ngay sau <name> của SV01 ---
date_after_name = root.xpath("//student[id='SV01']/name/following-sibling::date/text()")
print("\n15. <date> sau <name> SV01:", date_after_name)

# --- 16. Phần tử <id> anh em ngay trước <name> của SV02 ---
id_before_name = root.xpath("//student[id='SV02']/name/preceding-sibling::id/text()")
print("\n16. <id> trước <name> SV02:", id_before_name)

# --- 17. Node <course> trong enrollment của SV03 ---
course_sv03 = root.xpath("//enrollment[studentRef='SV03']/course/text()")
print("\n17. Môn học của SV03:", course_sv03)

# --- 18. Sinh viên có họ “Trần” ---
sv_tran = root.xpath("//student[starts-with(name, 'Trần')]/name/text()")
print("\n18. Sinh viên họ Trần:", sv_tran)

# --- 19. Năm sinh SV01 ---
year_sv01 = root.xpath("substring(//student[id='SV01']/date,1,4)")
print("\n19. Năm sinh SV01:", year_sv01)
