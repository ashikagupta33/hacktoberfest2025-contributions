from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

def create_resume(data):
    c = canvas.Canvas("resume.pdf", pagesize=LETTER)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, 750, data["name"])
    c.setFont("Helvetica", 12)
    c.drawString(50, 730, f"Email: {data['email']} | Phone: {data['phone']}")
    
    c.drawString(50, 700, "Skills:")
    for i, skill in enumerate(data["skills"]):
        c.drawString(70, 680 - (i * 15), f"- {skill}")

    c.drawString(50, 600, "Experience:")
    for i, job in enumerate(data["experience"]):
        c.drawString(70, 580 - (i * 40), f"{job['position']} at {job['company']}")
        c.drawString(70, 565 - (i * 40), f"{job['years']}")

    c.save()
    print("Resume generated: resume.pdf")

if __name__ == "__main__":
    user_data = {
        "name": input("Full Name: "),
        "email": input("Email: "),
        "phone": input("Phone: "),
        "skills": input("Skills (comma separated): ").split(","),
        "experience": [
            {
                "position": input("Last Job Title: "),
                "company": input("Company: "),
                "years": input("Years (e.g. 2021-2023): ")
            }
        ]
    }
    create_resume(user_data)
