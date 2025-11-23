# Beginner Python Projects

A collection of small, self-contained Python scripts I wrote while learning Python. Each file is a simple project you can run and study.

Files in this folder
- [chose_your_own_adventure.py](chose_your_own_adventure.py) — a small text-based adventure.
- [number_guesser.py](number_guesser.py) — guess the randomly chosen number.
- [rock_paper_scissors.py](rock_paper_scissors.py) — play Rock/Paper/Scissors vs the computer.
- [quiz_game.py](quiz_game.py) — a simple multiple-question quiz.
- [password_manager.py](password_manager.py) — minimal encrypted password manager. See functions [`password_manager.load_key`](password_manager.py), [`password_manager.add`](password_manager.py), [`password_manager.view`](password_manager.py).
- [passwords.txt](passwords.txt) — encrypted password storage used by the password manager.
- [key.key](key.key) — the symmetric key used by the password manager (Fernet).

Quick start
- Install Python 3.
- To run any script:
  - python3 <script_name>.py
  - Example: `python3 number_guesser.py`

Password manager notes
- The password manager uses the `cryptography` package. Install it with:
  - `pip install cryptography`
- The manager expects a valid key in [key.key](key.key) and stores entries in [passwords.txt](passwords.txt).
- Do not use real or sensitive passwords in this toy manager. Keep [key.key](key.key) private.

Suggestions
- Open a script to read the code and run it to see how input/output and control flow works.
- Try modifying or refactoring small parts (add functions, improve error handling, add tests).
- For the password manager, consider adding argument parsing, better file handling, or a secure keystore.

License & safety
- These are learning exercises. Do not use the password manager for production secrets.
- Remove or regenerate [key.key](key.key) before storing any real credentials.