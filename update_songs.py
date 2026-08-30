import os
import json

WEB_DIR = "/var/www/html"
SONGS_JSON_PATH = os.path.join(WEB_DIR, "songs.json")

# Danh sách từ khóa tên bài hát -> Tên bài hiển thị & Ca sĩ
TITLE_MAP = {
    # Ái Phương
    "toi_thay_hoa_vang": ("Tôi Thấy Hoa Vàng Trên Cỏ Xanh", "Ái Phương", "VPOP"),
    "dong_tay_nam_bac": ("Đông Tây Nam Bắc", "Ái Phương", "VPOP"),
    "tro_troi": ("Trô Trọi", "Ái Phương", "VPOP"),
    "co_don": ("Cô Đơn", "Ái Phương", "VPOP"),
    "duong_ve_nha": ("Đường Về Nhà", "Ái Phương", "VPOP"),
    "den_voi_nhau_la_do_duyen": ("Đến Với Nhau Là Do Duyên", "Ái Phương", "VPOP"),
    "chia_tay_trong_mua": ("Chia Tay Trong Mưa", "Ái Phương", "VPOP"),
    "nhung_ngay_me_vang_nha": ("Những Ngày Mẹ Vắng Nhà", "Ái Phương", "VPOP"),
    "hua_voi_em": ("Hứa Với Em", "Ái Phương", "VPOP"),
    "loi_ru_cho_con": ("Lời Ru Cho Con", "Ái Phương", "VPOP"),
    "dung_im": ("Đứng Im", "Ái Phương", "VPOP"),
    "neu_anh_yeu_em": ("Nếu Anh Yêu Em", "Ái Phương", "VPOP"),
    "khi_me_vang_nha": ("Khi Mẹ Vắng Nhà", "Ái Phương", "VPOP"),
    "nam_lay_tay_anh": ("Nắm Lấy Tay Anh", "Ái Phương", "VPOP"),
    "giot_nuoc_mat_cho_doi": ("Giọt Nước Mắt Cho Đời", "Ái Phương", "VPOP"),
    "co_phai_em_la_mua_thu_ha_noi": ("Có Phải Em Là Mùa Thu Hà Nội", "Ái Phương", "VPOP"),
    "nhong_nhang": ("Nhõng Nhẽo", "Ái Phương", "VPOP"),
    "tinh_yeu_trai_qua": ("Tình Yêu Trải Qua", "Ái Phương", "VPOP"),
    "giac_mo_ngay_tho": ("Giấc Mơ Ngây Thơ", "Ái Phương", "VPOP"),
    "nguyen_cau": ("Nguyện Cầu", "Ái Phương", "VPOP"),

    # Khởi My
    "gui_cho_anh": ("Gửi Cho Anh", "Khởi My", "VPOP"),
    "vi_sao": ("Vì Sao", "Khởi My", "VPOP"),
    "goc_nho_trong_tim": ("Góc Nhỏ Trong Tim", "Khởi My", "VPOP"),
    "khoc_dem": ("Khóc Đêm", "Khởi My", "VPOP"),
    "hat_cat": ("Hạt Cát", "Khởi My", "VPOP"),
    "thuong_anh": ("Thương Anh", "Khởi My", "VPOP"),
    "neu_nho_nam_xua": ("Nếu Nhớ Năm Xưa", "Khởi My", "VPOP"),
    "nguoi_yeu_cu": ("Người Yêu Cũ", "Khởi My", "VPOP"),
    "de_thuong": ("Dễ Thương", "Khởi My", "VPOP"),
    "xe_dap_teen": ("Xe Đạp Teen", "Khởi My", "VPOP"),

    # Mỹ Tâm
    "my_tam": ("Mỹ Tâm Song", "Mỹ Tâm", "VPOP"),
    "uoc_gi": ("Ưóc Gì", "Mỹ Tâm", "VPOP"),
    "duong_nhu_ta_da": ("Dường Như Ta Đã", "Mỹ Tâm", "VPOP"),
    "hoa_mi_toc_nau": ("Họa Mi Tóc Nâu", "Mỹ Tâm", "VPOP"),
    "cay_dan_sinh_vien": ("Cây Đàn Sinh Viên", "Mỹ Tâm", "VPOP"),
    "toc_nau_moi_tram": ("Tóc Nâu Môi Trầm", "Mỹ Tâm", "VPOP"),
    "chuyen_nhu_chua_bat_dau": ("Chuyện Như Chưa Bắt Đầu", "Mỹ Tâm", "VPOP"),
    "dung_hoi_em": ("Đừng Hỏi Em", "Mỹ Tâm", "VPOP"),
    "nguoi_hay_quen_em_di": ("Người Hãy Quên Em Đi", "Mỹ Tâm", "VPOP"),

    # Mr. Siro
    "lang_nghe_nuoc_mat": ("Lắng Nghe Nước Mắt", "Mr. Siro", "VPOP"),
    "buc_tranh_tu_nuoc_mat": ("Bức Tranh Từ Nước Mắt", "Mr. Siro", "VPOP"),
    "em_gai_mua": ("Em Gái Mưa", "Mr. Siro", "VPOP"),
    "trai_tim_em_cung_biet_dau": ("Trái Tim Em Cùng Biết Đau", "Mr. Siro", "VPOP"),
    "cham_day_noi_dau": ("Chạm Đáy Nỗi Đau", "Mr. Siro", "VPOP"),
    "mot_buoc_yeu_van_dam_dau": ("Một Bước Yêu Vạn Dặm Đau", "Mr. Siro", "VPOP"),
    "dung_ai_nhac_ve_anh_ay": ("Đừng Ai Nhắc Về Anh Ấy", "Mr. Siro", "VPOP"),
    "song_xa_anh_chang_de_dang": ("Sống Xa Anh Chẳng Dễ Dàng", "Mr. Siro", "VPOP"),

    # BIGBANG
    "haruharu": ("Haru Haru", "BIGBANG", "KPOP"),
    "bang_bang_bang": ("BANG BANG BANG", "BIGBANG", "KPOP"),
    "fantastic_baby": ("Fantastic Baby", "BIGBANG", "KPOP"),
    "loser": ("Loser", "BIGBANG", "KPOP"),
    "blue": ("Blue", "BIGBANG", "KPOP"),
    "bad_boy": ("Bad Boy", "BIGBANG", "KPOP"),
    "if_you": ("If You", "BIGBANG", "KPOP"),
    "fxxk_it": ("Fxxk It", "BIGBANG", "KPOP"),

    # Lương Bích Hữu
    "em_yeu_anh": ("Em Yêu Anh", "Lương Bích Hữu", "VPOP"),
    "co_gai_trung_hoa": ("Cô Gái Trung Hoa", "Lương Bích Hữu", "VPOP"),
    "goi_ten_toi": ("Gọi Tên Tôi Nhé Bạn Thân Hỡi", "Lương Bích Hữu", "VPOP"),
    "cun_yeu": ("Cún Yêu", "Lương Bích Hữu", "VPOP"),
    "hoc_cach_di_mot_minh": ("Học Cách Đi Một Mình", "Lương Bích Hữu", "VPOP"),
    "quen_cach_yeu": ("Quên Cách Yêu", "Lương Bích Hữu", "VPOP"),

    # Quan Họ
    "beo_dat_may_troi": ("Bèo Dạt Mây Trôi", "Quan Họ Bắc Ninh", "QUAN HO"),
    "nguoi_oi_nguoi_o": ("Người Ôi Người Ở Đừng Về", "Quan Họ Bắc Ninh", "QUAN HO"),
    "xe_chi_luon_kim": ("Xe Chỉ Luồn Kim", "Quan Họ Bắc Ninh", "QUAN HO"),
    "con_duyen": ("Còn Duyên", "Quan Họ Bắc Ninh", "QUAN HO"),
    "gia_ban": ("Giã Bạn", "Quan Họ Bắc Ninh", "QUAN HO"),
    "ly_cay_da": ("Lý Cây Đa", "Quan Họ Bắc Ninh", "QUAN HO")
}

