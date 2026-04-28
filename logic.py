import re

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 25
    else:
        feedback.append("Password çox qısadır (min 8 simvol)")

    if re.search(r"[A-Z]", password):
        score += 20
    else:
        feedback.append("Böyük hərf əlavə et")

    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Kiçik hərf əlavə et")

    if re.search(r"[0-9]", password):
        score += 20
    else:
        feedback.append("Rəqəm əlavə et")

    if re.search(r"[!@#$%^&*]", password):
        score += 20
    else:
        feedback.append("Simvol (!@#$%) əlavə et")

    if password.lower() in ["123456", "admin", "password"]:
        score = 0
        feedback.append("Bu password HACKED siyahısındadır!")

    if score >= 80:
        strength = "STRONG"
    elif score >= 50:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
  }
