# Cryptography Basics

## Introduction to Cryptography

Cryptography is the practice and study of techniques for secure communication in the presence of adversaries. It's a fundamental component of PKI and modern information security.

## Symmetric vs. Asymmetric Encryption

### Symmetric Encryption
- Uses a single key for both encryption and decryption
- Generally faster than asymmetric encryption
- Examples: AES, DES

### Asymmetric Encryption
- Uses a pair of keys: public key for encryption, private key for decryption
- More computationally intensive but solves key distribution problem
- Examples: RSA, ECC

## Hash Functions

- One-way functions that produce a fixed-size output from variable-size input
- Properties: deterministic, quick to compute, infeasible to reverse
- Used for integrity checking and password storage
- Examples: SHA-256, MD5 (now considered insecure)

## Digital Signatures

- Combine asymmetric encryption and hash functions
- Provide authentication, non-repudiation, and integrity
- Process: hash the message, encrypt the hash with private key

Understanding these cryptographic primitives is crucial for grasping how PKI functions and provides security.