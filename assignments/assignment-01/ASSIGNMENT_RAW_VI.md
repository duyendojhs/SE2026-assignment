BT cá nhân 1 – AI-03 – RE-027
BỐI CẢNH CÁ NHÂN HÓA (RE-027)
Bạn phân tích đề tài “AI-03 – GitHub Project Coach cho nhóm sinh viên” của nhóm SE2026-T07. Stakeholder trọng tâm của bài là quản trị viên chịu trách nhiệm về quyền truy cập. Trong quá trình phát triển, một chính sách mới yêu cầu xóa dữ liệu cá nhân theo yêu cầu. Ràng buộc tổ chức: yêu cầu ban đầu còn nhiều giả định chưa kiểm chứng. Tham số riêng của biến thể: 302 người dùng hoạt động đồng thời, dữ liệu được lưu 41 ngày và nhóm có 20 giờ để phản hồi change request.

YÊU CẦU THỰC HIỆN
1. Software Engineering trong kỷ nguyên AI (15 điểm): Nêu ba lý do một MVP do AI sinh ra có thể chạy được nhưng chưa đủ tin cậy để bàn giao. Phân tích trách nhiệm của kỹ sư khi AI có nguy cơ: AI bỏ qua xung đột giữa hai stakeholder.
2. Software Process (20 điểm): Chọn Waterfall, iterative/incremental, Scrum, Kanban hoặc quy trình AI-native kết hợp. Thiết kế workflow 1 tuần có tối thiểu 5 checkpoint từ yêu cầu đến bản build kiểm chứng được. Giải thích vì sao workflow phù hợp với ràng buộc trên và nêu một trade-off.
3. Product Thinking (20 điểm): Viết problem statement không chứa tên công nghệ; xác định user outcome, product outcome và hai giả định nguy hiểm. Tạo stakeholder map tối thiểu 4 bên, chỉ rõ một xung đột cần giải quyết.
4. Requirements Engineering (30 điểm): Viết 4 user stories; mỗi story có acceptance criteria Given/When/Then, gồm ít nhất một failure case. Viết một quality attribute scenario cho Performance tập trung vào thời gian phản hồi và tải đồng thời, với số đo có thể kiểm thử. Lập MoSCoW cho MVP và chỉ rõ mục nào không làm trong vòng đầu.
5. Engineering evidence và AI reflection (15 điểm): Bổ sung một ma trận stakeholder–need–conflict. Đính kèm prompt và một phần output AI đã dùng; đánh dấu ít nhất hai chỗ bạn sửa hoặc bác bỏ, kèm lý do. Tạo bảng truy vết ngắn: Outcome → Requirement → Acceptance criterion → Planned test.

ĐẦU RA: Một file PDF tối đa 6 trang, không tính phụ lục prompt. Bài làm phải sử dụng đúng stakeholder, biến cố, ràng buộc và quality attribute của biến thể RE-027. Không sao chép artefact của nhóm hoặc của sinh viên khác.
HƯỚNG DẪN NỘP BÀI

1. Nơi nộp
Nộp bài cá nhân trực tiếp vào Assignment tương ứng trên Google Classroom. Không gửi bài qua email và không nộp vào GitHub repo của nhóm.

2. File phải nộp
• Nộp 01 file PDF duy nhất.
• Tên file: BT1_23001857_<Mã biến thể>.pdf
Ví dụ: BT1_23001898_RE-001.pdf
• Tối đa 6 trang nội dung chính; phụ lục khai báo sử dụng AI không tính vào giới hạn 6 trang.
• Không nộp file Word, ZIP hoặc đường dẫn yêu cầu giảng viên cấp quyền truy cập.

3. Thông tin bắt buộc ở trang đầu
• Họ và tên.
• Mã sinh viên: 23001857.
• Mã biến thể được ghi trong tên bài.
• Team ID và mã đề tài của nhóm.
• Cam kết: “Tôi chịu trách nhiệm về toàn bộ nội dung bài làm và đã khai báo việc sử dụng AI.”

4. Cấu trúc bài làm
Trình bày theo đúng thứ tự các phần trong đề:
• Software Engineering trong kỷ nguyên AI.
• Software Process.
• Product Thinking.
• Requirements Engineering.
• Engineering Evidence và AI Reflection.
• Phụ lục AI Usage Log.

5. Khai báo sử dụng AI
Sinh viên được phép sử dụng AI nhưng phải chịu trách nhiệm về nội dung nộp. Trong phụ lục, ghi công cụ đã dùng, prompt chính, nội dung AI đề xuất, phần đã giữ/sửa/bác bỏ và lý do. Không cần nộp toàn bộ lịch sử chat.

6. Lưu ý
• Bài phải sử dụng đúng stakeholder, biến cố, ràng buộc, tham số và quality attribute của biến thể cá nhân.
• Kiểm tra đúng mã sinh viên và mã biến thể trước khi nộp.
• Có thể nộp lại trước deadline; phiên bản cuối cùng trên Google Classroom được sử dụng để chấm.
• Giảng viên có thể yêu cầu sinh viên giải thích trực tiếp một số nội dung trong bài để xác minh tính cá nhân.

Khung chấm điểm
Tiêu chí	Điểm	Yêu cầu
Software Engineering trong kỷ nguyên AI	15	Phân biệt software chạy được với software đáng tin cậy; nêu trách nhiệm kiểm chứng và phân tích đúng failure mode AI được giao.
Lựa chọn và thiết kế Software Process	20	Workflow 1 tuần có ≥5 checkpoint; lựa chọn process có lập luận; thể hiện feedback, verification và một trade-off.
Problem framing và Product Thinking	20	Problem statement không chốt sẵn giải pháp; outcome rõ; stakeholder map ≥4 bên; có conflict và giả định cần kiểm chứng.
User stories và Acceptance Criteria	20	4 stories có giá trị người dùng; Given/When/Then quan sát được; có boundary/failure case; không phụ thuộc vô lý vào implementation.
Quality requirement và MVP scope	15	Quality scenario có source, stimulus, environment, response và measurable response; MoSCoW nhất quán với outcome và giới hạn MVP.
Engineering evidence và sử dụng AI	10	Có artefact evidence, prompt/output, ít nhất 2 chỉnh sửa hoặc bác bỏ có lý do, và traceability từ outcome đến planned test.