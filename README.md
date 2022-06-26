# Data_Itegration

<h1>Mục đich của Repo này là Tích hợp dữ liệu điện thoại từ 4 nguồn:</h1>
- Thế giới di động
- CellPhoneS
- Phong Vũ
- FPT Shop
<br>
----------------------
<br>
- Bước crawl data nhóm dùng scrapy và splash để crawl từ trang web dùng js để load
- Bước schema_matching dùng thuật toán Cupid
- Bước data_matching sử dụng hướng tiếp cận phân cụm, dùng độ tương đồng về xâu là fuzzy và jaccard
<br>
Bạn hãy tham khảo code để hiểu ý tưởng của nhóm
<br>
----------------------
<br>
<h1>Để chạy chương trình demo cần cài đặt:</h1>
<br>
- Elasticsearch
- MySQL
- Thư viện Flask của python, thư viện elasticsearch, thư viện mysql, thư viện fuzzywuzzy
<br>
<br>
- Chạy file config.sql để khởi tạo database
- Chạy file matching_data.py để import data vào database. (thư mục data_matching/data_matching)
- Chạy elasticsearch. Put data vào elasticsearch theo hướng dẫn trong file matching_data.py
<br>
<br>
- Chạy file controller.py để chạy server backend (folder interface/backend) (chạy elasticsearch trước)
- Chạy file phone.html (folder interface/frontend/ui/customer/phone.html)