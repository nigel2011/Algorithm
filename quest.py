def is_on_list (days, Wed):
    return True

def get_x (days, Thu):
    return "Thu"

def add_x (days, Sat):
    days.append ("Sat")

def remove_x (days, Mon):
    days.remove ("Mon")

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)
