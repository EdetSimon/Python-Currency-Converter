import customtkinter as ctk
from currency_api import convert_currency


ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

def run_app():

    def convert():
        try:
            amount = float(amount_entry.get())

        except ValueError:
            result_label.configure(text="Invalid Amount")
            return

        from_code = from_currency.get().split(" - ")[0]
        to_code = to_currency.get().split(" - ")[0]

        result = convert_currency(amount, from_code, to_code)

        if result is None:
            exchange_rate_label.configure(text="Unable to fetch exchange rate")

            result_label.configure(text="Invalid Amount")
            return

        exchange_rate_label.configure(text=f"1 {from_code} = {result['rate']:,.4f} {to_code}")

        result_label.configure(text=f"{result['converted']:,.2f} {to_code}")

    def swap_currency():
        first = from_currency.get()
        second = to_currency.get()

        from_currency.set(second)
        to_currency.set(first)

    root = ctk.CTk()

    root.title("Currency Converter")
    root.geometry("600x800")
    root.resizable(False, False)

    title = ctk.CTkLabel(root, text="💱 Currency Converter", font=("Segoe UI", 32, "bold"))
    title.pack(pady=(30, 10))

    subtitle = ctk.CTkLabel(root, text="Fast • Accurate • Real-Time", font=("Segoe UI", 15))
    subtitle.pack(pady=(0, 25))

    main_frame = ctk.CTkFrame(root, width=470, height=700, corner_radius=20)
    main_frame.pack(pady=15)
    main_frame.pack_propagate(False)

    amount_label = ctk.CTkLabel(main_frame, text="Amount", font=("Segoe UI", 18, "bold"))
    amount_label.pack(anchor="w", padx=25, pady=(25, 5))

    amount_entry = ctk.CTkEntry(main_frame, width=400, height=45, corner_radius=15, font=("Segoe UI", 18), placeholder_text="Enter Amount")
    amount_entry.pack(pady=(0, 20))

    from_label = ctk.CTkLabel(main_frame, text="From", font=("Segoe UI", 18, "bold"))
    from_label.pack(anchor="w", padx=25, pady=(5, 5))

    currencies = [
        "USD - US Dollar",
        "EUR - Euro",
        "GBP - GREAT BRITISH POUND",
        "NGN - Nigerian Naira",
        "JPY - Japanese Yen",
        "CAD - Canadian Dollar",
        "AUD - Australian Dollar",
        "CHF - Swiss Franc",
    ]

    from_currency = ctk.CTkComboBox(main_frame, values=currencies, width=420, height=45, corner_radius=15, font=("Segoe UI", 16))
    from_currency.pack()
    from_currency.set("USD - US Dollar")

    swap_button = ctk.CTkButton(main_frame, text="⇅", width=60, height=60, corner_radius=30, font=("Segoe UI", 24),command=swap_currency)
    swap_button.pack(pady=18)

    to_label = ctk.CTkLabel(main_frame, text="To", font=("Segoe UI", 18, "bold"))
    to_label.pack(anchor="w", padx=25, pady=(20, 5))

    to_currency = ctk.CTkComboBox(main_frame, values=currencies, width=420, height=45, corner_radius=15, font=("Segoe UI", 16))
    to_currency.pack()
    to_currency.set("NGN - Nigerian Naira")

    convert_button = ctk.CTkButton(main_frame, text="Convert", width=300, height=50, corner_radius=25, command=convert, font=("Segoe UI", 18, "bold"), fg_color="#10B981", hover_color="#059669")
    convert_button.pack(pady=(10, 15))

    exchange_frame = ctk.CTkFrame(main_frame, width=400, height=65, corner_radius=15)
    exchange_frame.pack(pady=(8, 12))
    exchange_frame.pack_propagate(False)

    exchange_title = ctk.CTkLabel(exchange_frame, text="Live Exchange Rate", font=("Segoe UI", 13, "bold"))
    exchange_title.pack(pady=(6, 0))

    exchange_rate_label = ctk.CTkLabel(exchange_frame, text="1 USD = ₦0.00", font=("Segoe UI", 18, "bold"))
    exchange_rate_label.pack()

    result_frame = ctk.CTkFrame(main_frame, width=400, height=85, corner_radius=15)
    result_frame.pack()
    result_frame.pack_propagate(False)

    result_title = ctk.CTkLabel(result_frame, text="Converted Amount", font=("Segoe UI", 13, "bold"))
    result_title.pack(pady=(6, 0))

    result_label = ctk.CTkLabel(result_frame, text="₦0.00", font=("Segoe UI", 24, "bold"))
    result_label.pack()














































    root.mainloop()