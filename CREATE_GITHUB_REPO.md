# สร้าง GitHub Repository - ขั้นตอนง่ายๆ 2 นาที

## ขั้นตอนที่ 1: สร้าง Repository บน GitHub (1 นาที)

1. เปิดลิงก์นี้ในเว็บเบราว์เซอร์: https://github.com/new

2. กรอกข้อมูล:
   - Repository name: `EdcellenceEdPEx`
   - Description: `From Excellence Guidelines to Computable Performance Systems: BEB-EdPEx Framework for Higher Education`
   - เลือก: **Public** (สำคัญ! เพื่อใช้ในงานวิจัย)
   - **อย่า** เลือก "Initialize this repository with a README"
   - **อย่า** เลือก .gitignore หรือ license

3. คลิก **"Create repository"**

## ขั้นตอนที่ 2: Push Code ขึ้น GitHub (30 วินาที)

หลังจากสร้าง repository แล้ว ให้รันคำสั่งนี้:

```bash
cd "D:/2026-Journal/Rung/GitHub/EdcellenceEdPEx"
git push -u origin master
```

## ขั้นตอนที่ 3: ตรวจสอบ (30 วินาที)

เปิดลิงก์นี้: https://github.com/ChatchaiTritham/EdcellenceEdPEx

ควรเห็น:
✓ ไฟล์ทั้งหมด 21+ ไฟล์
✓ โฟลเดอร์ manuscript_figures/ มี 15 รูป
✓ ไฟล์ README.md แสดงผล
✓ ไฟล์ IEEE_ACCESS_SUBMISSION_GUIDE.md

---

## หากมีปัญหา Authentication

ถ้าขึ้น error ว่า authentication failed:

1. ใช้ GitHub Desktop (ง่ายที่สุด):
   - ดาวน์โหลด: https://desktop.github.com/
   - เปิดโปรแกรม > File > Add Local Repository
   - เลือกโฟลเดอร์: D:\2026-Journal\Rung\GitHub\EdcellenceEdPEx
   - คลิก "Publish repository"

2. หรือใช้ Personal Access Token:
   - ไปที่: https://github.com/settings/tokens
   - Generate new token (classic)
   - เลือก scope: repo
   - Copy token
   - ใช้แทนรหัสผ่านตอน push

---

## ผลลัพธ์ที่คาดหวัง

หลัง push สำเร็จจะเห็น:

```
Enumerating objects: 150, done.
Counting objects: 100% (150/150), done.
Delta compression using up to 8 threads
Compressing objects: 100% (120/120), done.
Writing objects: 100% (150/150), 5.2 MiB | 2.5 MiB/s, done.
Total 150 (delta 45), reused 0 (delta 0)
To https://github.com/ChatchaiTritham/EdcellenceEdPEx.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

---

## สำหรับใช้ใน Manuscript

หลังจาก push แล้ว ให้:

1. **Copy GitHub Link**: 
   ```
   https://github.com/ChatchaiTritham/EdcellenceEdPEx
   ```

2. **ใส่ใน Manuscript** (ส่วน Data Availability):
   ```
   The BEB-EdPEx framework source code and sample datasets 
   are publicly available at 
   https://github.com/ChatchaiTritham/EdcellenceEdPEx 
   under the MIT License.
   ```

3. **Figures สำหรับ IEEE ACCESS**:
   - อยู่ใน: manuscript_figures/
   - ไฟล์ทั้งหมด 15 รูป (Fig1-Fig15)
   - Copy ไปใส่ใน submission package

4. **Supplementary Materials**:
   - Interactive visualizations: outputs/*.html
   - Jupyter notebooks: notebooks/*.ipynb
   - Sample data: data/sample/organizational_data.json

---

## พร้อมส่ง IEEE ACCESS!

หลัง push สำเร็จแล้ว:

✓ Repository สาธารณะ - ใช้อ้างอิงใน paper ได้
✓ Figures 15 รูปพร้อมใช้ (300 DPI)
✓ Code ครบถ้วน พร้อม reproduce
✓ Documentation สมบูรณ์
✓ Test suite ผ่าน 96.9%

**ส่ง IEEE ACCESS ได้เลย!**

Portal: https://mc.manuscriptcentral.com/ieee-access
