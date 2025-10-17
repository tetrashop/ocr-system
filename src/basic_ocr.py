cat > src/basic_ocr.py << 'EOF'
import os
import json

print("🚀 سیستم OCR پایه راه‌اندازی شد")

class BasicOCRSystem:
    def __init__(self):
        self.name = "سیستم OCR پایه"
        self.version = "1.0.0"
        self.features = [
            "آماده برای توسعه",
            "ساختار ماژولار", 
            "پشتیبانی چندزبانه"
        ]
    
    def get_info(self):
        return {
            "system": self.name,
            "version": self.version,
            "features": self.features,
            "status": "فعال"
        }

if __name__ == "__main__":
    ocr = BasicOCRSystem()
    info = ocr.get_info()
    print("📋 اطلاعات سیستم:", json.dumps(info, ensure_ascii=False, indent=2))
    print("✅ سیستم OCR پایه با موفقیت راه‌اندازی شد")
EOF
