# Codebook Cho `Survey result_Flash sale.sav`

## 1. Mục đích của codebook này

File này dùng để giải thích:

- tên cột trong file `.sav` nghĩa là gì,
- mỗi cột map với câu hỏi thực tế nào trong bảng hỏi gốc,
- biến được mã hóa theo kiểu nào,
- những chỗ nào trong dữ liệu cần lưu ý khi phân tích.

Nguồn đối chiếu:

- `data/Survey data collection.xlsx`: bảng hỏi gốc
- `data/Survey result_Flash sale.sav`: dữ liệu đã làm sạch và mã hóa

## 2. Quy ước mã hóa chung

### 2.1. Câu hỏi thang Likert

Áp dụng cho các cột như `Urgency_1`, `Enjoyment_3`, `Visual_5`...

| Giá trị | Ý nghĩa |
|---|---|
| 1 | Rất không đồng ý |
| 2 | Không đồng ý |
| 3 | Trung lập |
| 4 | Đồng ý |
| 5 | Rất đồng ý |

### 2.2. Câu hỏi chọn nhiều đáp án

Áp dụng cho các cột như `Shopee_Reason_Price`, `FS_Product_Fashion`, `FS_Reason_Discount`...

| Giá trị | Ý nghĩa |
|---|---|
| 0 | Không chọn |
| 1 | Có chọn |

### 2.3. Ghi chú quan trọng

- File `.sav` là bản **đã làm sạch và đã lọc**, không phải bản copy nguyên xi của toàn bộ file Excel gốc.
- File `.sav` hiện có `267` dòng và `79` cột.
- Trong `.sav`, hai cột đầu của thang thời gian được đặt là `Limit_Time_1`, `Limit_Time_2`, trong khi ba cột sau lại là `Time_Limit_3`, `Time_Limit_4`, `Time_Limit_5`. Đây là **lệch tên biến**, không phải khác nội dung.
- Metadata nhãn biến trong file `.sav` không hoàn toàn sạch. Cụ thể, `Shopee_Reason_Variety` đang bị gán nhãn trùng với `Shopee_Reason_Promotion`. Khi phân tích nên ưu tiên **tên cột** và đối chiếu với dữ liệu gốc thay vì chỉ nhìn label của SPSS.
- Một số câu trả lời `Other` trong file gốc không còn được giữ đầy đủ trong `.sav`. Trong mẫu `.sav` hiện tại, các cột `Shopee_Reason_Other`, `FS_Product_Other`, `FS_Reason_Other` đều đang có toàn bộ giá trị bằng `0`.
- Tên cột `FS_Reason_Variety` **gây hiểu nhầm**. Qua đối chiếu từng bản ghi giữa dữ liệu gốc và `.sav`, cột này khớp với lựa chọn:
  `Cơ hội khám phá và trải nghiệm các thương hiệu mới`
  chứ không khớp với lựa chọn:
  `Dễ dàng tiếp cận nhiều loại sản phẩm đa dạng`

## 3. Những cột có trong file gốc nhưng không còn trong `.sav`

Các cột sau xuất hiện trong `Survey data collection.xlsx` nhưng không còn trong file `.sav`:

- `Timestamp`
- 2 câu xác nhận đồng ý tham gia và đồng ý sử dụng dữ liệu
- Câu sàng lọc: đã từng mua Flash Sale trên Shopee chưa
- Câu hỏi mở cuối cùng: đề xuất cải thiện Flash Sale

## 4. Map cột trong `.sav` với câu hỏi gốc

### 4.1. Thông tin hành vi mua sắm chung

| Cột trong `.sav` | Câu hỏi gốc | Kiểu mã hóa |
|---|---|---|
| `STT` | Số thứ tự bản ghi trong file phân tích | Số thứ tự |
| `Shopee_Exp` | 2. Quý vị đã mua sắm trên Shopee được bao lâu? | Mã số |
| `Shopee_Freq` | 3. Tần suất mua sắm trung bình của Quý vị trên Shopee? | Mã số |
| `Shopee_Monthly_Spend` | 4. Mức chi tiêu trung bình hàng tháng của Quý vị trên Shopee? | Mã số |
| `FS_Freq_6m` | 6. Trong 6 tháng gần đây, Quý vị đã mua sắm trong Flash Sale trên Shopee bao nhiêu lần? | Mã số |
| `FS_Occasion` | 7. Quý vị mua sắm trong Flash Sale trên Shopee chủ yếu vào dịp nào? | Mã số |
| `FS_Time` | 8. Quý vị thường mua sắm trong Flash Sale trên Shopee vào thời điểm nào? | Mã số |

