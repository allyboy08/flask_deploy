from flask import Flask, render_template,request
import smtplib

app= Flask(__name__)

@app.route('/')
def load_index():
    return render_template('contact.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/send_email/',methods=["POST","GET"])
def send_email():
    message1=request.form['message']

    server= smtplib.SMTP('smtp.gmail.com')
    sender_email='sassmanalex3@gmail.com'
    reciever_email=request.form['Email']
    password='maxsassy08'
    server.starttls()
    server.login(sender_email,password)
    server.sendmail(sender_email,reciever_email,message1)
    server.quit()
    return render_template('success.html')



if __name__=='__main__':
    app.run(debug=True)
