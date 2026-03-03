from model import calculate_similarity

print("===== Resume Screening AI =====")

resume = input("\nPaste Resume Text:\n")
jd = input("\nPaste Job Description Text:\n")

score = calculate_similarity(resume, jd)

print(f"\nMatch Score: {score}%")

if score > 70:
    print("Strong Match ✅")
elif score > 40:
    print("Moderate Match ⚠️")
else:
    print("Low Match ❌")