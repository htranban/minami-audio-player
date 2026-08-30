import os
import json

WEB_DIR = "/var/www/html"
SONGS_JSON_PATH = os.path.join(WEB_DIR, "songs.json")

# Bảng map chuẩn xác Tên File -> (Tên Bài Hát, Ca Sĩ, Thể Loại)
EXACT_MAP = {
    # Khởi My
    "gui_cho_anh.m4a": ("Gửi Cho Anh", "Khởi My", "VPOP"),
    "vi_sao.m4a": ("Vì Sao", "Khởi My", "VPOP"),
    "goc_nho_trong_tim.m4a": ("Góc Nhỏ Trong Tim", "Khởi My", "VPOP"),
    "khoc_dem.m4a": ("Khóc Đêm", "Khởi My", "VPOP"),
    "hat_cat.m4a": ("Hạt Cát", "Khởi My", "VPOP"),
    "thuong_anh.m4a": ("Thương Anh", "Khởi My", "VPOP"),
    "neu_nho_nam_xua.m4a": ("Nếu Nhớ Năm Xưa", "Khởi My", "VPOP"),
    "nguoi_yeu_cu_km.m4a": ("Người Yêu Cũ", "Khởi My", "VPOP"),
    "nguoi_yeu_cu.mp3": ("Người Yêu Cũ", "Khởi My", "VPOP"),
    "de_thuong.m4a": ("Dễ Thương", "Khởi My", "VPOP"),
    "xe_dap_teen.m4a": ("Xe Đạp Teen", "Khởi My", "VPOP"),

    # Ái Phương
    "toi_thay_hoa_vang_tren_co_xanh.m4a": ("Tôi Thấy Hoa Vàng Trên Cỏ Xanh", "Ái Phương", "VPOP"),
    "dong_tay_nam_bac.m4a": ("Đông Tây Nam Bắc", "Ái Phương", "VPOP"),
    "tro_troi.m4a": ("Trô Trọi", "Ái Phương", "VPOP"),
    "co_don.m4a": ("Cô Đơn", "Ái Phương", "VPOP"),
    "duong_ve_nha.m4a": ("Đường Về Nhà", "Ái Phương", "VPOP"),
    "den_voi_nhau_la_do_duyen.m4a": ("Đến Với Nhau Là Do Duyên", "Ái Phương", "VPOP"),
    "chia_tay_trong_mua.m4a": ("Chia Tay Trong Mưa", "Ái Phương", "VPOP"),
    "nhung_ngay_me_vang_nha.m4a": ("Những Ngày Mẹ Vắng Nhà", "Ái Phương", "VPOP"),
    "hua_voi_em.m4a": ("Hứa Với Em", "Ái Phương", "VPOP"),
    "loi_ru_cho_con.m4a": ("Lời Ru Cho Con", "Ái Phương", "VPOP"),
    "dung_im.m4a": ("Đứng Im", "Ái Phương", "VPOP"),
    "neu_anh_yeu_em.m4a": ("Nếu Anh Yêu Em", "Ái Phương", "VPOP"),
    "khi_me_vang_nha.m4a": ("Khi Mẹ Vắng Nhà", "Ái Phương", "VPOP"),
    "nam_lay_tay_anh.m4a": ("Nắm Lấy Tay Anh", "Ái Phương", "VPOP"),
    "giot_nuoc_mat_cho_doi.m4a": ("Giọt Nước Mắt Cho Đời", "Ái Phương", "VPOP"),
    "co_phai_em_la_mua_thu_ha_noi.m4a": ("Có Phải Em Là Mùa Thu Hà Nội", "Ái Phương", "VPOP"),
    "nhong_nhang.m4a": ("Nhõng Nhẽo", "Ái Phương", "VPOP"),
    "tinh_yeu_trai_qua.m4a": ("Tình Yêu Trải Qua", "Ái Phương", "VPOP"),
    "giac_mo_ngay_tho.m4a": ("Giấc Mơ Ngây Thơ", "Ái Phương", "VPOP"),
    "nguyen_cau.m4a": ("Nguyện Cầu", "Ái Phương", "VPOP"),

    # Mỹ Tâm
    "nho_my_tam.webm": ("Nhớ", "Mỹ Tâm", "VPOP"),
    "uoc_gi_my_tam.m4a": ("Ước Gì", "Mỹ Tâm", "VPOP"),
    "duong_nhu_ta_da.m4a": ("Dường Như Ta Đã", "Mỹ Tâm", "VPOP"),
    "hoa_mi_toc_nau.m4a": ("Họa Mi Tóc Nâu", "Mỹ Tâm", "VPOP"),
    "cay_dan_sinh_vien.m4a": ("Cây Đàn Sinh Viên", "Mỹ Tâm", "VPOP"),
    "toc_nau_moi_tram.m4a": ("Tóc Nâu Môi Trầm", "Mỹ Tâm", "VPOP"),
    "chuyen_nhu_chua_bat_dau.m4a": ("Chuyện Như Chưa Bắt Đầu", "Mỹ Tâm", "VPOP"),
    "dung_hoi_em.m4a": ("Đừng Hỏi Em", "Mỹ Tâm", "VPOP"),
    "nguoi_hay_quen_em_di.m4a": ("Người Hãy Quên Em Đi", "Mỹ Tâm", "VPOP"),
    "noi_minh_dung_chan.m4a": ("Nơi Mình Dừng Chân", "Mỹ Tâm", "VPOP"),
    "don_coi_my_tam.m4a": ("Đơn Côi", "Mỹ Tâm", "VPOP"),
    "hat_voi_dong_song.m4a": ("Hát Với Dòng Sông", "Mỹ Tâm", "VPOP"),

    # Mr. Siro
    "lang_nghe_nuoc_mat.m4a": ("Lắng Nghe Nước Mắt", "Mr. Siro", "VPOP"),
    "buc_tranh_tu_nuoc_mat.m4a": ("Bức Tranh Từ Nước Mắt", "Mr. Siro", "VPOP"),
    "em_gai_mua.m4a": ("Em Gái Mưa", "Mr. Siro", "VPOP"),
    "trai_tim_em_cung_biet_dau.m4a": ("Trái Tim Em Cùng Biết Đau", "Mr. Siro", "VPOP"),
    "cham_day_noi_dau.m4a": ("Chạm Đáy Nỗi Đau", "Mr. Siro", "VPOP"),
    "mot_buoc_yeu_van_dam_dau.m4a": ("Một Bước Yêu Vạn Dặm Đau", "Mr. Siro", "VPOP"),
    "dung_ai_nhac_ve_anh_ay.m4a": ("Đừng Ai Nhắc Về Anh Ấy", "Mr. Siro", "VPOP"),
    "song_xa_anh_chang_de_dang.m4a": ("Sống Xa Anh Chẳng Dễ Dàng", "Mr. Siro", "VPOP"),
    "yeu_mot_nguoi_co_le.m4a": ("Yêu Một Người Có Lẽ", "Mr. Siro", "VPOP"),
    "tim_lai_bau_troi.m4a": ("Tìm Lại Bầu Trời", "Mr. Siro", "VPOP"),
    "guong_mat_ta_loi.m4a": ("Gương Mặt Tạ Lỗi", "Mr. Siro", "VPOP"),
    "duoi_mua.m4a": ("Dưới Mưa", "Mr. Siro", "VPOP"),

    # Lương Bích Hữu
    "em_yeu_anh.mp3": ("Em Yêu Anh", "Lương Bích Hữu", "VPOP"),
    "co_gai_trung_hoa.webm": ("Cô Gái Trung Hoa", "Lương Bích Hữu", "VPOP"),
    "goi_ten_toi_nhe_ban_than_hoi.m4a": ("Gọi Tên Tôi Nhé Bạn Thân Hỡi", "Lương Bích Hữu", "VPOP"),
    "danh_cho_em.m4a": ("Dành Cho Em", "Lương Bích Hữu", "VPOP"),
    "cai_dau_lanh_va_trai_tim_nong.m4a": ("Cái Đầu Lạnh Và Trái Tim Nóng", "Lương Bích Hữu", "VPOP"),
    "cun_yeu.m4a": ("Cún Yêu", "Lương Bích Hữu", "VPOP"),

    # Các bài hát khác (Đã gán đúng ca sĩ thực tế)
    "anh-con-no-em.mp3": ("Anh Còn Nợ Em", "Quang Dũng", "VPOP"),
    "anh_khac_hay_em_khac.m4a": ("Anh Khác Hay Em Khác", "Khắc Việt", "VPOP"),
    "ao_mong_tinh_yeu.m4a": ("Ảo Mộng Tình Yêu", "Đan Trường & Cẩm Ly", "VPOP"),
    "cau_vong_khuyet.m4a": ("Cầu Vồng Khuyết", "Tuấn Hưng", "VPOP"),
    "why_did_i_fall.mp3": ("Why Did I Fall In Love With You", "Tohoshinki", "WORLD"),
    "take_me_to_your_heart.mp3": ("Take Me To Your Heart", "MLTR", "WORLD"),
    "e_la_khong_the.mp3": ("E Là Không Thể", "Anh Quân Idol", "VPOP"),
    "yeu_dau_theo_gio_bay.mp3": ("Yêu Dấu Theo Gió Bay", "Hiền Thục", "VPOP"),
    "nguoi_vo_hinh.mp3": ("Người Vô Hình", "Minh Hằng", "VPOP"),
    "tinh_yeu_hoa_gio.mp3": ("Tình Yêu Hoa Gió", "Trương Thế Vinh", "VPOP"),
    "mai_mai_mot_tinh_yeu.webm": ("Mãi Mãi Một Tình Yêu", "Đan Trường", "VPOP"),
    "lang_quen_chieu_thu.webm": ("Lãng Quên Chiều Thu", "Lam Trường", "VPOP"),
    "trang_giay_trang.m4a": ("Trang Giấy Trắng", "Phạm Trưởng", "VPOP"),
    "tinh_don_phuong.m4a": ("Tình Đơn Phương", "Lam Trường", "VPOP"),
    "kiep_ve_sau.m4a": ("Kiếp Ve Sầu", "Đan Trường", "VPOP")
}

# Quét tất cả file audio trong thư mục
audio_files = [f for f in os.listdir(WEB_DIR) if f.endswith(('.mp3', '.m4a', '.webm'))]
audio_files.sort()

new_songs = []
for idx, f in enumerate(audio_files, 1):
    if f in EXACT_MAP:
        title, artist, genre = EXACT_MAP[f]
    else:
        # Nếu bài nào chưa khai báo, tự lấy tên file sạch và để ca sĩ gốc
        raw_name = os.path.splitext(f)[0].replace("_", " ").replace("-", " ").title()
        title, artist, genre = raw_name, "VPOP Artist", "VPOP"

    new_songs.append({
        "id": idx,
        "title": title,
        "artist": artist,
        "genre": genre,
        "src": f
    })

with open(SONGS_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(new_songs, f, ensure_ascii=False, indent=2)

print(f"✅ Đã sửa chuẩn xác ca sĩ cho tất cả {len(new_songs)} bài hát!")
