@echo off
chcp 65001 >nul
echo ================================================================
echo สร้างและอัปโหลด GitHub Repository - EdcellenceEdPEx
echo ================================================================
echo.

echo [ขั้นที่ 1] เปิด GitHub เพื่อสร้าง Repository...
echo.
start https://github.com/new?name=EdcellenceEdPEx&description=From+Excellence+Guidelines+to+Computable+Performance+Systems:+BEB-EdPEx+Framework+for+Higher+Education&visibility=public

echo กรุณารอ 5 วินาที...
timeout /t 5 /nobreak >nul

echo.
echo ================================================================
echo คำแนะนำ:
echo ================================================================
echo.
echo 1. เบราว์เซอร์จะเปิดหน้า GitHub (ถ้ายังไม่เปิด กด Enter)
echo 2. ตรวจสอบข้อมูล:
echo    - Repository name: EdcellenceEdPEx
echo    - Description: ถูกกรอกให้แล้ว
echo    - Public: เลือกอยู่แล้ว
echo 3. **สำคัญ: อย่าเลือก "Initialize this repository"**
echo 4. คลิก "Create repository" (ปุ่มเขียว)
echo.

pause

echo.
echo [ขั้นที่ 2] กำลัง Push code ไป GitHub...
echo.

cd /d "%~dp0"
git push -u origin master

if %errorlevel% equ 0 (
    echo.
    echo ================================================================
    echo ✓ สำเร็จ! Repository พร้อมใช้งานแล้ว
    echo ================================================================
    echo.
    echo เปิด Repository:
    start https://github.com/ChatchaiTritham/EdcellenceEdPEx
    echo.
    echo GitHub URL สำหรับใช้ใน Manuscript:
    echo https://github.com/ChatchaiTritham/EdcellenceEdPEx
    echo.
    echo Manuscript Figures อยู่ที่:
    echo %~dp0manuscript_figures
    echo.
    echo ดูคำแนะนำเพิ่มเติมที่:
    echo - MANUSCRIPT_READY_TH.md (ภาษาไทย)
    echo - IEEE_ACCESS_SUBMISSION_GUIDE.md (ภาษาอังกฤษ)
    echo.
) else (
    echo.
    echo ================================================================
    echo เกิดข้อผิดพลาด - กรุณาตรวจสอบ:
    echo ================================================================
    echo.
    echo 1. Repository ถูกสร้างบน GitHub แล้วหรือยัง?
    echo 2. Login GitHub ถูกต้องหรือไม่?
    echo 3. ลองใช้ GitHub Desktop แทน:
    echo    - ดาวน์โหลด: https://desktop.github.com/
    echo    - File ^> Add Local Repository
    echo    - เลือกโฟลเดอร์นี้: %~dp0
    echo    - Publish repository
    echo.
)

echo.
pause
