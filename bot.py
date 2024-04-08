import random
import json

# Membuka file yang menyimpan data belajar
try:
    with open("learned_responses.json", "r") as file:
        learned_responses = json.load(file)
except FileNotFoundError:
    learned_responses = {}

def save_learned_responses():
    with open("learned_responses.json", "w") as file:
        json.dump(learned_responses, file)

def chat():
    print("Selamat datang di chatbox sederhana. Ketik 'exit' untuk keluar.")
    while True:
        user_input = input("Anda: ").lower()  # Mengambil input dari pengguna dan mengonversinya menjadi huruf kecil
        if user_input == "exit":
            print("Chatbox ditutup.")
            save_learned_responses()
            break

        # Mencari respons yang sesuai
        if user_input in learned_responses:
            response = learned_responses[user_input]
        else:
            response = learned_responses.get(user_input, ["default"])

        # Jika respons tidak ditemukan, bot akan belajar dari pengguna
        if response == ["default"]:
            print("Chatbot: Maaf, saya tidak tahu jawabannya. Bisakah kamu mengajari saya? Jawabannya adalah:")
            new_response = input("Anda: ")
            learned_responses[user_input] = [new_response]
            print("Chatbot: Terima kasih! Saya akan mengingatnya.")
        else:
            print("Chatbot:", random.choice(response))  # Memilih respons secara acak dari daftar respons yang sesuai

if __name__ == "__main__":
    # Menambahkan beberapa kata ke dalam kamus respons
    learned_responses.update({
        "halo": ["Halo!", "Hai!", "Ada yang bisa saya bantu?"],
        "apa kabar?": ["Saya baik, terima kasih.", "Baik, terima kasih. Bagaimana dengan Anda?"],
        "siapa kamu?": ["Saya adalah chatbot sederhana.", "Saya adalah program komputer yang dibuat untuk berinteraksi dengan Anda."]
    })

    chat()

