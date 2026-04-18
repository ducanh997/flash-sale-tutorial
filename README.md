# Flash Sale Cronbach Alpha

Project này chứa một notebook tutorial bằng tiếng Việt để giải thích **Cronbach's Alpha** bằng chính bộ dữ liệu khảo sát về **Shopee Flash Sale**.

Mục tiêu của notebook là:

- giải thích Cronbach's Alpha theo cách dễ hiểu với người học marketing,
- dùng ví dụ thật từ bộ dữ liệu thay vì chỉ nói lý thuyết,
- kiểm tra độ tin cậy của các thang đo như `Urgency`, `Enjoyment`, `Impulse`.

## File chính

- `main.ipynb`: notebook tutorial chính.
- `data/SAV_CODEBOOK.md`: codebook giải thích tên cột trong file `.sav`, mapping với câu hỏi gốc và các lưu ý khi diễn giải dữ liệu.
- `requirements.txt`: các thư viện Python cần thiết để mở và chạy notebook.

## File dữ liệu

Notebook sử dụng 2 file dữ liệu nguồn:

- `data/Survey result_Flash sale.sav`: dữ liệu đã làm sạch và mã hóa, là nguồn trực tiếp cho phần tính Cronbach's Alpha.
- `data/Survey data collection.xlsx`: file bảng hỏi/nguồn gốc để đối chiếu nội dung câu hỏi.

Hai file này hiện đã được thêm vào `.gitignore`, nên sẽ **không được push lên git**.

## Cách chạy

```bash
pip install -r requirements.txt
jupyter lab main.ipynb
```

## Nội dung notebook

Notebook hiện gồm các phần chính:

- mở đầu bằng một tình huống gần với marketer để giải thích vì sao cần Cronbach's Alpha,
- ví dụ thật từ dữ liệu cho các thang đo như `Urgency` và `Enjoyment`,
- ví dụ giả định về trường hợp alpha thấp,
- ví dụ giả định về **câu hỏi đảo chiều** và vì sao cần đảo mã,
- bảng thuật ngữ để người mới học dễ theo dõi,
- phần tính Cronbach's Alpha cho từng thang đo trong bộ dữ liệu.

## Lưu ý dữ liệu

- Kết quả trong notebook được tính trên `267` quan sát trong file `.sav`, không phải toàn bộ phản hồi trong file Excel gốc.
- Với các câu hỏi chọn nhiều đáp án, mỗi lựa chọn thường được tách thành một cột riêng theo dạng `1 = Có chọn`, `0 = Không chọn`.
- Nếu cần hiểu một cột trong `.sav` tương ứng với câu hỏi gốc nào, nên xem `data/SAV_CODEBOOK.md`.

## Kiểm tra kết quả

Các giá trị Cronbach's Alpha tính lại từ notebook đã được đối chiếu với file phân tích `Analysed data_Flash sales.pdf` và **khớp nhau theo làm tròn 3 chữ số thập phân**.
