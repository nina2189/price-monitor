# 🛒 PChome 24h 價格監控 LINE 機器人

一個基於 Python 與 GitHub Actions 的輕量級價格監控工具。每當 PChome 商品價格跌破您設定的目標價（如限時下殺、歷史最低價），系統將自動透過 LINE 官方帳號發送警報通知！

## ✨ 特色功能
隱藏 API 串接：直接讀取 PChome 後端 JSON 資料，避開動態 HTML 載入陷阱，穩定度高。
最低價精準捕捉：優先偵測 歷史最低促銷價 欄位，完美捕捉限時特價。
完全免開電腦：利用 GitHub Actions 雲端排程，24 小時在背景默默守候。
資安合規：敏感的 LINE Token 與 User ID 皆透過密碼抽屜保護，代碼安全可公開。

### 1. 準備工作
請先至 [LINE Developers](https://line.biz) 後台申請並取得以下兩項憑證：
Channel access token (long-lived) (LINE 權杖)
Your user ID (您的 LINE 帳號辨識碼，以 U 開頭)

### 2. 貼上秘密金鑰 (GitHub Secrets)
請至本專案的 Setting > Secrets and variables > Actions > New repository secret 
分別新增兩筆資料：
1. LINE_ACCESS_TOKEN 您的LINE權杖(不要加引號)
2. MY_USER_ID 您的User ID(不要加引號)

### 3. 修改商品與目標價
打開 monitor.py，修改以下兩個變數即可完成設定：
python
PRODUCT_URL = "您的 PChome 商品網址"
TARGET_PRICE = 33000  # 您心目中的理想便宜價

## ⏰ 巡邏時間設定
目前設定每天於台灣時間 **05:13**、**11:27**、**19:42**（皆已刻意避開整點大塞車時段）自動發動巡邏。您也可以隨時到 GitHub Actions 點選 Run workflow 進行手動即時測試。









