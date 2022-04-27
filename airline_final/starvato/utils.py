from uuid import uuid4

def create_unique_id(Identify):
    new = str(uuid4())
    check_new = Identify.objects.filter(unique_id = new)
    try:
        if check_new[0]:
            create_unique_id()
        else:
            Identify.objects.create(unique_id = new)
            return new
    except:
        Identify.objects.create(unique_id = new)
        return new

