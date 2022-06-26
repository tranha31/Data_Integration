# Data_Itegration

<h3>Mục đich của Repo này là Tích hợp dữ liệu điện thoại từ 4 nguồn:</h3>
<ul>
<li>Thế giới di động</li>
<li>CellPhoneS</li>
<li>Phong Vũ</li>
<li>FPT Shop</li>
</ul>
<br>
----------------------
<br>
<ul>
<li>Bước crawl data nhóm dùng scrapy và splash để crawl từ trang web dùng js để load</li>
<li>Bước schema_matching dùng thuật toán Cupid</li>
<li>Bước data_matching sử dụng hướng tiếp cận phân cụm, dùng độ tương đồng về xâu là fuzzy và jaccard</li>
</ul>
<br>
Bạn hãy tham khảo code để hiểu ý tưởng của nhóm
<br>
----------------------
<br>
<h3>Để chạy chương trình demo cần cài đặt:</h3>
<br>
<ul>
<li>Elasticsearch</li>
<li>MySQL</li>
<li>Thư viện Flask của python, thư viện elasticsearch, thư viện mysql, thư viện fuzzywuzzy</li>
</ul>
<br>
<br>
<ul>
<li>Chạy file config.sql để khởi tạo database</li>
<li>Chạy file matching_data.py để import data vào database. (thư mục data_matching/data_matching)</li>
<li>Chạy elasticsearch. Put data vào elasticsearch theo hướng dẫn trong file matching_data.py</li>
</ul>
<br>
<br>
<ul>
<li>Chạy file controller.py để chạy server backend (folder interface/backend) (chạy elasticsearch trước)</li>
<li>Chạy file phone.html (folder interface/frontend/ui/customer/phone.html)</li>
</ul>