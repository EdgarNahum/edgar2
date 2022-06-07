import cloudpickle
from flask import Flask, render_template, request

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', nome='Fulano')

@app.route('/predicao', methods=['POST'])
def predicao():
  Age = int(request.form['Age'])
  YearsAtCompany = int(request.form['YearsAtCompany'])
  Department = int(request.form['Department'])
  JobSatisfaction = int(request.form['JobSatisfaction'])
  MaritalStatus = int(request.form['MaritalStatus'])
  WorkLifeBalance = int(request.form['WorkLifeBalance'])
  
 
  predicao = model.predict([[Age,YearsAtCompany,Department,JobSatisfaction,MaritalStatus,WorkLifeBalance]])
  return render_template('resposta.html', predicao=predicao[0])

app.run(debug=True)

# pip install -r requirements.txt (instala as bibliotecas)
# python app.py (para executar)

# git add .
# git commit -m "nomenovo"
# git push



