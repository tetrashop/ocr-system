<<<<<<< HEAD
=======
cat > src/basic_ocr.py << 'EOF'
import os
>>>>>>> 6696dc26c2d68a1fb8a993fb10e4aa22387a3ea9
import json

print("🚀 سیستم OCR پایه راه‌اندازی شد")

class BasicOCRSystem:
    def __init__(self):
        self.name = "سیستم OCR پایه"
        self.version = "1.0.0"
<<<<<<< HEAD
        self.status = "فعال"
=======
        self.features = [
            "آماده برای توسعه",
            "ساختار ماژولار", 
            "پشتیبانی چندزبانه"
        ]
>>>>>>> 6696dc26c2d68a1fb8a993fb10e4aa22387a3ea9
    
    def get_info(self):
        return {
            "system": self.name,
            "version": self.version,
<<<<<<< HEAD
            "status": self.status,
            "features": ["تشخیص متن", "پشتیبانی فارسی", "ساختار ماژولار"]
=======
            "features": self.features,
            "status": "فعال"
>>>>>>> 6696dc26c2d68a1fb8a993fb10e4aa22387a3ea9
        }

if __name__ == "__main__":
    ocr = BasicOCRSystem()
    info = ocr.get_info()
<<<<<<< HEAD
    print("✅ سیستم OCR پایه با موفقیت راه‌اندازی شد")
    print("📋 اطلاعات سیستم:", json.dumps(info, ensure_ascii=False, indent=2))
=======
    print("📋 اطلاعات سیستم:", json.dumps(info, ensure_ascii=False, indent=2))
    print("✅ سیستم OCR پایه با موفقیت راه‌اندازی شد")
EOF
>>>>>>> 6696dc26c2d68a1fb8a993fb10e4aa22387a3ea9
