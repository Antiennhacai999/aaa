def analyze_hex_ma_phien(hex_ma_phien):
    """Phân tích chuỗi HEX để dự đoán Tài/Xỉu"""
    try:
        digits = [int(ch, 16) for ch in hex_ma_phien.lower()]
    except ValueError:
        return None, None, None, None, "Mã HEX không hợp lệ!"

    if len(digits) != 32:
        return None, None, None, None, "Mã HEX phải đúng 32 ký tự!"

    checksum = sum(digits)
    even_count = sum(1 for d in digits if d % 2 == 0)
    high_digits = sum(1 for d in digits if d > 9)
    last_digit = digits[-1]
    high_last4 = sum(1 for d in digits[-4:] if d > 12)

    # Hệ thống điểm cải tiến
    score_tai = 0
    score_xiu = 0

    if checksum > 280: score_tai += 30
    else: score_xiu += 30

    if high_digits >= 12: score_tai += 25
    else: score_xiu += 25

    if even_count > 16: score_tai += 15
    else: score_xiu += 15

    if high_last4 >= 2: score_tai += 20
    else: score_xiu += 20

    if last_digit % 2 == 0: score_tai += 10
    else: score_xiu += 10

    total_score = score_tai + score_xiu
    probability_tai = score_tai / total_score
    probability_xiu = score_xiu / total_score
    du_doan = "Tài" if probability_tai >= 0.5 else "Xỉu"

    do_tin_cay = abs(probability_tai - probability_xiu)
    confidence = "CAO" if do_tin_cay >= 0.3 else "TRUNG BÌNH" if do_tin_cay >= 0.15 else "THẤP"

    return probability_tai, probability_xiu, du_doan, confidence, None
