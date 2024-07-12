# Cryptography Basics

## Introduction to Cryptography

Cryptography is the practice and study of techniques for secure communication in the presence of adversaries. It's a fundamental component of PKI and modern information security.

## Symmetric vs. Asymmetric Encryption

### Symmetric Encryption
- Uses a single key for both encryption and decryption
- Generally faster than asymmetric encryption
- Examples: 
  - AES (Advanced Encryption Standard)
  - DES (Data Encryption Standard)
  - 3DES (Triple DES)
  - Blowfish
  - Twofish

### Asymmetric Encryption
- Uses a pair of keys: public key for encryption, private key for decryption
- More computationally intensive but solves key distribution problem
- Examples: 
  - RSA (Rivest–Shamir–Adleman)
  - ECC (Elliptic Curve Cryptography)
  - DSA (Digital Signature Algorithm)

#### How Asymmetric Encryption Works
1. Each party generates a public-private key pair
2. Public keys are freely distributed
3. To send a secure message:
   - Sender encrypts the message with the recipient's public key
   - Only the recipient's private key can decrypt the message

## Hash Functions

- One-way functions that produce a fixed-size output from variable-size input
- Properties: 
  - Deterministic: same input always produces same output
  - Quick to compute
  - Infeasible to reverse
  - Small change in input changes output significantly
- Used for integrity checking and password storage
- Examples: 
  - SHA-256, SHA-3 (Secure Hash Algorithm family)
  - MD5 (Message Digest algorithm, now considered insecure)

## Digital Signatures

- Combine asymmetric encryption and hash functions
- Provide authentication, non-repudiation, and integrity
- Process: 
  1. Hash the message
  2. Encrypt the hash with the sender's private key
  3. Recipient decrypts the hash with sender's public key and compares with independently calculated hash

## Key Management Basics

Key management is crucial for maintaining the security of cryptographic systems. It involves:

1. Key generation: Creating strong, random keys
2. Key exchange: Securely sharing keys between parties
3. Key storage: Protecting keys from unauthorized access
4. Key rotation: Regularly updating keys to limit potential damage from breaches
5. Key revocation: Invalidating compromised keys

Proper key management is essential for the effective use of cryptography in PKI and other security systems.

Understanding these cryptographic primitives is crucial for grasping how PKI functions and provides security.