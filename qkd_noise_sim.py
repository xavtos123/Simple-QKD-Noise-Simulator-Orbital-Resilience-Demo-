# Simple QKD Noise Simulator - Like a radio game in space where static messes up secret messages!
# QKD is a way to share super-secret keys using light particles (photons). But in space, noise (like sun static) can 'hear' it.
# This tool pretends to send keys, adds noise, and fixes it with error correction—like your dissertation on stable QKD.

import random  # Dice for noise and keys.

def generate_qkd_key(length=8):
    # Make a secret key: Random 0s and 1s, like flipping coins for a binary code.
    key = [random.choice([0, 1]) for _ in range(length)]
    return key

def add_noise(key, noise_rate=0.2):
    # Add 'static' (noise): Flip some bits with chance (20% = vauge like space noise).
    noisy_key = key.copy()
    for i in range(len(key)):
        if random.random() < noise_rate:  # If dice roll < 0.2, flip the bit.
            noisy_key[i] = 1 - key[i]  # Flip 0 to 1, 1 to 0.
    return noisy_key

def correct_errors(noisy_key, original_key):
    # Fix static: Compare to original, flip back wrong bits (error correction).
    corrected = noisy_key.copy()
    errors_fixed = 0
    for i in range(len(noisy_key)):
        if noisy_key[i] != original_key[i]:
            corrected[i] = original_key[i]  # Flip back.
            errors_fixed += 1
    return corrected, errors_fixed

# Pretend space key share.
original_key = generate_qkd_key()
noisy = add_noise(original_key)
corrected, fixed = correct_errors(noisy, original_key)

print("Original Secret Key (from Earth to Satellite):", original_key)
print("Noisy Key (After Space Static):", noisy)
print("Fixed Key (Error Correction Magic):", corrected)
print(f"Fixed {fixed} bad bits! Like making QKD work in noisy space (your dissertation style).")
# Tip: Run multiple times to see more/less noise!
