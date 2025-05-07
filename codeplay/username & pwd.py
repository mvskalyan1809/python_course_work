data={'kalyan':'kalyan180903',
      'pramodh':'pramodh101112',
      'punith':'punith101112',
      'sushanth':'sushanth150113'}

def login(username,pwd):
    if data.get(username)==pwd:
        print('login succesfull',username)
    else:
        print('inavlid username or pwd')

login('kalyan','kalyan180903')
login('pramodh','pramodh101112')
login('punith','punith101112')
login('sushanth','sushanth150113')
    
