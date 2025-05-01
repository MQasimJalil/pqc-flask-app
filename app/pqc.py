from kyber_py.ml_kem import ML_KEM_512
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def keygen():
    public_key, private_key = ML_KEM_512.keygen()
    return public_key, private_key

def encrypt_message(public_key: bytes, message: str):
    # Step 1: PQC encapsulation
    shared_secret, ciphertext = ML_KEM_512.encaps(public_key)

    # Step 2: Symmetric encryption (AES-GCM)
    aesgcm = AESGCM(shared_secret[:32])  # AES-256
    nonce = os.urandom(12)
    encrypted_message = aesgcm.encrypt(nonce, message.encode(), None)

    return ciphertext, nonce, encrypted_message

def decrypt_message(private_key: bytes, ciphertext: bytes, nonce: bytes, encrypted_message: bytes):
    # Step 1: PQC decapsulation
    shared_secret = ML_KEM_512.decaps(private_key, ciphertext)

    # Step 2: Symmetric decryption
    aesgcm = AESGCM(shared_secret[:32])
    decrypted_message = aesgcm.decrypt(nonce, encrypted_message, None)

    return decrypted_message.decode()