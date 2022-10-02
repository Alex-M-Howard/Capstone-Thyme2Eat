# Clone Project 
git clone https://github.com/Alex-M-Howard/Capstone-Thyme2Eat.git
cd Capstone-Thyme2Eat

# Install venv and activate 
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Create Database - Using PostgreSQL
creatdb thyme2eat

# Run app
flask --app Thyme2Eat run

# Navigate to localhost in Browser
In the browser go to 127.0.0.1:5000/
 
# Sign Up

# Get Meals

