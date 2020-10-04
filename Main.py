import sports 
From pynotifier import Notification

matchinfo = sports.get_sport("cricket")

Notification(title= "LIVE SCORE", description= str(matchinfo), duration= 40).send()
