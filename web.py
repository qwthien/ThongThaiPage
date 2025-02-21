import streamlit as st

def main():
    st.set_page_config(page_title="Kỹ Năng Quan Trọng Trong Thời Đại AI", layout="wide")
    
    st.title("Kỹ Năng Quan Trọng Trong Thời Đại AI")
    st.subheader("Lý do AI không thể thay thế con người")
    
    st.markdown("""
    ### 1. Kỹ năng giao tiếp và tương tác xã hội
    **Chủ đề:**
    - Nghệ thuật lắng nghe và thấu hiểu người khác.
    - Kỹ năng đàm phán và thuyết phục.
    - Xây dựng mối quan hệ trong công việc và cuộc sống.
    
    **Lý do AI không thể thay thế:**
    - AI thiếu khả năng thấu hiểu cảm xúc phức tạp của con người.
    - Giao tiếp hiệu quả đòi hỏi sự đồng cảm và trải nghiệm thực tế.
    
    ---
    
    ### 2. Kỹ năng lãnh đạo và quản lý con người
    **Chủ đề:**
    - Phong cách lãnh đạo truyền cảm hứng.
    - Quản lý xung đột trong nhóm.
    - Xây dựng văn hóa doanh nghiệp.
    
    **Lý do AI không thể thay thế:**
    - Lãnh đạo đòi hỏi khả năng ra quyết định dựa trên giá trị và đạo đức.
    - AI không thể hiểu được động lực và cảm xúc của từng cá nhân.
    
    ---
    
    ### 3. Kỹ năng sáng tạo và tư duy đổi mới
    **Chủ đề:**
    - Phương pháp brainstorm ý tưởng mới.
    - Tư duy thiết kế (Design Thinking).
    - Sáng tạo trong nghệ thuật, văn học, và âm nhạc.
    
    **Lý do AI không thể thay thế:**streamlit run
    - Sáng tạo đòi hỏi trí tưởng tượng và cảm hứng, điều mà AI không có.
    - AI chỉ có thể mô phỏng hoặc kết hợp ý tưởng có sẵn.
    
    ---
    
    ### 4. Cách triển khai trong cộng đồng
    - **Chia sẻ kinh nghiệm thực tế**: Thành viên có thể kể lại câu chuyện cá nhân.
    - **Tổ chức workshop**: Mời chuyên gia chia sẻ về kỹ năng lãnh đạo, giao tiếp.
    - **Thử thách phát triển**: "Thử thách 7 ngày lắng nghe tích cực".
    - **Tạo tài nguyên hữu ích**: Ebook, checklist, video hướng dẫn.
    """)
    
    if st.button("Tải xuống tài liệu đầy đủ"):
        with open("ky_nang_con_nguoi.txt", "w", encoding="utf-8") as file:
            file.write("Nội dung đầy đủ của bài viết...")
        st.success("Tài liệu đã được tải xuống thành công!")

if __name__ == "__main__":
    main()
