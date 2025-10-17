import json

print("🚀 سیستم OCR پایه راه‌اندازی شد")

class BasicOCRSystem:
    def __init__(self):
        self.name = "سیستم OCR پایه"
        self.version = "1.0.0"
        self.status = "فعال"
    
    def get_info(self):
        return {
            "system": self.name,
            "version": self.version,
            "status": self.status,
            "features": ["تشخیص متن", "پشتیبانی فارسی", "ساختار ماژولار"]
        }

if __name__ == "__main__":
    ocr = BasicOCRSystem()
    info = ocr.get_info()
    print("✅ سیستم OCR پایه با موفقیت راه‌اندازی شد")
    print("📋 اطلاعات سیستم:", json.dumps(info, ensure_ascii=False, indent=2))
