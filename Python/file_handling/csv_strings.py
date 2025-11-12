import csv
field_name =['No','Company','Car Model']
car=[
    {'No':1,'Company':'Ferrari','Car Model':'GH'},
    {'No':2,'Company':'BMW','Car Model':'M5'},
    {'No':3,'Company':'Suzuki','Car Model':'800'},
    {'No':4,'Company':'Audi','Car Model':'RS7'},
    {'No':5,'Company':'Toyota','Car Model':'Innova'}
]
with open('car.csv','w',newline='')as csvfile:
    write=csv.DictWriter(csvfile,fieldnames=field_name)
    write.writeheader()
    write.writerows(car)
with open('car.csv',newline='')as csvfile:
    d=csv.reader(csvfile)
    for r in d:
        print(','.join(r))
        print(r)