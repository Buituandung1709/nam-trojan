# File mã độc chính: test-copy.exe
# Khi chạy code nó sẽ tạo ra Auto-start để tự khởi động
## Cách xóa

Mở **Task Manager** (chuột phải Taskbar hoặc Ctrl+Shift+Esc)

Vào **Startup** tìm **win-updater.exe**

Chuột phải chọn **Open file location** và xóa nó đi

Mở **Registry Editor** (regedit)

Tìm đến đường dẫn sau: **Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run**

Xóa **WindowsUpdater**

Xong
# Nội dung repo
```
root
│   bytecode.txt					-- File dữ liệu thô của bytecode sau khi trích xuất qua getbytecode.py
│   getbytecode.py					-- File python trích xuẩt bytecode từ Trojan_test.pyc
│   pyinstxtractor.py*				-- File python trích xuất dữ liệu từ file thực thi test-copy.exe được đóng gói bởi PyInstaller
│   test-copy.exe					-- File trojan gốc được đóng gói bởi PyInstaller
│   Trojan_test1.pyc				-- File bytecode có được sau khi trích xuất file thực thi test-copy.exe
│   Trojan_test1_reconstructed.py	-- File python dịch ngược từ bytecode của Trojan_test.pyc bởi Bùi Tuấn Dũng và tái cấu trúc lại function bởi AI
└───test-copy.exe_extracted			-- Folder dữ liệu được trích xuất từ test-copy.exe qua pyinstxtractor.py
    │   Trojan_test.pyc				-- Vị trí gốc của file bytecode
```
> [!NOTE]
> Code dịch ngược từ bytecode không thể đúng hoàn toàn 100% code gốc
# Virustotal
[Trojan_test1_reconstructed.py](https://www.virustotal.com/gui/file/74817fb36cf2a2da76aafddd379cbb45f9a0d44560db639b5f036ddce5913ab0/detection)

[test-copy.exe](https://www.virustotal.com/gui/file/38fa80082ac63b1dcdbd7d34146523922ef1524518606581bbe240d9ffb086d1/detection)
# Credits
*[extremecoders-re/pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor/)
