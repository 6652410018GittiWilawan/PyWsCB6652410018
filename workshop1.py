import os

def createsub():
    filename = input("ป้อนชื่อไฟล์วิชาเพื่อเก็บข้อมูลคะแนน (xxxxx.txt): ")
    if not filename.endswith(".txt"): print("ชื่อ-นามสกุลไฟล์ไม่ถูกต้อง กรุณาป้อนใหม่"); return
    with open(filename, "w") as f: print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")

def adddatafile():
    files = [f for f in os.listdir() if f.endswith(".txt")]
    if not files: print("ไม่มีไฟล์ใดๆอยู่เลย"); return
    filename = input("เลือกไฟล์โดยการป้อนชื่อไฟล์: ")
    if filename not in files: print("คุณพิมพ์ชื่อไฟล์ผิด"); return
    try:
        with open(filename, "a") as f:
            data = input("ป้อนข้อมูล (ชื่อ-สกุล กลางภาค ปลายภาค เก็บ): ")
            total_score = sum(map(float, data.split()[1:]))
            result = "ผ่าน" if total_score > 50 else "ไม่ผ่าน"
            f.write(f"{data} รวม {total_score} ({result})\n")
        print("เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว")
    except ValueError: print("กรุณาป้อนข้อมูลให้ถูกต้อง")

def displaydata():
    files = [f for f in os.listdir() if f.endswith(".txt")]
    if not files: print("ไม่มีไฟล์ใดๆอยู่เลย"); return
    filename = input("เลือกไฟล์โดยการป้อนชื่อไฟล์: ")
    if filename not in files: print("คุณพิมพ์ชื่อไฟล์ผิด"); return
    try:
        with open(filename, "r") as f: print(f.read())
    except FileNotFoundError: print("ไฟล์ไม่พบ")

def deletef():
    files = [f for f in os.listdir() if f.endswith(".txt")]
    if not files: print("ไม่มีไฟล์ใดๆอยู่เลย"); return
    filename = input("เลือกไฟล์โดยการป้อนชื่อไฟล์: ")
    if filename not in files: print("คุณพิมพ์ชื่อไฟล์ผิด"); return
    os.remove(filename); print("ลบไฟล์เรียบร้อยแล้ว")

def main():
    while True:
        print("1. สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล\n2. เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์\n3. เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล\n4. เลือกวิชาและลบไฟล์\n0. จบการทำงาน")
        choice = input("เลือกเมนู: ")
        if choice == '1': createsub()
        elif choice == '2': adddatafile()
        elif choice == '3': displaydata()
        elif choice == '4': deletef()
        elif choice == '0': print("จบการทำงาน"); break
        else: print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")

if __name__ == "__main__":
    main()