# Quét tất cả file nhạc
audio_files = [f for f in os.listdir(WEB_DIR) if f.endswith(('.mp3', '.m4a', '.webm'))]
audio_files.sort()

new_songs = []
for idx, f in enumerate(audio_files, 1):
    matched = False
    
    # 1. Quét từ khóa trong tên bài
    for key, (t, a, g) in TITLE_MAP.items():
        if key in f.lower():
            title, artist, genre = t, a, g
            matched = True
            break
            
    # 2. Nếu tên file chứa từ khóa ai_phuong / khoi_my / my_tam
    if not matched:
        if "ai_phuong" in f.lower() or "phuong" in f.lower():
            artist = "Ái Phương"
        elif "khoi_my" in f.lower():
            artist = "Khởi My"
        elif "my_tam" in f.lower():
            artist = "Mỹ Tâm"
        else:
            artist = "Ca Sĩ Khác"
            
        clean_name = os.path.splitext(f)[0].replace("_", " ").title()
        title = clean_name
        genre = "VPOP"

    new_songs.append({
        "id": idx,
        "title": title,
        "artist": artist,
        "genre": genre,
        "src": f
    })

# Lưu lại songs.json
with open(SONGS_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(new_songs, f, ensure_ascii=False, indent=2)

print(f"🎉 Đã cập nhật xong {len(new_songs)} bài hát! Ái Phương & các ca sĩ đã được khôi phục chuẩn xác!")
