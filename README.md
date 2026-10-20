# open-rewindpix

給 Rewindpix PS135 底片風格數位相機用的非官方 App：換底片、在手機上沖洗照片、存到 iPhone「照片」。它是一個放在相機記憶卡上的網頁，手機連上相機的 Wi-Fi 就能打開。

> 個人研究專案，與 Rewindpix 無關。App 會改寫相機設定，請自行承擔風險。目前只在韌體 V1.2.1D 上測試過。

## 安裝

需要：PS135 相機、iPhone（Safari 或 Brave）、一台能讀記憶卡的電腦。

1. 在這個頁面按 **Code → Download ZIP**，解壓縮。
2. 把記憶卡接到電腦，將 `app` 資料夾**裡面**的 `app.html` 和 `APP` 資料夾複製到記憶卡最上層：

   ```
   記憶卡/
   ├── app.html   ← 新增
   ├── APP/       ← 新增
   └── DCIM/      ← 原本就有，不要動
   ```

3. 手機在**有網路**時，用 Safari 打開一次 https://loldotenv.github.io/open-rewindpix/saver/
   （「存到照片」功能需要這一頁，打開過一次之後離線也能用。）
4. 記憶卡裝回相機，開機，按相機的 **WIFI** 鍵。
5. iPhone 到「設定 → Wi-Fi」連上相機，密碼 `12345678`。顯示「沒有網際網路連線」是正常的。
6. 用 Safari 打開 **http://192.168.1.254/app.html**，再按「分享 → 加入主畫面」。之後從主畫面的圖示開啟即可。

## 更新

下載新版，把 `app/app.html`（和有變動的 `app/APP/` 檔案）複製到記憶卡覆蓋舊檔。App 下次開啟時會自動換成新版。

## 授權

[MIT](LICENSE)。`app/APP/` 裡的樣本照片是 CC0，出處見 [CREDITS.txt](app/APP/CREDITS.txt)。
