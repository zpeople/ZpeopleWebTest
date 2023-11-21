
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def main():
    return '''
     <h3>welcome to my webpage!</h3><hr><p style="color:red">haha,I am Zpeople. Please check your review coursera user_id Is zpeople,  yes or no?</p>
     <form action="/echo_user_input" method="POST">
         <input name="user_input">
         <input type="submit" value="Submit!">
     </form>
     '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    if input_text=="yes":
        return "Your submit is  " + input_text+ ".Thank you for your review!"
    else:
        return  "Your submit is  " + input_text+ ".You may have found a plagiarism!"

if __name__ == '__main__':
    # flask应用运行
    app.run()