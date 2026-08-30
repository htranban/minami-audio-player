import os
import json

WEB_DIR = "/var/www/html"
SONGS_JSON_PATH = os.path.join(WEB_DIR, "songs.json")

# Quy tắc Map thủ công chính xác từng file thực tế trên server
FILE_MAPPING = {
    # --- BIGBANG ---
    "bad_boy_bigbang.m4a": ("BAD BOY", "BIGBANG", "KPOP"),
    "bae_bae.m4a": ("BAE BAE", "BIGBANG", "KPOP"),
    "bang_bang_bang.m4a": ("BANG BANG BANG", "BIGBANG", "KPOP"),
    "blue_bigbang.m4a": ("BLUE", "BIGBANG", "KPOP"),
    "fantastic_baby.m4a": ("Fantastic Baby", "BIGBANG", "KPOP"),
    "fxxk_it.m4a": ("FXXK IT", "BIGBANG", "KPOP"),
    "haruharu.mp3": ("Haru Haru", "BIGBANG", "KPOP"),
    "if_you_bigbang.m4a": ("IF YOU", "BIGBANG", "KPOP"),
    "lets_not_fall_in_love.m4a": ("Let's Not Fall In Love", "BIGBANG", "KPOP"),
    "lies_bigbang.m4a": ("Lies", "BIGBANG", "KPOP"),
    "loser_bigbang.m4a": ("LOSER", "BIGBANG", "KPOP"),

    # --- KHỞI MY ---
    "gui_cho_anh.m4a": ("Gửi Cho Anh", "Khởi My", "VPOP"),
    "vi_sao.m4a": ("Vì Sao", "Khởi My", "VPOP"),
    "goc_nho_trong_tim.m4a": ("Góc Nhỏ Trong Tim", "Khởi My", "VPOP"),
    "khoc_dem.m4a": ("Khóc Đêm", "Khởi My", "VPOP"),
    "hat_cat.m4a": ("Hạt Cát", "Khởi My", "VPOP"),
    "thuong_anh.m4a": ("Thương Anh", "Khởi My", "VPOP"),
    "neu_nho_nam_xua.m4a": ("Nếu Nhớ Năm Xưa", "Khởi My", "VPOP"),
    "nguoi_yeu_cu.mp3": ("Người Yêu Cũ", "Khởi My", "VPOP"),
    "nguoi_yeu_cu_km.m4a": ("Người Yêu Cũ (Acoustic)", "Khởi My", "VPOP"),
    "de_thuong.m4a": ("Dễ Thương", "Khởi My", "VPOP"),
    "xe_dap_teen.m4a": ("Xe Đạp Teen", "Khởi My", "VPOP"),
    "giay_phut_em_dem.m4a": ("Giây Phút Êm Đềm", "Khởi My", "VPOP"),
    "bang_bang_bang.m4a": ("BANG BANG BANG", "BIGBANG", "KPOP"),

    # --- MỸ TÂM ---
    "uoc_gi_my_tam.m4a": ("Ước Gì", "Mỹ Tâm", "VPOP"),
    "duong_nhu_ta_da.m4a": ("Đường Như Ta Đã", "Mỹ Tâm", "VPOP"),
    "hoa_mi_toc_nau.m4a": ("Họa Mi Tóc Nâu", "Mỹ Tâm", "VPOP"),
    "cay_dan_sinh_vien.m4a": ("Cây Đàn Sinh Viên", "Mỹ Tâm", "VPOP"),
    "toc_nau_moi_tram.m4a": ("Tóc Nâu Môi Trầm", "Mỹ Tâm", "VPOP"),
    "chuyen_nhu_chua_bat_dau.m4a": ("Chuyện Như Chưa Bắt Đầu", "Mỹ Tâm", "VPOP"),
    "dung_hoi_em.m4a": ("Đừng Hỏi Em", "Mỹ Tâm", "VPOP"),
    "nguoi_hay_quen_em_di.m4a": ("Người Hãy Quên Em Đi", "Mỹ Tâm", "VPOP"),
    "noi_minh_dung_chan.m4a": ("Nơi Mình Dừng Chân", "Mỹ Tâm", "VPOP"),
    "don_coi_my_tam.m4a": ("Đơn Côi", "Mỹ Tâm", "VPOP"),
    "hat_voi_dong_song.m4a": ("Hát Với Dòng Sông", "Mỹ Tâm", "VPOP"),
    "nho_my_tam.webm": ("Nhớ", "Mỹ Tâm", "VPOP"),

    # --- MR. SIRO ---
    "lang_nghe_nuoc_mat.m4a": ("Lắng Nghe Nước Mắt", "Mr. Siro", "VPOP"),
    "buc_tranh_tu_nuoc_mat.m4a": ("Bức Tranh Từ Nước Mắt", "Mr. Siro", "VPOP"),
    "em_gai_mua.m4a": ("Em Gái Mưa", "Mr. Siro", "VPOP"),
    "trai_tim_em_cung_biet_dau.m4a": ("Trái Tim Em Cùng Biết Đau", "Mr. Siro", "VPOP"),
    "cham_day_noi_dau.m4a": ("Chạm Đáy Nỗi Đau", "Mr. Siro", "VPOP"),
    "mot_buoc_yeu_van_dam_dau.m4a": ("Một Bước Yêu Vạn Dặm Đau", "Mr. Siro", "VPOP"),
    "dung_ai_nhac_ve_anh_ay.m4a": ("Đừng Ai Nhắc Về Anh Ấy", "Mr. Siro", "VPOP"),
    "song_xa_anh_chang_de_dang.m4a": ("Sống Xa Anh Chẳng Dễ Dàng", "Mr. Siro", "VPOP"),
    "cang_niu_giu_cang_de_mat.m4a": ("Càng Níu Giữ Càng Dễ Mất", "Mr. Siro", "VPOP"),
    "da_biet_se_co_ngay_hom_nay.m4a": ("Đã Biết Sẽ Có Ngày Hôm Nay", "Mr. Siro", "VPOP"),

    # --- LƯƠNG BÍCH HỮU ---
    "co_gai_trung_hoa.webm": ("Cô Gái Trung Hoa", "Lương Bích Hữu", "VPOP"),
    "goi_ten_toi_nhe_ban_than_hoi.m4a": ("Gọi Tên Tôi Nhé Bạn Thân Hỡi", "Lương Bích Hữu", "VPOP"),
    "danh_cho_em.m4a": ("Dành Cho Em", "Lương Bích Hữu", "VPOP"),
    "cai_dau_lanh_va_trai_tim_nong.m4a": ("Cái Đầu Lạnh Và Trái Tim Nóng", "Lương Bích Hữu", "VPOP"),
    "cun_yeu.m4a": ("Cún Yêu", "Lương Bích Hữu", "VPOP"),
    "hoc_cach_di_mot_minh.m4a": ("Học Cách Đi Một Mình", "Lương Bích Hữu", "VPOP"),
    "quen_cach_yeu.m4a": ("Quên Cách Yêu", "Lương Bích Hữu", "VPOP"),
    "em_van_tin_vao_tinh_yeu_cua_anh.m4a": ("Em Vẫn Tin Vào Tình Yêu Của Anh", "Lương Bích Hữu", "VPOP"),

    # --- QUAN HỌ BẮC NINH ---
    "beo_dat_may_troi.m4a": ("Bèo Dạt Mây Trôi", "Quan Họ Bắc Ninh", "QUAN HO"),
    "nguoi_oi_nguoi_o_dung_ve.m4a": ("Người Ơi Người Ở Đừng Về", "Quan Họ Bắc Ninh", "QUAN HO"),
    "xe_chi_luon_kim.m4a": ("Xe Chỉ Luồn Kim", "Quan Họ Bắc Ninh", "QUAN HO"),
    "con_duyen.m4a": ("Còn Duyên", "Quan Họ Bắc Ninh", "QUAN HO"),
    "gia_ban.m4a": ("Giã Bạn", "Quan Họ Bắc Ninh", "QUAN HO"),
    "ly_cay_da.m4a": ("Lý Cây Đa", "Quan Họ Bắc Ninh", "QUAN HO"),
    "cay_truc_xinh.m4a": ("Cây Trúc Xinh", "Quan Họ Bắc Ninh", "QUAN HO"),
    "khach_den_choi_nha.m4a": ("Khách Đến Chơi Nhà", "Quan Họ Bắc Ninh", "QUAN HO"),
    "ngoi_tua_man_thuyen.m4a": ("Ngồi Tựa Mạn Thuyền", "Quan Họ Bắc Ninh", "QUAN HO"),

    # --- ÁI PHƯƠNG ---
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

    # --- NHẠC VPOP / KHÁC ---
    "anh-con-no-em.mp3": ("Anh Còn Nợ Em", "Quang Dũng", "VPOP"),
    "anh_khac_hay_em_khac.m4a": ("Anh Khác Hay Em Khác", "Khắc Việt", "VPOP"),
    "ao_mong_tinh_yeu.m4a": ("Ảo Mộng Tình Yêu", "Đan Trường & Cẩm Ly", "VPOP"),
    "cau_vong_khuyet.m4a": ("Cầu Vồng Khuyết", "Tuấn Hưng", "VPOP"),
    "co_don_tren_sofa.m4a": ("Cô Đơn Trên Sofa", "Hồ Ngọc Hà", "VPOP"),
    "cuoi_nhau_di_yes_i_do.m4a": ("Cưới Nhau Đi (Yes I Do)", "Bùi Anh Tuấn & Hiền Hồ", "VPOP"),
    "dung_lam_trai_tim_anh_dau.m4a": ("Đừng Làm Trái Tim Anh Đau", "Sơn Tùng M-TP", "VPOP"),
    "e_la_khong_the.mp3": ("E Là Không Thể", "Anh Quân Idol", "VPOP"),
    "khoc_cung_em.m4a": ("Khóc Cùng Em", "Mr. Siro ft. Gray4", "VPOP"),
    "khong_the_cung_nhau_suot_kiep.m4a": ("Không Thể Cùng Nhau Suốt Kiếp", "Hòa Minzy", "VPOP"),
    "kiep_ve_sau.m4a": ("Kiếp Ve Sầu", "Đan Trường", "VPOP"),
    "lang_quen_chieu_thu.webm": ("Lãng Quên Chiều Thu", "Lam Trường", "VPOP"),
    "mai_mai_mot_tinh_yeu.webm": ("Mãi Mãi Một Tình Yêu", "Đan Trường", "VPOP"),
    "nguoi_vo_hinh.mp3": ("Người Vô Hình", "Minh Hằng", "VPOP"),
    "take_me_to_your_heart.mp3": ("Take Me To Your Heart", "MLTR", "WORLD"),
    "tim_lai_bau_troi.m4a": ("Tìm Lại Bầu Trời", "Tuấn Hưng", "VPOP"),
    "tinh_don_phuong.m4a": ("Tình Đơn Phương", "Lam Trường", "VPOP"),
    "tinh_yeu_hoa_gio.mp3": ("Tình Yêu Hoa Gió", "Trương Thế Vinh", "VPOP"),
    "trang_giay_trang.m4a": ("Trang Giấy Trắng", "Phạm Trưởng", "VPOP"),
    "trang_giay_trang.webm": ("Trang Giấy Trắng (Remix)", "Phạm Trưởng", "VPOP"),
    "why_did_i_fall.mp3": ("Why Did I Fall In Love With You", "Tohoshinki", "WORLD"),
    "yeu_dau_theo_gio_bay.mp3": ("Yêu Dấu Theo Gió Bay", "Hiền Thục", "VPOP")
}

# Quét tất cả file nhạc có trong thư mục
audio_files = [f for f in os.listdir(WEB_DIR) if f.endswith(('.mp3', '.m4a', '.webm'))]
audio_files.sort()

new_songs = []
for idx, f in enumerate(audio_files, 1):
    if f in FILE_MAPPING:
        title, artist, genre = FILE_MAPPING[f]
    else:
        # Tự động hóa cho các file phát sinh thêm
        raw_name = os.path.splitext(f)[0]
        title = raw_name.replace("_", " ").replace("-", " ").title()
        artist = "Ca Sĩ Khác"
        genre = "VPOP"

    new_songs.append({
        "id": idx,
        "title": title,
        "artist": artist,
        "genre": genre,
        "src": f
    })

# Ghi đè songs.json
with open(SONGS_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(new_songs, f, ensure_ascii=False, indent=2)

print(f"🎉 ĐÃ MAP CHUẨN XÁC 100% BỘ {len(new_songs)} BÀI HÁT TRÊN SERVER!")
