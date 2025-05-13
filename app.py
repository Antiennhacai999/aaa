import time

def analyze_hex_ma_phien(hex_ma_phien):
    """Phân tích chuỗi HEX 32 ký tự để dự đoán Tài/Xỉu"""
    try:
        digits = [int(ch, 16) for ch in hex_ma_phien.lower()]  # Chuyển mỗi ký tự hex sang số (0–15)
    except ValueError:
        return None, None, None, None, "Mã HEX không hợp lệ!"

    if len(digits) != 32:
        return None, None, None, None, "Mã HEX phải đúng 32 ký tự!"

    checksum = sum(digits)
    even_count = sum(1 for d in digits if d % 2 == 0)
    odd_count = 32 - even_count
    sum_first_half = sum(digits[:16])
    sum_second_half = sum(digits[16:])
    last_digit = digits[-1]
    high_digits = sum(1 for d in digits[-4:] if d > 8)

    # Chấm điểm nghiêng Tài/Xỉu
    score_tai = 0
    score_xiu = 0

    if checksum > 240: score_tai += 20
    else: score_xiu += 20

    if sum_second_half > sum_first_half: score_tai += 20
    else: score_xiu += 20

    if even_count > odd_count: score_tai += 20
    else: score_xiu += 20

    if high_digits >= 3: score_tai += 15
    else: score_xiu += 15

    if last_digit % 2 == 0: score_tai += 25
    else: score_xiu += 25

    total_score = score_tai + score_xiu
    probability_tai = score_tai / total_score
    probability_xiu = score_xiu / total_score
    du_doan = "Tài" if probability_tai >= 0.5 else "Xỉu"

    do_tin_cay = abs(probability_tai - probability_xiu)
    confidence = "CAO" if do_tin_cay >= 0.3 else "TRUNG BÌNH" if do_tin_cay >= 0.15 else "THẤP"

    return probability_tai, probability_xiu, du_doan, confidence, None

def main():
    print("🎮 TOOL DỰ ĐOÁN TÀI/XỈU - PHIÊN BẢN HEX 🎮")
    print("=========================================")

    while True:
        hex_ma_phien = input("🔷 Nhập mã phiên HEX (32 ký tự): ").strip()

        if hex_ma_phien.lower() == "out":
            print("🚪 Kết thúc chương trình.")
            break

        print("⏳ Đang phân tích, vui lòng đợi...")
        time.sleep(1.5)

        prob_tai, prob_xiu, du_doan, confidence, err = analyze_hex_ma_phien(hex_ma_phien)

        if err:
            print(f"❌ Lỗi: {err}")
            continue

        # Hiển thị kết quả
        print("\n📊 KẾT QUẢ DỰ ĐOÁN 📊")
        print("─────────────────────────────")
        print(f"🔢 Tỷ Lệ Tài  : {prob_tai * 100:.2f}%")
        print(f"🔢 Tỷ Lệ Xỉu  : {prob_xiu * 100:.2f}%")
        print(f"💰 Dự Đoán    : {'🔴 TÀI' if du_doan == 'Tài' else '🔵 XỈU'}")
        print(f"✅ Độ Tin Cậy : {confidence}")
        print("─────────────────────────────")

        # Nhập kết quả thực tế
        result = input("📢 Nhập kết quả thực tế (T/X): ").strip().upper()
        if result in ["T", "X"]:
            print("✅ Đã lưu kết quả.")
        else:
            print("⚠️ Không xác định kết quả, bỏ qua.")

if name == "__main__":
    main()
