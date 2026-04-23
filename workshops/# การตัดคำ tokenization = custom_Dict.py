# การตัดคำ tokenization = custom_Dict
import re
LEGAL_KEYWORDS = ["ละเมิดสิทธิบัตร","เครื่องหมายการค้า","ลิขสิทธิ์","การกระทำความผิด"]
def legal_tokenizer(text):
    # ใข้ regex จัดการเบื้องต้น ค่อยตัดส่วนที่เหลือ


    compound = "|".join(map(re.escape,sorted(LEGAL_KEYWORDS,key = len, reverse=True)))
    pattern = compound + r"|[\u0E00-\u0E7F]+" + r"|[a-zA-Z0-9]+"
    tokens = re.findall(pattern, text)
    return re.findall(pattern, text)


test_text = "จำเลยกระทำความผิดฐานละเมิดสิธิบัตรและเครื่องหมายการค้า"
tokens = legal_tokenizer(test_text)
print(f"Input: {test_text}")
print(f"Output: {tokens}")


#import deepcut
#print(f"Output: {deepcut.tokenize(test_text)}")