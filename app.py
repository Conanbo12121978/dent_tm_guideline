import streamlit as st
from pathlib import Path

st.set_page_config(page_title="แสดงภาพแนวทางปฏิบัติ", layout="centered")
st.title("📋 แนวทางปฏิบัติในหน่วยทันตกรรม")

# โฟลเดอร์ภาพ
folder_path = Path("images")
image_files = [f for f in folder_path.iterdir() if f.suffix.lower() in [".jpg", ".jpeg", ".png"]]

# แสดง dropdown เลือกรูป
if image_files:
    image_dict = {f.stem: f for f in image_files}  # {'ชื่อไฟล์ไม่รวมสกุล': Path}
    selected = st.selectbox("เลือกรูปภาพ", list(image_dict.keys()))
    st.image(image_dict[selected], use_column_width=True, caption=selected)
else:
    st.warning("ยังไม่มีภาพในโฟลเดอร์ images")
