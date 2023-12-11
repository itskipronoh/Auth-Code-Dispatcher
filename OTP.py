from tkinter import *
from tkinter import messagebox
from twilio.rest import Client
import smtplib
import random

otp = random.randint(1000, 9999)
otp = str(otp)
print("Your OTP is", otp)

root = Tk()
root.title("Send OTP Via Email")
root.geometry("565x450")
email_label = Label(root, text="Enter receiver's Email: ", font="ariel 15 bold", relief=FLAT)
email_label.grid(row=0, column=0, padx=15, pady=60)
email_entry = Entry(root, font="ariel 15 bold", width=25, relief=GROOVE, bd=2)
email_entry.grid(row=0, column=1, padx=12, pady=60)
email_entry.focus()

def Email():
    try:
        s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
        s.starttls()
        sender_email = "pythonproject24@gmail.com"  # Updated sender email
        sender_password = "myzxaqasdfzwpdzy"  # Replace with your sender email password
        s.login(sender_email, sender_password)
        s.sendmail(sender_email, email_entry.get(), otp)
        messagebox.showinfo("Send OTP via Email", f"OTP sent to {email_entry.get()}")
        s.quit()
    except:
        messagebox.showinfo("Send OTP via Email", "Please enter a valid email address or check an internet connection")

send_button = Button(root, text="Send Email", font="ariel 15 bold", bg="black", fg="green2", bd=3, command=Email)
send_button.place(x=210, y=150)
root.mainloop()

Mo = Tk()
Mo.title("Send OTP on Mobile")
Mo.geometry("565x400")
Mobile_label = Label(Mo, text="Enter Mobile no: ", font="ariel 15 bold", relief=FLAT)
Mobile_label.grid(row=0, column=0, padx=15, pady=60)
Mobile_entry = Entry(Mo, font="ariel 15 bold", width=25, relief=GROOVE, bd=2)
Mobile_entry.grid(row=0, column=1, padx=12, pady=60)
Mobile_entry.focus()

def sms():
    account_sid = 'AC22b53a3424a9d71cb59499f27e678c73'
    auth_token = '5904bcb8827458785ec00216099d7011' 
    client = Client(account_sid, auth_token)

    # Check if the mobile number starts with +254
    mobile_number = Mobile_entry.get()
    if mobile_number.startswith("+254") and len(mobile_number) == 13:
        message = client.messages.create(
            body='Hello Your Secure Device OTP is - ' + str(otp),
            from_='+254782606380',  # Replace with your Twilio number
            to=mobile_number
        )
        messagebox.showinfo("Send OTP via SMS", f"OTP sent to {mobile_number}")
    else:
        messagebox.showinfo("Send OTP via SMS", "Please enter a valid Kenyan mobile number starting with +254.")

Mob_button = Button(Mo, text="Send SMS", font="ariel 15 bold", bg="black", fg="green2", bd=3, command=sms)
Mob_button.place(x=210, y=150)
Mo.mainloop()