#### Bảng mã chi tiết cho các biến hành vi

`Shopee_Exp`

- `1 = Dưới 6 tháng`
- `2 = Từ 6 tháng đến dưới 1 năm`
- `3 = Từ 1 năm đến dưới 2 năm`
- `4 = Từ 2 năm đến dưới 3 năm`
- `5 = Từ 3 năm trở lên`

`Shopee_Freq`

- `1 = 1 lần/tháng hoặc ít hơn`
- `2 = 2 đến 3 lần/tháng`
- `3 = 4 đến 5 lần/tháng`
- `4 = Hơn 6 lần/tháng`

`Shopee_Monthly_Spend`

- `1 = Dưới 500.000 VNĐ`
- `2 = Từ 500.000 đến dưới 1.000.000 VNĐ`
- `3 = Từ 1.000.000 đến dưới 2.000.000 VNĐ`
- `4 = Từ 2.000.000 đến dưới 5.000.000 VNĐ`
- `5 = Trên 5.000.000 VNĐ`

`FS_Freq_6m`

- `1 = 1 đến 3 lần`
- `2 = 4 đến 6 lần`
- `3 = 7 đến 10 lần`
- `4 = Hơn 10 lần`

`FS_Occasion`

- `1 = Các đợt khuyến mãi lớn (Ngày đôi, Tết, Black Friday, v.v.)`
- `2 = Khi có nhu cầu mua sắm cụ thể và cấp thiết`
- `3 = Ngẫu nhiên, không theo dịp cụ thể`

`FS_Time`

- `1 = Buổi sáng (sau 6:00 — 10:00)`
- `2 = Buổi trưa (sau 10:00 — 12:00)`
- `3 = Buổi chiều (sau 12:00 — 18:00)`
- `4 = Buổi tối (sau 18:00 — 00:00)`
- `5 = Buổi đêm (sau 00:00 — 6:00)`

### 4.2. Lý do chọn mua sắm trên Shopee

Nguồn từ Câu 5: `Lý do Quý vị chọn mua sắm trên Shopee? (Chọn tối đa 3 đáp án)`

| Cột trong `.sav` | Map với lựa chọn gốc |
|---|---|
| `Shopee_Reason_Price` | Giá cả hợp lý và cạnh tranh |
| `Shopee_Reason_Variety` | Mẫu mã sản phẩm đa dạng, phong phú |
| `Shopee_Reason_Promotion` | Nhiều chương trình khuyến mãi hấp dẫn |
| `Shopee_Reason_Interface` | Giao diện thân thiện, dễ tìm kiếm sản phẩm |
| `Shopee_Reason_Payment` | Phương thức thanh toán đa dạng và tiện lợi |
| `Shopee_Reason_Delivery` | Dịch vụ giao hàng nhanh chóng và đáng tin cậy |
| `Shopee_Reason_Security` | Chính sách bảo mật dữ liệu cá nhân an toàn và nghiêm ngặt |
| `Shopee_Reason_Other` | Lý do khác |

Ghi chú:

- Trong metadata của file `.sav`, `Shopee_Reason_Variety` đang bị gán nhãn hiển thị là `Shopee_Reason_Promotion`. Đây là lỗi nhãn, không phải bằng chứng cho thấy cột bị trùng dữ liệu.

### 4.3. Danh mục sản phẩm thường mua trong Flash Sale

Nguồn từ Câu 9: `Quý vị thường mua danh mục sản phẩm nào trong Flash Sale trên Shopee? (Chọn tối đa 3 đáp án)`

| Cột trong `.sav` | Map với lựa chọn gốc |
|---|---|
| `FS_Product_Fashion` | Thời trang & Phụ kiện |
| `FS_Product_Electronics` | Điện tử & Gia dụng |
| `FS_Product_Beauty` | Mỹ phẩm & Chăm sóc cá nhân |
| `FS_Product_Food` | Thực phẩm & Đồ uống |
| `FS_Product_Health` | Chăm sóc sức khỏe & Thể thao |
| `FS_Product_Home` | Nội thất & Đồ dùng gia đình |
| `FS_Product_Other` | Danh mục khác |

Ghi chú:

