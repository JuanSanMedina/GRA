from ecan.models import Item, Feature
items = Item.objects.all()
count = 0
for i in items:
    if not i.thumb:
        try:
            count+=1
            print count
            i.save()
        except:
            quit()