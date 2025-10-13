import mariadb
from lxml import etree
import sys

# === 1. Đường dẫn file XML và XSD ===
XML_FILE = "catalog.xml"
XSD_FILE = "catalog.xsd"

# === 2. Parse file XML, XSD ===
try:
    xml_doc = etree.parse(XML_FILE)
    xsd_doc = etree.parse(XSD_FILE)
    xmlschema = etree.XMLSchema(xsd_doc)
except Exception as e:
    print(f"❌ Lỗi khi đọc file XML/XSD: {e}")
    sys.exit(1)

# === 3. Validate XML với XSD ===
if not xmlschema.validate(xml_doc):
    print("❌ XML KHÔNG HỢP LỆ! Chi tiết lỗi:")
    for error in xmlschema.error_log:
        print(f"  - Dòng {error.line}: {error.message}")
    sys.exit(1)
else:
    print("✅ XML hợp lệ, tiếp tục xử lý dữ liệu...")

# === 4. Kết nối MariaDB ===
try:
    conn = mariadb.connect(
        user="root",
        password="07082004",
        host="localhost",
        database="product"
    )
    cursor = conn.cursor()
except mariadb.Error as e:
    print(f"❌ Lỗi kết nối MariaDB: {e}")
    sys.exit(1)

# === 5. Tạo bảng nếu chưa có ===
cursor.execute("""
CREATE TABLE IF NOT EXISTS Categories (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(255)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10,2),
    currency VARCHAR(10),
    stock INT,
    category_id VARCHAR(10),
    FOREIGN KEY (category_id) REFERENCES Categories(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci
""")

# === 6. Dùng XPath để lấy dữ liệu ===
root = xml_doc.getroot()

# --- Categories ---
for cat in root.xpath("//categories/category"):
    cat_id = cat.get("id")
    cat_name = cat.text.strip() if cat.text else ""
    cursor.execute("""
        INSERT INTO Categories (id, name)
        VALUES (?, ?)
        ON DUPLICATE KEY UPDATE name=VALUES(name)
    """, (cat_id, cat_name))

# --- Products ---
for prod in root.xpath("//products/product"):
    prod_id = prod.get("id")
    category_ref = prod.get("categoryRef")
    name = prod.findtext("name")
    price = float(prod.findtext("price"))
    currency = prod.find("price").get("currency")
    stock = int(prod.findtext("stock"))

    cursor.execute("""
        INSERT INTO Products (id, name, price, currency, stock, category_id)
        VALUES (?, ?, ?, ?, ?, ?)
        ON DUPLICATE KEY UPDATE
            name=VALUES(name),
            price=VALUES(price),
            currency=VALUES(currency),
            stock=VALUES(stock),
            category_id=VALUES(category_id)
    """, (prod_id, name, price, currency, stock, category_ref))

# === 7. Lưu và đóng kết nối ===
conn.commit()
cursor.close()
conn.close()

print("✅ Dữ liệu đã được chèn/cập nhật thành công vào MariaDB!")