- Trong file gốc có một số trả lời khác như `Sách`, `Mẹ và bé`, `Đồ chơi`...
- Các trả lời này không còn được phản ánh rõ trong cột `FS_Product_Other` của `.sav`.

### 4.4. Lý do chọn mua sắm trong Flash Sale

Nguồn từ Câu 10: `Lý do Quý vị chọn mua sắm trong Flash Sale trên Shopee? (Chọn tối đa 3 đáp án)`

| Cột trong `.sav` | Map với lựa chọn gốc | Ghi chú |
|---|---|---|
| `FS_Reason_Discount` | Mức giảm giá hấp dẫn | Khớp tốt |
| `FS_Reason_Voucher` | Tiết kiệm thêm nhờ voucher giảm giá và miễn phí vận chuyển | Khớp tốt |
| `FS_Reason_Variety` | `Cơ hội khám phá và trải nghiệm các thương hiệu mới` | Đã xác nhận qua đối chiếu bản ghi |
| `FS_Reason_Experience` | Trải nghiệm mua sắm thú vị | Khớp tốt |
| `FS_Reason_Other` | Lý do khác | Trong `.sav` gần như không còn thông tin |

Ghi chú quan trọng:

- Trong file gốc còn có lựa chọn:
  `Dễ dàng tiếp cận nhiều loại sản phẩm đa dạng`
- Qua đối chiếu dữ liệu, lựa chọn này **không có cột tương ứng riêng rõ ràng** trong `.sav` hiện tại.

### 4.5. Thang đo `Time_Limit`

Nguồn từ Câu 11: `Nhận thức về giới hạn thời gian`

| Cột trong `.sav` | Câu hỏi gốc |
|---|---|
| `Limit_Time_1` | Tôi cho rằng thời gian diễn ra Flash Sale bị giới hạn. |
| `Limit_Time_2` | Tôi cho rằng thời gian diễn ra Flash Sale thường rất ngắn. |
| `Time_Limit_3` | Tôi cảm thấy thời gian diễn ra Flash Sale kết thúc rất nhanh. |
| `Time_Limit_4` | Tôi cho rằng Flash Sale không cho tôi đủ thời gian để cân nhắc kĩ lưỡng trước khi mua hàng. |
| `Time_Limit_5` | Tôi lo rằng mình sẽ không kịp mua hàng trước khi Flash Sale kết thúc. |

### 4.6. Thang đo `Qty_Scarcity`

Nguồn từ Câu 12: `Nhận thức về giới hạn số lượng sản phẩm`

| Cột trong `.sav` | Câu hỏi gốc |
|---|---|
| `Qty_Scarcity_1` | Tôi cho rằng số lượng sản phẩm trong Flash Sale bị giới hạn. |
| `Qty_Scarcity_2` | Tôi cho rằng số lượng sản phẩm trong Flash Sale còn rất ít. |
| `Qty_Scarcity_3` | Tôi cho rằng số lượng sản phẩm trong Flash Sale không đủ để đáp ứng nhu cầu của tất cả người mua. |
| `Qty_Scarcity_4` | Tôi cho rằng có nhiều người cùng mua sản phẩm tôi quan tâm trong Flash Sale. |
| `Qty_Scarcity_5` | Tôi cho rằng sản phẩm mình quan tâm trong Flash Sale thường hết hàng rất nhanh. |

### 4.7. Thang đo `Voucher_Scarcity`

Nguồn từ Câu 13: `Nhận thức về giới hạn số lượng voucher`

| Cột trong `.sav` | Câu hỏi gốc |
|---|---|
| `Voucher_Scarcity_1` | Tôi cho rằng số lượng voucher trong Flash Sale bị giới hạn. |
| `Voucher_Scarcity_2` | Tôi cho rằng số lượng voucher trong Flash Sale còn rất ít. |
| `Voucher_Scarcity_3` | Tôi cho rằng số lượng voucher trong Flash Sale không đủ để đáp ứng nhu cầu của tất cả người mua. |
| `Voucher_Scarcity_4` | Tôi cho rằng có nhiều người cùng lấy voucher tôi quan tâm trong Flash Sale. |
| `Voucher_Scarcity_5` | Tôi cho rằng voucher tôi quan tâm trong Flash Sale thường hết rất nhanh. |

### 4.8. Thang đo `Visual`

Nguồn từ Câu 14: `Nhận thức về khả năng hiển thị`

