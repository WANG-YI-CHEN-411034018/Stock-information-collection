import twstock
import pandas as pd
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

# 使用者輸入股票代號和日期
target_stock = input("請輸入股票代號：")
start_year = int(input("請輸入開始年份："))
start_month = int(input("請輸入開始月份："))

stock = twstock.Stock(target_stock)  # 告訴 twstock 我們要查詢的股票
target_price = stock.fetch_from(start_year, start_month)  # 取用指定日期至今每天的交易數據

name_attribute = [
    'Date', 'Capacity', 'Turnover', 'Open', 'High', 'Low', 'Close', 'Change',
    'Transcation'
]  # 幫收集到的資料設定表頭

df = pd.DataFrame(columns=name_attribute, data=target_price)
# 將 twstock 抓到的清單轉換成 Data Frame 格式的資料表

filename = f'/content/drive/My Drive/{target_stock}.csv'
# 指定 Data Frame 轉存 csv 檔案的檔案名稱與路徑

df.to_csv(filename)
# 將 Data Frame 轉存為 csv 檔案存放在 Google Drive 中
