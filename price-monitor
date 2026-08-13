import os
import sys
import requests
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PRODUCT_URL = "https://24h.pchome.com.tw/prod/DYAJ01-1900J84BU"
TARGET_PRICE = 33000

LINE_ACCESS_TOKEN = os.environ.get("LINE_ACCESS_TOKEN")
MY_USER_ID = os.environ.get("MY_USER_ID")


def get_current_price():
    try:
        prod_id = PRODUCT_URL.split("prod/")[-1].split("?")[0]
        api_url = 'https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/button&id=' + prod_id
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Origin": "https://pchome.com.tw",
            "Referer": "https://pchome.com.tw/"
        }        
        response = requests.get(api_url, headers=headers, timeout=10)
        data = response.json()
        

        prod_data = data[0] if isinstance(data, list) else data.get(prod_id, {})
        current_price = prod_data.get("Price", {}).get("Low") or prod_data.get("Price", {}).get("P")
        
        return int(current_price)
    except Exception as e:
        print(f"❌ 嘗試解析商品編號或售價時發生錯誤：{e}")
        return None


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
    response = requests.post(line_url, headers=headers, json=payload)


    print(f"📡 LINE 伺服器回傳狀態：{response.status_code} - {response.text}")
    print("  LINE 特價訊息已成功投遞至您的手機！")
    
    return response.status_code    

def main():
    print("🚀 2026 電商特價監控爬蟲正式啟動...")
    print(f"🔍 正在巡邏目標商品：iPhone 17 (512G)")
    
    price = get_current_price()
    
    if price is not None:
        print(f"📊 監控回報：目前 PChome 網路即時售價為 {price} 元")
        print(f"🎯 您的目標便宜價設定為：{TARGET_PRICE} 元")
        
        if price <= TARGET_PRICE:
            print("🔥 發現符合期望特價！正在發送 LINE 機器人通知...")
            msg = f"🛒 【特價警報】您監控的商品降價啦！\n📱 商品：Apple 蘋果 iPhone 17 (512G)\n💰 目前即時售價：{price} 元\n🔗 商品傳送門：{PRODUCT_URL}"
            send_line_message(msg)
            print("✅ LINE 特價訊息已成功投遞至您的手機！")
        else:
            print("⏳ 目前價格還太貴，持續背景巡邏中，不發送通知打擾。")


if __name__ == "__main__":
    main()

