<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    
    <xsl:output method="html" encoding="UTF-8" indent="yes"/>
    
    <xsl:template match="/">
        <html>
            <head>
                <title>Kết quả truy vấn quản lý bàn ăn</title>
                <style>
                    body { font-family: Arial; margin: 20px; }
                    table, th, td { border: 1px solid black; border-collapse: collapse; padding: 5px; }
                    th { background-color: #d9eaf7; }
                    h2 { color: darkblue; margin-top: 30px; }
                </style>
            </head>
            
            <body>
                
                <h2>Danh sách tất cả các bàn</h2>
                <table>
                    <tr><th>STT</th><th>Số bàn</th><th>Tên bàn</th></tr>
                    <xsl:for-each select="QUANLY/BANS/BAN">
                        <tr>
                            <td><xsl:value-of select="position()"/></td>
                            <td><xsl:value-of select="SOBAN"/></td>
                            <td><xsl:value-of select="TENBAN"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
                
                <h2>Danh sách nhân viên</h2>
                <table>
                    <tr><th>STT</th><th>Mã NV</th><th>Tên NV</th><th>Giới tính</th><th>SĐT</th><th>Địa chỉ</th></tr>
                    <xsl:for-each select="QUANLY/NHANVIENS/NHANVIEN">
                        <tr>
                            <td><xsl:value-of select="position()"/></td>
                            <td><xsl:value-of select="MANV"/></td>
                            <td><xsl:value-of select="TENV"/></td>
                            <td><xsl:value-of select="GIOITINH"/></td>
                            <td><xsl:value-of select="SDT"/></td>
                            <td><xsl:value-of select="DIACHI"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
                <h2>Danh sách món ăn</h2>
                <table>
                    <tr><th>STT</th><th>Mã món</th><th>Tên món</th><th>Giá</th></tr>
                    <xsl:for-each select="QUANLY/MONS/MON">
                        <tr>
                            <td><xsl:value-of select="position()"/></td>
                            <td><xsl:value-of select="MAMON"/></td>
                            <td><xsl:value-of select="TENMON"/></td>
                            <td><xsl:value-of select="GIA"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
                <h2>Thông tin nhân viên NV02</h2>
                <table>
                    <tr><th>Mã NV</th><th>Tên NV</th><th>Giới tính</th><th>SĐT</th><th>Địa chỉ</th></tr>
                    <xsl:for-each select="QUANLY/NHANVIENS/NHANVIEN[MANV='NV02']">
                        <tr>
                            <td><xsl:value-of select="MANV"/></td>
                            <td><xsl:value-of select="TENV"/></td>
                            <td><xsl:value-of select="GIOITINH"/></td>
                            <td><xsl:value-of select="SDT"/></td>
                            <td><xsl:value-of select="DIACHI"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
                <h2>Danh sách món có giá &gt; 50000</h2>
                <table>
                    <tr><th>STT</th><th>Tên món</th><th>Giá</th></tr>
                    <xsl:for-each select="QUANLY/MONS/MON[GIA &gt; 50000]">
                        <tr>
                            <td><xsl:value-of select="position()"/></td>
                            <td><xsl:value-of select="TENMON"/></td>
                            <td><xsl:value-of select="GIA"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
                <h2>Hóa đơn HD02</h2>
                <table>
                    <tr><th>Số HĐ</th><th>Ngày lập</th><th>Tổng tiền</th><th>Số bàn</th><th>Nhân viên</th></tr>
                    <xsl:for-each select="QUANLY/HOADONS/HOADON[SOHD='HD02']">
                        <tr>
                            <td><xsl:value-of select="SOHD"/></td>
                            <td><xsl:value-of select="NGAYLAP"/></td>
                            <td><xsl:value-of select="TONGTIEN"/></td>
                            <td><xsl:value-of select="SOBAN"/></td>
                            <td><xsl:value-of select="MANV"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
                <h2>Đếm số bàn</h2>
                <p>Tổng số bàn: <b><xsl:value-of select="count(QUANLY/BANS/BAN)"/></b></p>
                <h2>Số hóa đơn lập bởi NV01</h2>
                <p>Số hóa đơn do NV01 lập: <b><xsl:value-of select="count(QUANLY/HOADONS/HOADON[MANV='NV01'])"/></b></p>
                <h2>Danh sách món từng bán cho bàn số 2</h2>
                <table>
                    <tr><th>STT</th><th>Tên món</th></tr>
                    <xsl:for-each select="QUANLY/HOADONS/HOADON[SOBAN=2]/CTHDS/CTHD">
                        <xsl:variable name="mam" select="MAMON"/>
                        <tr>
                            <td><xsl:value-of select="position()"/></td>
                            <td><xsl:value-of select="/QUANLY/MONS/MON[MAMON=$mam]/TENMON"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
                <h2>Nhân viên từng lập hóa đơn cho bàn số 3</h2>
                <table>
                    <tr><th>STT</th><th>Tên nhân viên</th></tr>
                    <xsl:for-each select="QUANLY/HOADONS/HOADON[SOBAN=3]">
                        <xsl:variable name="manv" select="MANV"/>
                        <tr>
                            <td><xsl:value-of select="position()"/></td>
                            <td><xsl:value-of select="/QUANLY/NHANVIENS/NHANVIEN[MANV=$manv]/TENV"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
                <h2>Các món ăn được gọi nhiều hơn 1 lần trong các hóa đơn</h2>
                <table>
                    <tr><th>STT</th><th>Tên món</th><th>Tổng số lượng</th></tr>
                    <xsl:for-each select="QUANLY/MONS/MON">
                        <xsl:variable name="ma" select="MAMON"/>
                        <xsl:variable name="tong" select="sum(//CTHD[MAMON=$ma]/SOLUONG)"/>
                        <xsl:if test="$tong &gt; 1">
                            <tr>
                                <td><xsl:value-of select="position()"/></td>
                                <td><xsl:value-of select="TENMON"/></td>
                                <td><xsl:value-of select="$tong"/></td>
                            </tr>
                        </xsl:if>
                    </xsl:for-each>
                </table>
                <h2>Hóa đơn HD04 chi tiết (Mã món, tên món, đơn giá, tiền)</h2>
                <table>
                    <tr><th>Mã món</th><th>Tên món</th><th>Đơn giá</th><th>Số lượng</th><th>Thành tiền</th></tr>
                    <xsl:for-each select="QUANLY/HOADONS/HOADON[SOHD='HD04']/CTHDS/CTHD">
                        <xsl:variable name="mamon" select="MAMON"/>
                        <xsl:variable name="gia" select="/QUANLY/MONS/MON[MAMON=$mamon]/GIA"/>
                        <xsl:variable name="sol" select="SOLUONG"/>
                        <tr>
                            <td><xsl:value-of select="$mamon"/></td>
                            <td><xsl:value-of select="/QUANLY/MONS/MON[MAMON=$mamon]/TENMON"/></td>
                            <td><xsl:value-of select="$gia"/></td>
                            <td><xsl:value-of select="$sol"/></td>
                            <td><xsl:value-of select="$gia * $sol"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
                
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