| Cột trong `.sav` | Câu hỏi gốc |
|---|---|
| `Visual_1` | Tôi cho rằng giao diện và bố cục tổng thể của Flash Sale trông bắt mắt. |
| `Visual_2` | Tôi cho rằng hình ảnh sản phẩm, banner và nhãn khuyến mãi trong Flash Sale trông hấp dẫn. |
| `Visual_3` | Tôi cho rằng hình ảnh và đồ họa trong Flash Sale phù hợp với nội dung. |
| `Visual_4` | Tôi cho rằng thông tin trong Flash Sale được hiển thị rõ ràng và dễ hiểu. |
| `Visual_5` | Tôi cho rằng giao diện Flash Sale giúp tôi dễ dàng tìm kiếm thông tin sản phẩm. |

### 4.9. Thang đo `Eco_Benefit`

Nguồn từ Câu 15: `Nhận thức về lợi ích kinh tế`

| Cột trong `.sav` | Câu hỏi gốc |
|---|---|
| `Eco_Benefit_1` | Tôi cho rằng Flash Sale cung cấp mức giảm giá rất hấp dẫn. |
| `Eco_Benefit_2` | Tôi cho rằng Flash Sale cung cấp sản phẩm với giá phải chăng. |
| `Eco_Benefit_3` | Tôi cho rằng Flash Sale cung cấp sản phẩm với giá thấp hơn các chương trình khác. |
| `Eco_Benefit_4` | Tôi cho rằng Flash Sale giúp tôi tiết kiệm tiền mua sản phẩm. |
| `Eco_Benefit_5` | Tôi cho rằng Flash Sale giúp tôi giảm chi phí mua sắm đáng kể. |

### 4.10. Thang đo `Social_Proof`

Nguồn từ Câu 16: `Nhận thức về bằng chứng xã hội`

| Cột trong `.sav` | Câu hỏi gốc |
|---|---|
| `Social_Proof_1` | Tôi thường dựa vào bằng chứng xã hội trong Flash Sale khi quyết định mua hàng. |
| `Social_Proof_2` | Tôi cho rằng bằng chứng xã hội trong Flash Sale giúp tôi hiểu biết thêm về sản phẩm. |
| `Social_Proof_3` | Tôi cho rằng bằng chứng xã hội trong Flash Sale giúp tôi chọn đúng sản phẩm. |
| `Social_Proof_4` | Tôi cho rằng nếu không có bằng chứng xã hội trong Flash Sale, tôi sẽ khó chọn được sản phẩm phù hợp. |
| `Social_Proof_5` | Tôi cảm thấy tự tin hơn khi mua hàng sau khi tham khảo bằng chứng xã hội trong Flash Sale. |

### 4.11. Thang đo `Urgency`

Nguồn từ Câu 17: `Nhận thức về sự cấp bách`

| Cột trong `.sav` | Câu hỏi gốc |
|---|---|
| `Urgency_1` | Tôi cho rằng mình cần phải mua ngay lập tức để sở hữu được sản phẩm này. |
| `Urgency_2` | Tôi cho rằng nếu không mua ngay, sản phẩm sẽ sớm bị bán hết. |
| `Urgency_3` | Tôi cho rằng mình phải quyết định mua nhanh trước khi Flash Sale kết thúc. |
| `Urgency_4` | Tôi cho rằng nếu không mua ngay, tôi có thể bỏ lỡ cơ hội sở hữu sản phẩm với giá ưu đãi. |
| `Urgency_5` | Tôi cho rằng mình sẽ hối tiếc nếu không mua ngay lập tức. |

### 4.12. Thang đo `Enjoyment`

Nguồn từ Câu 18: `Cảm xúc tận hưởng`

| Cột trong `.sav` | Câu hỏi gốc |
|---|---|
| `Enjoyment_1` | Flash Sale khiến tôi cảm thấy vui vẻ. |
| `Enjoyment_2` | Flash Sale khiến tôi cảm thấy hạnh phúc. |
| `Enjoyment_3` | Flash Sale khiến tôi cảm thấy phấn khích. |
| `Enjoyment_4` | Flash Sale khiến tôi cảm thấy thích thú. |
| `Enjoyment_5` | Flash Sale khiến tôi giảm bớt cảm giác mệt mỏi. |

### 4.13. Thang đo `Impulse`

Nguồn từ Câu 19: `Hành vi mua sắm ngẫu hứng`

