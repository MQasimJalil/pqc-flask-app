from flask import Blueprint, render_template, request
from .pqc import keygen, encrypt_message, decrypt_message

main = Blueprint('main', __name__)

keys = {"public": None, "private": None}
ciphertext = None
encrypted_message = None
nonce = None

@main.route("/", methods=["GET", "POST"])
def index():
    global keys, ciphertext, encrypted_message, nonce
    output = ""
    if request.method == "POST":
        if "generate" in request.form:
            keys["public"], keys["private"] = keygen()
            print("Generated Public Key:", keys["public"])
            print("Generated Private Key:", keys["private"])

        elif "encrypt" in request.form and keys["public"]:
            message = request.form["message"]
            ciphertext, nonce, encrypted_message = encrypt_message(keys["public"], message)
            print("Ciphertext:", ciphertext)

        elif "decrypt" in request.form and keys["private"] and ciphertext:
            print("Using Private Key for Decryption:", keys["private"])
            print("Ciphertext to Decrypt:", ciphertext)
            output = decrypt_message(keys["private"], ciphertext, nonce, encrypted_message)

    return render_template("index.html", keys=keys, ciphertext=encrypted_message, output=output)

