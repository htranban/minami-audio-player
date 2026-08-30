import os
import json

WEB_DIR = "/var/www/html"
SONGS_JSON_PATH = os.path.join(WEB_DIR, "songs.json")

# Danh sách từ khóa nhận diện các ca sĩ khác
KHOI_MY_KEYWORDS = ["gui_cho_anh", "vi_sao", "goc_nho_trong_tim", "khoc_dem", "hat_cat", "thuong_anh", "neu_nho_nam_xua", "nguoi_yeu_cu", "de_thuong", "xe_dap_teen", "khoi_my"]
MY_TAM_KEYWORDS = ["uoc_gi", "duong_nhu_ta_da", "hoa_mi_toc_nau", "cay_dan_sinh_vien", "toc_nau_moi_tram", "chuyen_nhu_chua_bat_dau", "dung_hoi_em", "nguoi_hay_quen_em_di", "noi_minh_dung_chan", "don_coi", "hat_voi_dong_song", "my_tam"]
MR_SIRO_KEYWORDS = ["lang_nghe_nuoc_mat", "buc_tranh_tu_nuoc_mat", "em_gai_mua", "trai_tim_em_cung_biet_dau", "cham_day_noi_dau", "mot_buoc_yeu_van_dam_dau", "dung_ai_nhac_ve_anh_ay", "song_xa_anh", "yeu_mot_nguoi_co_le", "tim_lai_bau_troi", "guong_mat_ta_loi", "duoi_mua", "cang_niu_giu", "khoc_cung_em", "khong_the_cung_nhau", "tu_lau_nuoc_mat", "co_don_tren_sofa", "mr_siro", "siro"]
LUONG_BICH_HUU_KEYWORDS = ["co_gai_trung_hoa", "goi_ten_toi", "danh_cho_em", "cai_dau_lanh", "cun_yeu", "hoc_cach_di_mot_minh", "quen_cach_yeu", "nuoc_mat_hoa_da", "dem_trang", "xem_nhu_em_chang_may", "gap_lai_nhau_lam_gi", "em_van_tin", "luong_bich_huu"]
BIGBANG_KEYWORDS = ["haruharu", "bang_bang_bang", "fantastic_baby", "loser", "blue", "bad_boy", "if_you", "fxxk_it", "bae_bae", "lies", "lets_not_fall_in_love", "bigbang"]
QUAN_HO_KEYWORDS = ["beo_dat_may_troi", "nguoi_oi_nguoi_o", "xe_chi_luon_kim", "con_duyen", "gia_ban", "ly_cay_da", "ngoi_tua_man_thuyen", "khach_den_choi_nha", "cay_truc_xinh", "muoi_nho"]

TITLE_CLEAN_MAP = {
    "toi_thay_hoa_vang_tren_co_xanh": "Tôi Thấy Hoa Vàng Trên Cỏ Xanh",
    "dong_tay_nam_bac": "Đông Tây Nam Bắc",
    "tro_troi": "Trô Trọi",
    "co_don": "Cô Đơn",
    "duong_ve_nha": "Đường Về Nhà",
    "den_voi_nhau_la_do_duyen": "Đến Với Nhau Là Do Duyên",
    "chia_tay_trong_mua": "Chia Tay Trong Mưa",
    "nhung_ngay_me_vang_nha": "Những Ngày Mẹ Vắng Nhà",
    "hua_voi_em": "Hứa Với Em",
    "loi_ru_cho_con": "Lời Ru Cho Con",
    "dung_im": "Đứng Im",
    "neu_anh_yeu_em": "Nếu Anh Yêu Em",
    "khi_me_vang_nha": "Khi Mẹ Vắng Nhà",
    "nam_lay_tay_anh": "Nắm Lấy Tay Anh",
    "giot_nuoc_mat_cho_doi": "Giọt Nước Mắt Cho Đời",
    "co_phai_em_la_mua_thu_ha_noi": "Có Phải Em Là Mùa Thu Hà Nội",
    "nhong_nhang": "Nhõng Nhẽo",
    "tinh_yeu_trai_qua": "Tình Yêu Trải Qua",
    "giac_mo_ngay_tho": "Giấc Mơ Ngây Thơ",
    "nguyen_cau": "Nguyện Cầu"
}

def detect_info(filename):
    fname = filename.lower()
    genre = "VPOP"
    
    # Đổi mặc định thành Ái Phương thay vì Ca Sĩ Khác
    artist = "Ái Phương"
    
    raw_name = os.path.splitext(filename)[0]
    title = TITLE_CLEAN_MAP.get(raw_name, raw_name.replace("_", " ").title())
    
    # Phân loại ca sĩ khác nếu trúng từ khóa
    if any(k in fname for k in KHOI_MY_KEYWORDS):
        artist = "Khởi My"
    elif any(k in fname for k in MY_TAM_KEYWORDS):
        artist = "Mỹ Tâm"
    elif any(k in fname for k in MR_SIRO_KEYWORDS):
        artist = "Mr. Siro"
    elif any(k in fname for k in LUONG_BICH_HUU_KEYWORDS):
        artist = "Lương Bích Hữu"
    elif any(k in fname for k in BIGBANG_KEYWORDS):
        artist = "BIGBANG"
        genre = "KPOP"
    elif any(k in fname for k in QUAN_HO_KEYWORDS):
        artist = "Quan Họ Bắc Ninh"
        genre = "QUAN HO"
        
    return title, artist, genre

audio_files = [f for f in os.listdir(WEB_DIR) if f.endswith(('.mp3', '.m4a', '.webm'))]
audio_files.sort()

new_songs = []
for idx, f in enumerate(audio_files, 1):
    title, artist, genre = detect_info(f)
    new_songs.append({
        "id": idx,
        "title": title,
        "artist": artist,
        "genre": genre,
        "src": f
    })

with open(SONGS_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(new_songs, f, ensure_ascii=False, indent=2)

print(f"✅ Đã xóa sạch 'Ca Sĩ Khác' và gán hết thành 'Ái Phương'!")
