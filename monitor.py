import time
import requests
import json
from DrissionPage import ChromiumPage

LINE_ACCESS_TOKEN = os.environ.get("LINE_ACCESS_TOKEN")
MY_USER_ID = os.environ.get("MY_USER_ID")
PRODUCT_URL = "https://24h.pchome.com.tw/prod/DYAJ01-1900J84BU" 
TARGET_PRICE = 33800                                            

def get_current_price():
    print("🌐 正在啟動真實瀏覽器核心，模擬真人載入網頁...")
    page = ChromiumPage()
    
    try:
        page.get(PRODUCT_URL)
        
        print("⏳ 等待網頁元素與價格載入...")
        time.sleep(3)
        
        elements = page.eles('xpath://span|//h2|//div')
        
        possible_prices = []
        for ele in elements:
            try:
                text = ele.text.strip()
                if '$' in text or any(char.isdigit() for char in text):
                    import re
                    nums = ''.join(re.findall(r'\d+', text))
                    if nums:
                        val = int(nums)
                        if 20000 <= val <= 60000:
                            possible_prices.append(val)
            except Exception:
                continue

        if possible_prices:
            return possible_prices[0]
            
        print("❌ 瀏覽器畫面上找不到符合價格範圍的數字")
        return None

        
    except Exception as e:
        print(f"❌ 瀏覽器自動化操作時發生錯誤: {e}")
        return None
        
    finally:
        page.quit()

def send_line_message(text_content):
    line_url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "to": MY_USER_ID,
        "messages": [{"type": "text", "text": text_content}]
    }
    try:
        response = requests.post(line_url, headers=headers, json=payload)
        if response.status_code == 200:
            print("🔔 LINE 特價通報發送成功！")
        else:
            print(f"❌ LINE 發送失敗，錯誤碼: {response.status_code}")
    except Exception as e:
        print(f"❌ 發送 LINE 訊息時發生異常: {e}")


if __name__ == "__main__":
    print("🚀 2026 電商特價監控爬蟲 (瀏覽器不死版) 正式啟動...")
    print(f"🔍 正在巡邏目標商品：iPhone 17 (512G)")
    
    current_price = get_current_price()
    
    if current_price:
        print(f"💰 成功抓取！目前網路最新售價為：${current_price} 元")
        
        if current_price <= TARGET_PRICE:
            msg = f"🎉【降價通報】\n商品：iPhone 17 (512G)\n目標價：${TARGET_PRICE}\n目前特價只要：${current_price} 元！\n趕快衝啊！網址：{PRODUCT_URL}"
            send_line_message(msg)
        else:
            print(f"📊 目前價格 ${current_price} 尚未低於目標價 ${TARGET_PRICE}，繼續監控。")
    else:
        print("❌ 本次巡邏失敗，未能取得價格。")
