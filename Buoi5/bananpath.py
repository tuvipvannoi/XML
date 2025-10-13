from lxml import etree
import os

# --- Đọc file XML ---
file_name = "quanlybanan.xml"
if not os.path.exists(file_name):
    print(f"Lỗi: Không tìm thấy file '{file_name}'. Đảm bảo file XML đã được lưu cùng thư mục.")
    exit()

try:
    tree = etree.parse(file_name)
    root = tree.getroot()
    print(f"Đã đọc thành công file '{file_name}'. Bắt đầu truy vấn XPath.\n")
except Exception as e:
    print(f"Lỗi khi đọc file XML: {e}")
    exit()

# Hàm in kết quả dạng Element
def print_elements(title, elements):
    print(title)
    if not elements:
        print("    (Không tìm thấy kết quả)")
        return
    for el in elements:
        print(etree.tostring(el, pretty_print=True, encoding='unicode', xml_declaration=False).strip())

# Hàm in kết quả dạng Text
def print_texts(title, texts):
    print(title)
    if isinstance(texts, list):
        if not texts:
             print("    (Không tìm thấy kết quả)")
             return
        print(f"    {texts}")
    elif isinstance(texts, str):
        print(f"    {texts}")
    else: # Dạng số count
        print(f"    {int(texts)}")

# --- 1. Lấy tất cả bàn ---
bans = root.xpath("//BAN")
print_elements("1. Tất cả bàn:", bans)

# --- 2. Lấy tất cả nhân viên ---
nvs = root.xpath("//NHANVIEN")
print_elements("\n2. Tất cả nhân viên:", nvs)

# --- 3. Lấy tất cả tên món ---
tenmon = root.xpath("//MON/TENMON/text()")
print_texts("\n3. Tên các món:", tenmon)

# --- 4. Tên nhân viên có mã NV02 ---
nv02 = root.xpath("//NHANVIEN[MANV='NV02']/TENV/text()")
print_texts("\n4. Tên NV02:", nv02)

# --- 5. Tên + số điện thoại NV03 ---
# Lấy tên (TENV)
ten_nv03 = root.xpath("//NHANVIEN[MANV='NV03']/TENV/text()")
# Lấy số điện thoại (SDT)
sdt_nv03 = root.xpath("//NHANVIEN[MANV='NV03']/SDT/text()")

# Kết hợp kết quả
nv03 = ten_nv03 + sdt_nv03
print("\n5. Tên và SĐT NV03:", nv03)

# --- 6. (Yêu cầu thêm) Lấy SOHD và MANV của hóa đơn NV03 lập ---
sohd_nv03 = root.xpath("//HOADON[MANV='NV03']/SOHD/text()")
nvhd_nv03 = root.xpath("//HOADON[MANV='NV03']/MANV/text()")
hd_nv03 = sohd_nv03 + nvhd_nv03
print("\n6. SOHD và MANV của hóa đơn NV03 lập:", hd_nv03)

# --- 7. Tên món có giá > 50000 ---
mon_gt50 = root.xpath("//MON[GIA > 50000]/TENMON/text()")
print_texts("\n7. Món giá > 50000:", mon_gt50)

# --- 8. Số bàn hóa đơn HD03 ---
soban_hd03 = root.xpath("//HOADON[SOHD='HD03']/SOBAN/text()")
print_texts("\n8. Số bàn HD03:", soban_hd03)

# --- 9. Tên món mã M02 ---
mon_m02 = root.xpath("//MON[MAMON='M02']/TENMON/text()")
print_texts("\n9. Tên món M02:", mon_m02)

# --- 10. Ngày lập hóa đơn HD03 ---
ngay_hd03 = root.xpath("//HOADON[SOHD='HD03']/NGAYLAP/text()")
print_texts("\n10. Ngày lập HD03:", ngay_hd03)

# --- 11. Mã món trong hóa đơn HD01 ---
mamon_hd01 = root.xpath("//HOADON[SOHD='HD01']/CTHDS/CTHD/MAMON/text()")
print_texts("\n11. Món trong HD01:", mamon_hd01)

# --- 12. Tên nhân viên lập hóa đơn HD01 (Tham chiếu) ---
nv_hd01 = root.xpath("//NHANVIEN[MANV=//HOADON[SOHD='HD01']/MANV]/TENV/text()")
print_texts("\n12. NV lập HD01:", nv_hd01)

# --- 13. Tên nhân viên lập hóa đơn HD02 (Tham chiếu) ---
nv_hd02 = root.xpath("//NHANVIEN[MANV=//HOADON[SOHD='HD02']/MANV]/TENV/text()")
print_texts("\n13. NV lập HD02:", nv_hd02)

# --- 14. Đếm số bàn ---
count_ban = root.xpath("count(//BAN)")
print_texts("\n14. Tổng số bàn:", count_ban)

# --- 15. Đếm số hóa đơn ---
count_hd = root.xpath("count(//HOADON)")
print_texts("\n15. Tổng số hóa đơn:", count_hd)

# --- 16. Đếm số hóa đơn NV01 lập ---
count_hd_nv01 = root.xpath("count(//HOADON[MANV='NV01'])")
print_texts("\n16. Số hóa đơn NV01 lập:", count_hd_nv01)

# --- 17. Tên món trong hóa đơn bàn số 2 (Tham chiếu) ---
mon_ban2 = root.xpath("//MON[MAMON = //HOADON[SOBAN='2']/CTHDS/CTHD/MAMON]/TENMON/text()")
print_texts("\n17. Món trong bàn 2:", mon_ban2)

# --- 18. Nhân viên từng lập hóa đơn bàn số 2 (Tham chiếu) ---
nv_ban2 = root.xpath("//NHANVIEN[MANV=//HOADON[SOBAN='2']/MANV]/TENV/text()")
print_texts("\n18. NV phục vụ bàn 2:", nv_ban2)

# --- 19. Tất cả hóa đơn NV01 lập ---
hd_nv01 = root.xpath("//HOADON[MANV='NV01']")
print_elements("\n19. Hóa đơn NV01:", hd_nv01)

# --- 20. Món NV02 từng phục vụ (Tham chiếu phức tạp) ---
mon_nv02 = root.xpath("//MON[MAMON = //HOADON[MANV='NV02']/CTHDS/CTHD/MAMON]/TENMON/text()")
print_texts("\n20. Món NV02 phục vụ:", mon_nv02)

# --- 21. Món được gọi nhiều hơn 1 lần (Số lượng > 1 trong 1 CTHD bất kỳ) ---
mon_nhieu = root.xpath("//MON[MAMON = //CTHD[SOLUONG > 1]/MAMON]/TENMON/text()")
print_texts("\n21. Món có số lượng > 1 trong 1 CTHD:", mon_nhieu)

# --- 22. Tên bàn + ngày lập hóa đơn HD02 (Tham chiếu + Concat) ---
ban_ngay_hd02 = root.xpath("concat(//BAN[SOBAN=//HOADON[SOHD='HD02']/SOBAN]/TENBAN/text(), ' - ', //HOADON[SOHD='HD02']/NGAYLAP/text())")
print_texts("\n22. Bàn + ngày HD02:", ban_ngay_hd02)