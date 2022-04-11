from uuid import uuid4

def unique_id():

    return str(uuid4())


'''
cosciente del fatto che non sia sicuro
devo trovare un modo per confrontare tutti gli id creati e
se è uguale a qualcuno ricrearlo


si potrebbe creare un json per controllare
'''