<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  
  <xsl:output method="html" encoding="UTF-8" indent="yes"/>
  
  <xsl:template match="/">
    <html>
      <head>
        <title>Danh sách sinh viên</title>
        <style>
          body {
          background-color: #111;
          color: white;
          font-family: Arial;
          }
          h2 {
          color: #66a3ff;
          }
          table {
          border-collapse: collapse;
          width: auto;
          margin-bottom: 30px;
          }
          th, td {
          border: 1px solid #444;
          padding: 8px;
          text-align: left;
          }
          th {
          background-color: #333;
          color: #fff;
          }
          tr:nth-child(even) {
          background-color: #222;
          }
        </style>
      </head>
      <body>
        <h2>Tất cả sinh viên (Mã, Họ tên, Ngày sinh)</h2>
        <table>
          <tr><th>Mã SV</th><th>Họ tên</th><th>Ngày sinh</th></tr>
          <xsl:for-each select="school/student">
            <tr>
              <td><xsl:value-of select="id"/></td>
              <td><xsl:value-of select="name"/></td>
              <td><xsl:value-of select="date"/></td>
            </tr>
          </xsl:for-each>
        </table>
        
        <h2>Sinh viên sắp xếp theo điểm giảm dần</h2>
        <table>
          <tr><th>Mã SV</th><th>Họ tên</th><th>Điểm</th></tr>
          <xsl:for-each select="school/student">
            <xsl:sort select="grade" data-type="number" order="descending"/>
            <tr>
              <td><xsl:value-of select="id"/></td>
              <td><xsl:value-of select="name"/></td>
              <td><xsl:value-of select="grade"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>Nhóm sinh viên sinh cùng tháng</h2>
        <table>
          <tr><th>STT</th><th>Họ tên</th><th>Tháng sinh</th><th>Ngày sinh</th></tr>
          <xsl:for-each select="school/student">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="name"/></td>
              <td><xsl:value-of select="substring(date,6,2)"/></td>
              <td><xsl:value-of select="date"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2> Danh sách các khóa học</h2>
        <table>
          <tr><th>Mã khóa học</th><th>Tên khóa học</th></tr>
          <xsl:for-each select="school/course">
            <tr>
              <td><xsl:value-of select="id"/></td>
              <td><xsl:value-of select="name"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>Sinh viên học khóa "Hóa học 201"</h2>
        <table>
          <tr><th>Mã SV</th><th>Họ tên</th><th>Khóa học</th></tr>
          <xsl:for-each select="school/enrollment[courseRef=/school/course[name='Hóa học 201']/id]">
            <xsl:variable name="sid" select="studentRef"/>
            <tr>
              <td><xsl:value-of select="$sid"/></td>
              <td><xsl:value-of select="/school/student[id=$sid]/name"/></td>
              <td>Hóa học 201</td>
            </tr>
          </xsl:for-each>
        </table>
        <h2>Sinh viên sinh năm 1997</h2>
        <table>
          <tr><th>Mã SV</th><th>Họ tên</th><th>Ngày sinh</th></tr>
          <xsl:for-each select="school/student[starts-with(date,'1997')]">
            <tr>
              <td><xsl:value-of select="id"/></td>
              <td><xsl:value-of select="name"/></td>
              <td><xsl:value-of select="date"/></td>
            </tr>
          </xsl:for-each>
        </table>
          <h2>Sinh viên có họ “Trần”</h2>
          <table>
            <tr><th>Mã SV</th><th>Họ tên</th><th>Ngày sinh</th><th>Điểm</th></tr>
            <xsl:for-each select="school/student[starts-with(name, 'Trần')]">
              <tr>
                <td><xsl:value-of select="id"/></td>
                <td><xsl:value-of select="name"/></td>
                <td><xsl:value-of select="date"/></td>
                <td><xsl:value-of select="grade"/></td>
              </tr>
            </xsl:for-each>
          </table>

        
      </body>
    </html>
  </xsl:template>
  
</xsl:stylesheet>
