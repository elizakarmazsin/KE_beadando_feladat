class KE_DataHelper:

    def __init__(self, prefix="KE_"):
        self.prefix = prefix
        print(f"KE_DataHelper inicializálva, előtag: {self.prefix}")

    def format_for_display(self, data):

        return f"{self.prefix} {data}"

def ke_format_text(input_text):
    if not input_text:
        return "Nincs megadott szöveg."

    return ", ".join(list(input_text.upper()))

if __name__ == "__main__":
    helper = KE_DataHelper()
    print(helper.format_for_display("Erős jelszó."))
    print(ke_format_text("monogram"))