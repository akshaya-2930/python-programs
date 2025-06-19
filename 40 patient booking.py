from datetime import datetime, timedelta

# Sample doctor database
doctors = {
    "Dr. Mehta": ["09:00", "11:00", "15:00"],
    "Dr. Kapoor": ["10:00", "13:00", "16:00"]
}

appointments = {}

def display_slots():
    print("\n📅 Available Time Slots:")
    for doc, slots in doctors.items():
        print(f"{doc}: {', '.join(slots)}")

def book_appointment(patient, doctor, time):
    if doctor not in doctors or time not in doctors[doctor]:
        print("❌ Invalid doctor or time.")
        return
    key = f"{patient}_{doctor}_{time}"
    appointments[key] = {
        "patient": patient,
        "doctor": doctor,
        "time": time,
        "reminder_sent": False
    }
    doctors[doctor].remove(time)
    print(f"✅ Appointment booked with {doctor} at {time} for {patient}")

def cancel_appointment(key):
    if key in appointments:
        data = appointments.pop(key)
        doctors[data["doctor"]].append(data["time"])
        print(f"🗑️ Appointment cancelled for {data['patient']}")
    else:
        print("❌ Appointment not found.")

def modify_appointment(key, new_time):
    if key not in appointments:
        print("❌ Appointment not found.")
        return
    data = appointments[key]
    doctor = data["doctor"]
    if new_time not in doctors[doctor]:
        print("❌ New time not available.")
        return
    doctors[doctor].append(data["time"])
    doctors[doctor].remove(new_time)
    data["time"] = new_time
    print(f"✏️ Appointment updated to {new_time}")

def send_reminders():
    print("\n🔔 Reminders:")
    for key, appt in appointments.items():
        if not appt["reminder_sent"]:
            print(f"Reminder: {appt['patient']}, appointment with {appt['doctor']} at {appt['time']}")
            appt["reminder_sent"] = True

# Example demo
display_slots()
book_appointment("Aarav", "Dr. Mehta", "09:00")
book_appointment("Sanya", "Dr. Kapoor", "13:00")
send_reminders()
modify_appointment("Sanya_Dr. Kapoor_13:00", "16:00")
cancel_appointment("Aarav_Dr. Mehta_09:00")
