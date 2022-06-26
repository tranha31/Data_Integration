# Data_Itegration

Mục đich của Repo này là Tích hợp dữ liệu điện thoại từ 4 nguồn:
- Thế giới di động
- CellPhoneS
- Phong Vũ
- FPT Shop
<br>
----------------------
<br>
1. Bước crawl data nhóm dùng scrapy và splash để crawl từ trang web dùng js để load
2. Bước schema_matching dùng thuật toán Cupid
3. Bước data_matching sử dụng hướng tiếp cận phân cụm, dùng độ tương đồng về xâu là fuzzy và jaccard
<br>
Bạn hãy tham khảo code để hiểu ý tưởng của nhóm
<br>
----------------------
<br>
Để chạy chương trình demo cần cài đặt:
1. Elasticsearch
2. MySQL
3. Thư viện Flask của python, thư viện elasticsearch, thư viện mysql, thư viện fuzzywuzzy
<br>
- Chạy file config.sql để khởi tạo database
- Chạy file matching_data.py để import data vào database. (thư mục data_matching/data_matching)
- Chạy elasticsearch. Put data vào elasticsearch theo hướng dẫn trong file matching_data.py
<br>
Chạy file controller.py để chạy server backend (folder interface/backend) (chạy elasticsearch trước)
Chạy file phone.html (folder interface/frontend/ui/customer/phone.html)