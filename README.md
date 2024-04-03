# Stock-information-collection  
這個 Python 程式可讓使用者使用 twstock 庫從台灣證券交易所檢索歷史股票資料。資料將被收集並存儲為 CSV 檔案在 Google 雲端硬碟上。   
## [twstock](https://github.com/mlouielu/twstock)  
* twstock是由Louie Lu開發的Python模組，使用這個模組便能輕易取得台灣證券交易所以及證券交易櫃買中心的資料，包括個股資訊、歷史價格、均價、均量、乖離值、及四大買賣點分析等，甚至能在盤中直接抓取即時價格資料，非常好用但似乎只能爬台股的資訊，無法爬ETF的
** 無法抓00929的資料:
  ![image](https://github.com/WANG-YI-CHEN-411034018/Stock-information-collection/blob/main/stock_img/1712179282258.jpg)  
## 使用說明：
* 連接 Google 雲端硬碟：  
在運行程式之前，您需要將 Google 雲端硬碟連接以便儲存收集到的資料。請確保您有適當的權限以訪問 Google 雲端硬碟。

* 輸入股票資訊：
程式提示時，輸入您想要檢索資料的股票代碼（例如，對於台積電，輸入“2330”）以及開始日期（年份和月份）。
* 資料檢索與存儲：  
程式將從指定的開始日期檢索歷史股票資料直到當前日期。  
收集到的資料將被格式化為資料框並保存為 CSV 檔案在您的 Google 雲端硬碟上。
* 台積電(2330)從2024/4/1~2024/4/3號的資訊
  ![image](https://github.com/WANG-YI-CHEN-411034018/Stock-information-collection/blob/main/stock_img/1712179308796.jpg)  
