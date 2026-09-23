# راه‌اندازی ریپو و GitHub Pages

این پروژه به build، نصب پکیج یا سرور خاصی نیاز نداره. بعد از آپلود فایل‌ها،
GitHub Pages خودکار نسخهٔ آنلاین رو منتشر می‌کنه.

## ۱. ساخت ریپو

در GitHub روی **New repository** بزن و این تنظیمات رو انتخاب کن:

- Repository name: `recaman-cinematic-reel`
- Visibility: `Public`
- گزینه‌های README، `.gitignore` و License رو فعال نکن؛ همهٔ این فایل‌ها داخل
  پکیج آماده هستن.

## ۲. آپلود پروژه

فایل ZIP رو Extract کن و **محتویات داخل پوشه** رو در ریشهٔ ریپو قرار بده؛ یعنی
`index.html` باید مستقیم در صفحهٔ اول ریپو دیده بشه، نه داخل یه پوشهٔ اضافه.

اگه با Git کار می‌کنی:

```bash
git init
git add .
git commit -m "Publish Recamán cinematic reel"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/recaman-cinematic-reel.git
git push -u origin main
```

## ۳. فعال‌کردن GitHub Pages

داخل ریپو برو به:

**Settings → Pages → Build and deployment**

مقدار **Source** رو روی **GitHub Actions** بذار. فایل
`.github/workflows/pages.yml` بقیهٔ فرایند رو خودکار انجام می‌ده.

حالا وارد تب **Actions** شو. اجرای `Deploy GitHub Pages` باید سبز بشه. بعد از
انتشار، لینک پروژه به این شکل می‌شه:

```text
https://YOUR-USERNAME.github.io/recaman-cinematic-reel/
```

هر بار تغییری به شاخهٔ `main` پوش کنی، نسخهٔ آنلاین هم خودکار آپدیت می‌شه.

## ۴. تست قبل از انتشار

در پوشهٔ پروژه این دستور رو اجرا کن:

```bash
python -m http.server 8000
```

بعد برو به <http://localhost:8000> و روی دکمهٔ **گوش کن** بزن. موزیک به‌دلیل
قانون autoplay مرورگر فقط بعد از کلیک کاربر شروع می‌شه.

برای تست کدهای پایتون:

```bash
python -m unittest discover -s tests -v
```

## ۵. لینک مناسب برای اینستاگرام

لینک GitHub Pages رو در Bio بذار و لینک سورس رو هم در README یا Link-in-bio
نگه دار:

```text
Live experience:
https://YOUR-USERNAME.github.io/recaman-cinematic-reel/

Source code:
https://github.com/YOUR-USERNAME/recaman-cinematic-reel
```

برای کپشن می‌تونی بنویسی:

> سورس کامل و نسخهٔ قابل‌اجرا روی GitHub — لینک توی Bio

## اگه انتشار انجام نشد

- چک کن نام شاخه `main` باشه.
- در **Settings → Pages**، منبع انتشار حتماً `GitHub Actions` باشه.
- در تب **Actions**، جزئیات آخرین اجرا رو باز کن.
- مطمئن شو `index.html` در ریشهٔ artifact قرار گرفته؛ workflow آمادهٔ پروژه این
  مورد رو انجام می‌ده.
- برای ریپوی خصوصی، مطمئن شو پلن GitHub حسابت از Pages خصوصی پشتیبانی می‌کنه؛
  ساده‌ترین حالت برای این پروژه ریپوی Public هست.

