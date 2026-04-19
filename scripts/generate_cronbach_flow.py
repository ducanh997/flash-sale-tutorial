from pathlib import Path
import html
from graphviz import Digraph


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def html_label(title: str, body: str) -> str:
    title = html.escape(title)
    body = html.escape(body).replace("\n", "<BR/>")
    return f"""<
    <TABLE BORDER="0" CELLBORDER="0" CELLPADDING="4">
      <TR><TD><B>{title}</B></TD></TR>
      <TR><TD>{body}</TD></TR>
    </TABLE>
    >"""


dot = Digraph("cronbach_alpha_flow_final", engine="dot")
dot.attr(
    rankdir="TB",
    splines="polyline",
    bgcolor="#F6F8FB",
    pad="0.4",
    nodesep="0.5",
    ranksep="0.8",
    fontname="Arial",
    labelloc="t",
    labeljust="c",
    label=(
        "<<FONT POINT-SIZE='28'><B>Flow Đọc Cronbach's Alpha (Digital Marketing)</B></FONT>"
        "<BR/><FONT POINT-SIZE='16'>Kết hợp logic thống kê + lập luận lý thuyết</FONT>>"
    ),
)

dot.attr("node", fontname="Arial", fontsize="13", margin="0.16,0.10")
dot.attr("edge", fontname="Arial", fontsize="11", color="#617C98", penwidth="1.8")


# ===== Nodes =====

dot.node("start",
    label=html_label("Bắt đầu", "Chuẩn bị đánh giá độ tin cậy cho các thang đo"),
    shape="box", style="rounded,filled", fillcolor="#FFFFFF", color="#C8D8E7")

dot.node("group",
    label=html_label("Nhóm item theo construct",
        "Dựa trên lý thuyết: Urgency, Enjoyment, Impulse Buying,\nTime/Qty/Voucher Scarcity..."),
    shape="box", style="rounded,filled", fillcolor="#F4F7FB", color="#C8D8E7")

dot.node("reverse_q",
    label=html_label("Câu hỏi 0",
        "Có item đảo chiều không và đã recode đúng chưa?"),
    shape="diamond", style="filled", fillcolor="#FFF4D8", color="#E7C76A")

dot.node("recode",
    label=html_label("Recode trước",
        "Cần xử lý item đảo chiều trước khi đọc alpha"),
    shape="box", style="rounded,filled", fillcolor="#FFF1EE", color="#DEB0A8")

dot.node("alpha_pre",
    label=html_label("Cronbach's Alpha sơ bộ",
        "Chạy riêng cho từng construct như kiểm tra reliability ban đầu"),
    shape="box", style="rounded,filled", fillcolor="#FFFFFF", color="#C8D8E7")

dot.node("alpha_q",
    label=html_label("Câu hỏi 1",
        "Alpha sơ bộ của construct đang gợi ý điều gì?"),
    shape="diamond", style="filled", fillcolor="#FFF4D8", color="#E7C76A")

dot.node("alpha_low",
    label=html_label("Alpha thấp",
        "alpha < 0.60 thường gợi ý internal consistency yếu"),
    shape="box", style="rounded,filled", fillcolor="#FDEDED", color="#DBA7A7")

dot.node("alpha_mid",
    label=html_label("Alpha mức cân nhắc",
        "0.60–0.70 có thể chấp nhận ở giai đoạn khám phá, tùy bối cảnh"),
    shape="box", style="rounded,filled", fillcolor="#FFF9EC", color="#E7C76A")

dot.node("alpha_good",
    label=html_label("Alpha chấp nhận được",
        "0.70–0.95 thường được xem là phù hợp cho nhiều nghiên cứu hành vi"),
    shape="box", style="rounded,filled", fillcolor="#EEF8F1", color="#B8D7BC")

dot.node("alpha_high",
    label=html_label("Alpha rất cao",
        "> 0.95 có thể gợi ý item trùng lặp hoặc construct quá hẹp"),
    shape="box", style="rounded,filled", fillcolor="#EEF2FF", color="#B7C8E6")

dot.node("review",
    label=html_label("Đọc nội dung item",
        "Kiểm tra ý nghĩa, wording, trùng lặp, đảo chiều"),
    shape="box", style="rounded,filled", fillcolor="#FFFFFF", color="#C8D8E7")

dot.node("content_q",
    label=html_label("Câu hỏi 2",
        "Có vấn đề rõ về nội dung không?"),
    shape="diamond", style="filled", fillcolor="#FFF4D8", color="#E7C76A")

dot.node("content_issue",
    label=html_label("Vấn đề nội dung",
        "Item lệch ý, mơ hồ hoặc sai logic"),
    shape="box", style="rounded,filled", fillcolor="#FFF1EE", color="#DEB0A8")

dot.node("stats",
    label=html_label("Xem chỉ số",
        "CITC + Alpha if Item Deleted (chỉ hỗ trợ, không tự động quyết định)"),
    shape="box", style="rounded,filled", fillcolor="#EEF2FF", color="#B7C8E6")

dot.node("stats_q",
    label=html_label("Câu hỏi 3",
        "Có item đáng nghi không?"),
    shape="diamond", style="filled", fillcolor="#FFF4D8", color="#E7C76A")

dot.node("one_item",
    label=html_label("1 item có vấn đề",
        "CITC thấp hoặc làm alpha tăng"),
    shape="box", style="rounded,filled", fillcolor="#FFF9EC", color="#E7C76A")

