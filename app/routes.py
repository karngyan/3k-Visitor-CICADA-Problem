from app import app
count = 0


@app.route('/')
def index():
    global count
    count+=1
    if(count%1000 == 0):
        return 'Hard work or Lazy-Smart Work? Both pays but the amount is different ;) flag{ Good_Work_Coder }' 
    return f"You are visitor number: {count}. \nVisit this website 1000 times to get the reward."
