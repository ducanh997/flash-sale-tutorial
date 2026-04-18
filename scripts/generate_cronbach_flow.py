from pathlib import Path

from graphviz import Digraph


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)


def html_label(title: str, body: str) -> str:
    body = body.replace("\n", "<BR/>")
    return f"""<
    <TABLE BORDER="0" CELLBORDER="0" CELLPADDING="4">
      <TR><TD><B>{title}</B></TD></TR>
      <TR><TD>{body}</TD></TR>
    </TABLE>
    >"""


dot = Digraph("cronbach_alpha_flow", engine="dot")
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
        "<<FONT POINT-SIZE='28'><B>Flow Đọc Kết Quả Cronbach's Alpha</B></FONT>"
        "<BR/><FONT POINT-SIZE='16'>Nhìn alpha trước, rồi mới soi tiếp từng item</FONT>>"
    ),
)

dot.attr("node", fontname="Arial", fontsize="13", margin="0.16,0.10")
dot.attr("edge", fontname="Arial", fontsize="11", color="#617C98", penwidth="1.8")


dot.node(
    "start",
    label=html_label("Bắt đầu", "Nhìn Cronbach's Alpha của thang đo"),
    shape="box",
    style="rounded,filled",
    fillcolor="#FFFFFF",
    color="#C8D8E7",
)

dot.node(
    "alpha_q",
    label=html_label("Câu hỏi 1", "Alpha đã đủ ổn để dùng tiếp chưa?"),
    shape="diamond",
    style="filled",
    fillcolor="#FFF4D8",
    color="#E7C76A",
    width="2.9",
    height="1.25",
)

dot.node(
    "alpha_low",
    label=html_label(
        "Alpha chưa ổn",
        "alpha &lt; 0.70.<BR/>Đừng kết luận vội, cần kiểm tra lại thang đo trước khi phân tích tiếp.",
    ),
    shape="box",
    style="rounded,filled",
    fillcolor="#FFF1EE",
    color="#DEB0A8",
)

dot.node(
    "alpha_ok",
    label=html_label(
        "Alpha khá ổn",
        "alpha &gt;= 0.70.<BR/>Có thể dùng tiếp, nhưng nếu muốn chắc hơn thì xem tiếp từng item.",
    ),
    shape="box",
    style="rounded,filled",
    fillcolor="#EEF8F1",
    color="#B8D7BC",
)

dot.node(
    "review",
    label=html_label("Đọc lại từng item", "Xem câu hỏi có thật sự đi cùng một ý hay không."),
    shape="box",
    style="rounded,filled",
    fillcolor="#FFFFFF",
    color="#C8D8E7",
)

dot.node(
    "item_q",
    label=html_label(
        "Câu hỏi 2",
        "Có item nào lệch ý, mơ hồ,<BR/>đảo chiều chưa xử lý hoặc quá giống câu khác không?",
    ),
    shape="diamond",
    style="filled",
    fillcolor="#FFF4D8",
    color="#E7C76A",
    width="3.3",
    height="1.45",
)

dot.node(
    "content_issue",
    label=html_label(
        "Nếu có vấn đề ở nội dung",
        "Xem lại mã hóa hoặc item đảo chiều.<BR/>Nếu vẫn bất ổn thì ghi nhận hạn chế hoặc cân nhắc loại item.",
    ),
    shape="box",
    style="rounded,filled",
    fillcolor="#FFF1EE",
    color="#DEB0A8",
)

dot.node(
    "item_stats",
    label=html_label(
        "Nếu chưa thấy vấn đề rõ",
        "Xem CITC trước,<BR/>rồi đọc thêm Cronbach's Alpha if Item Deleted.",
    ),
    shape="box",
    style="rounded,filled",
    fillcolor="#EEF2FF",
    color="#B7C8E6",
)

dot.node(
    "suspicious",
    label=html_label(
        "Item đáng nghi",
        "CITC &lt; 0.30 hoặc bỏ item làm alpha tăng rõ:<BR/>có thể cân nhắc loại.",
    ),
    shape="box",
    style="rounded,filled",
    fillcolor="#FFF9EC",
    color="#E7C76A",
)

dot.node(
    "keep",
    label=html_label(
        "Thường có thể giữ",
        "CITC ổn và bỏ item không làm alpha tăng rõ.",
    ),
    shape="box",
    style="rounded,filled",
    fillcolor="#F4F7FB",
    color="#C8D8E7",
)

dot.node(
    "drop_scale",
    label=html_label(
        "Cân nhắc loại cả thang đo",
        "Nếu đã kiểm tra mà alpha vẫn thấp,<BR/>hoặc có quá nhiều item có vấn đề,<BR/>có thể không dùng cả thang đo này.",
    ),
    shape="box",
    style="rounded,filled",
    fillcolor="#FDEDED",
    color="#DBA7A7",
)


with dot.subgraph() as same_rank:
    same_rank.attr(rank="same")
    same_rank.node("alpha_low")
    same_rank.node("alpha_ok")

with dot.subgraph() as same_rank:
    same_rank.attr(rank="same")
    same_rank.node("content_issue")
    same_rank.node("item_stats")

with dot.subgraph() as same_rank:
    same_rank.attr(rank="same")
    same_rank.node("drop_scale")
    same_rank.node("suspicious")
    same_rank.node("keep")


dot.edge("start", "alpha_q")
dot.edge("alpha_q", "alpha_low", label="chưa ổn")
dot.edge("alpha_q", "alpha_ok", label="khá ổn")
dot.edge("alpha_low", "review")
dot.edge("alpha_ok", "review")
dot.edge("review", "item_q")
dot.edge("item_q", "content_issue", label="có")
dot.edge("item_q", "item_stats", label="không rõ / không có")
dot.edge("item_stats", "suspicious")
dot.edge("item_stats", "keep")
dot.edge("content_issue", "drop_scale", label="vẫn yếu")
dot.edge("suspicious", "drop_scale", label="nhiều item đáng nghi")


svg_path = ASSETS / "cronbach_alpha_flow.svg"
png_path = ASSETS / "cronbach_alpha_flow.png"

svg_path.write_text(dot.pipe(format="svg").decode("utf-8"))
png_path.write_bytes(dot.pipe(format="png"))

print(f"Saved {svg_path}")
print(f"Saved {png_path}")
