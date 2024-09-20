from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def check_password(password):
    if len(password) < 15:
        return False
    if (any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in string.punctuation for c in password)):
        return True
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        password = request.form.get('password')

        # Generate a new password 
        if action == 'generate':
            password = generate_password()
            return render_template('e.html', password=password)

        elif action == 'yes':
            if not check_password(password):  # If the password is invalid,end game
                return render_template('e.html', message="GAME OVER!,You accepted an invalid password!.")
            else:
                # Valid passowrd; continue the game
                return render_template('e.html', message="Correct,Valid password accepted! Generate a new one...", password=generate_password())

        elif action == 'no':
            if check_password(password):  # If the password is invalid,end game
                return render_template('e.html', message="GAME OVER!,You rejected a valid password!.")
            else:
                # Valid password; continue the game
                return render_template('e.html', message="Correct,Invalid password rejected. Generating a new one...", password=generate_password())

    return render_template('e.html')

if __name__ == '__main__':
    app.run(debug=True)
