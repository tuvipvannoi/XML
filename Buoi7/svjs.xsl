<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    
    <!-- Xuất ra dạng text -->
    <xsl:output method="text" encoding="UTF-8" indent="no"/>
    
    <xsl:template match="/">
        <xsl:text>[</xsl:text>
        <xsl:for-each select="school/student">
            <xsl:text>{</xsl:text>
            <xsl:text>"masv": "</xsl:text><xsl:value-of select="id"/><xsl:text>", </xsl:text>
            <xsl:text>"hoten": "</xsl:text><xsl:value-of select="name"/><xsl:text>", </xsl:text>
            <xsl:text>"ngaysinh": "</xsl:text><xsl:value-of select="date"/><xsl:text>"}</xsl:text>
            
            <!-- Nếu chưa phải sinh viên cuối cùng thì thêm dấu phẩy -->
            <xsl:if test="position() != last()">
                <xsl:text>,</xsl:text>
            </xsl:if>
        </xsl:for-each>
        <xsl:text>]</xsl:text>
    </xsl:template>
    
</xsl:stylesheet>
