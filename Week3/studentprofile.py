def build_profile(name, **details):
    print("Student Name:", name)

    for key, value in details.items():
        print(key, ":", value)

build_profile(
    "Ayusha",
    Program="BSCS",
    Semester="Fourth",
    Portfolio="www.ayusha.com"
)