| Cột trong `.sav` | Câu hỏi gốc |
|---|---|
| `Impulse_1` | Tôi đã mua sản phẩm trong Flash Sale một cách ngẫu hứng. |
| `Impulse_2` | Tôi đã mua sản phẩm trong Flash Sale mà không suy nghĩ kỹ lưỡng. |
| `Impulse_3` | Tôi đã mua sản phẩm trong Flash Sale mà không có kế hoạch từ trước. |
| `Impulse_4` | Tôi đã mua sản phẩm trong Flash Sale mà ban đầu không muốn mua sản phẩm này. |
| `Impulse_5` | Tôi đã mua sản phẩm trong Flash Sale dù ban đầu hoàn toàn không có ý định mua sắm. |

### 4.14. Nhân khẩu học

| Cột trong `.sav` | Câu hỏi gốc | Ghi chú mã hóa |
|---|---|---|
| `Gender` | 20. Giới tính của quý vị? | `1 = Nam`, `2 = Nữ`, `3 = Khác`; trong mẫu `.sav` hiện tại chỉ thấy `Nam`, `Nữ` và thiếu giá trị |
| `Age` | 21. Độ tuổi của quý vị? | `.sav` chỉ còn 2 mã `18 - 29` và `30 - 45`; nhóm `Trên 46` có trong file gốc nhưng không còn là mã riêng trong `.sav` |
| `Education` | 22. Trình độ học vấn của quý vị? | Mã số theo thứ bậc học vấn |
| `Occupation` | 23. Nghề nghiệp của quý vị? | Trong file gốc có thêm `Giảng viên`, `Giáo viên`, `Hưu trí`; trong `.sav` các trường hợp ngoài nhóm chuẩn được biểu diễn bằng mã `7 = Other` |
| `Income` | 24. Mức thu nhập bình quân hàng tháng của quý vị? | Mã số theo mức thu nhập |
| `Marital_Status` | 25. Tình trạng hôn nhân của quý vị? | File gốc có cả `Đã kết hôn và không có con` và `Đã kết hôn và chưa có con`; trong `.sav` chỉ còn nhãn chuẩn `Đã kết hôn và chưa có con`, nhiều khả năng đã được gộp về cùng một mã |
| `Residence` | 26. Quý vị hiện đang sinh sống tại khu vực nào? | `1 = Thành thị`, `2 = Nông thôn` |

#### Bảng mã chi tiết cho nhân khẩu học

`Gender`

- `1 = Nam`
- `2 = Nữ`
- `3 = Khác`

`Age`

- `1 = 18 - 29 (Gen Z)`
- `2 = 30 - 45 (Gen Y/Millennials)`

`Education`

- `1 = Trung học phổ thông trở xuống`
- `2 = Trung cấp`
- `3 = Cao đẳng`
- `4 = Đại học`
- `5 = Sau Đại học`

`Occupation`

- `1 = Học sinh/Sinh viên`
- `2 = Nhân viên văn phòng`
- `3 = Kinh doanh/ Tự doanh`
- `4 = Công chức/ Viên chức`
- `5 = Lao động phổ thông/ Kỹ thuật`
- `6 = Nội trợ`
- `7 = Other`

`Income`

- `1 = Dưới 15 triệu`
- `2 = 15 - 30 triệu`
- `3 = 30 - 45 triệu`
- `4 = Trên 45 triệu`

`Marital_Status`

- `1 = Độc thân`
- `2 = Đã kết hôn và chưa có con`
- `3 = Đã kết hôn và có con`
- `4 = Đã ly hôn/Ly thân`

`Residence`

- `1 = Thành thị`
- `2 = Nông thôn`

## 5. Gợi ý dùng codebook này trong tutorial

Nếu muốn giải thích Cronbach's Alpha bằng đúng dữ liệu thật, nên ưu tiên:

- dùng tên thang đo như `Urgency`, `Enjoyment`, `Time_Limit`,
- trích đúng 2 đến 5 câu hỏi thật trong thang đo đó,
- tránh chỉ nói tên cột vì người đọc sẽ khó hình dung ý nghĩa thực tế.

Ví dụ:

- thay vì chỉ nói `Urgency_1` đến `Urgency_5`,
- nên nói đó là 5 câu hỏi về cảm giác \"phải mua ngay\", \"sợ hết hàng\", \"sợ bỏ lỡ giá ưu đãi\".