dot.node("many_item",
    label=html_label("Nhiều item có vấn đề",
        "Có thể sai ở cấp độ construct hoặc đang có đa chiều"),
    shape="box", style="rounded,filled", fillcolor="#FDEDED", color="#DBA7A7")

dot.node("theory",
    label=html_label("Check lý thuyết",
        "Không loại item nếu nó quan trọng về concept"),
    shape="box", style="rounded,filled", fillcolor="#F4F7FB", color="#C8D8E7")

dot.node("rerun",
    label=html_label("Tinh chỉnh & chạy lại",
        "Lặp lại theo từng construct đến khi thang đo ổn định"),
    shape="box", style="rounded,filled", fillcolor="#FFFFFF", color="#C8D8E7")

dot.node("keep",
    label=html_label("Giữ thang đo tạm thời",
        "Chấp nhận được về nội dung và chỉ số ở bước reliability sơ bộ"),
    shape="box", style="rounded,filled", fillcolor="#EEF8F1", color="#B8D7BC")

dot.node("revise",
    label=html_label("Sửa/loại thang đo",
        "Nếu nhiều vấn đề nghiêm trọng"),
    shape="box", style="rounded,filled", fillcolor="#FDEDED", color="#DBA7A7")

dot.node("efa",
    label=html_label("Kiểm tra cấu trúc",
        "Chạy EFA/CFA để kiểm tra dimensionality và factor structure"),
    shape="box", style="rounded,filled", fillcolor="#EEF8F1", color="#B8D7BC")

dot.node("post_reliability",
    label=html_label("Đánh giá lại reliability",
        "Tính lại Alpha/CR cho từng factor được giữ lại"),
    shape="box", style="rounded,filled", fillcolor="#EEF8F1", color="#B8D7BC")

dot.node("next_step",
    label=html_label("Bước tiếp theo",
        "Measurement model đạt yêu cầu rồi mới sang SEM / kiểm định giả thuyết"),
    shape="box", style="rounded,filled", fillcolor="#EEF8F1", color="#B8D7BC")

dot.node("prelim_note",
    label=html_label("Lưu ý học thuật",
        "Nếu đặt Alpha trước EFA, phải nói rõ đây là preliminary reliability check"),
    shape="note", style="filled", fillcolor="#FFFDF5", color="#E7D9A8")

dot.node("note",
    label=html_label("Lưu ý học thuật",
        "Cronbach's Alpha không kiểm tra unidimensionality;\nalpha cao cũng không tự động chứng minh validity"),
    shape="note", style="filled", fillcolor="#FFFDF5", color="#E7D9A8")

dot.node("threshold_note",
    label=html_label("Diễn giải ngưỡng",
        "Thresholds là context-dependent và nên đọc cùng theory + research stage"),
    shape="note", style="filled", fillcolor="#FFFDF5", color="#E7D9A8")

dot.node("end",
    label=html_label("Kết thúc",
        "Chốt quyết định cho từng construct và giải thích rõ lập luận"),
    shape="box", style="rounded,filled", fillcolor="#FFFFFF", color="#C8D8E7")


# ===== Edges =====

dot.edge("start", "group")
dot.edge("group", "reverse_q")
dot.edge("reverse_q", "recode", label="chưa")
dot.edge("reverse_q", "alpha_pre", label="đã xử lý")
dot.edge("recode", "alpha_pre")
dot.edge("alpha_pre", "alpha_q")

dot.edge("alpha_q", "alpha_low", label="<0.60")
dot.edge("alpha_q", "alpha_mid", label="0.60–0.70")
dot.edge("alpha_q", "alpha_good", label="0.70–0.95")
dot.edge("alpha_q", "alpha_high", label=">0.95")

dot.edge("alpha_low", "review")
dot.edge("alpha_mid", "review")
dot.edge("alpha_good", "review")
dot.edge("alpha_high", "review")

dot.edge("alpha_pre", "prelim_note", style="dashed")
dot.edge("alpha_good", "threshold_note", style="dashed")
dot.edge("alpha_high", "threshold_note", style="dashed")

dot.edge("review", "content_q")
dot.edge("content_q", "content_issue", label="có")
dot.edge("content_q", "stats", label="không rõ")
dot.edge("content_issue", "stats")
dot.edge("stats", "stats_q")
dot.edge("stats_q", "one_item", label="1 item")
dot.edge("stats_q", "many_item", label="nhiều")
dot.edge("stats_q", "keep", label="không đáng ngại")

dot.edge("one_item", "theory")
dot.edge("theory", "rerun", label="loại")
dot.edge("theory", "keep", label="giữ")

dot.edge("rerun", "alpha_pre")

dot.edge("many_item", "revise")

dot.edge("keep", "efa")
dot.edge("efa", "post_reliability")
dot.edge("post_reliability", "next_step")
dot.edge("next_step", "note")
dot.edge("note", "end")

dot.edge("revise", "end")


# ===== Save =====

svg_path = ASSETS / "cronbach_alpha_flow_final.svg"
png_path = ASSETS / "cronbach_alpha_flow_final.png"

svg_path.write_text(dot.pipe(format="svg").decode("utf-8"), encoding="utf-8")
png_path.write_bytes(dot.pipe(format="png"))

print(f"Saved {svg_path}")
print(f"Saved {png_path}")
