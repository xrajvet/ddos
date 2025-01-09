from time import sleep
from DrissionPage import ChromiumPage

p = ChromiumPage()
p.get('https://nowsecure.nl/')  # تأكد من إزالة المسافة بعد https:
i = p.get_frame('@srcAhttps://challenges.cloudflare.com/cdn-cgi')  # تأكد من أن URL هنا صحيح
e = i.mark()  # إصلاح المسافة الغير ضرورية وتصحيح الاقتباسات
sleep(3)
e.click()  # تصحيح السطر الأخير لإضافة مسافة صحيحة بين الكائن والدالة
