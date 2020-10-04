def pond_first_time(area):
    first_time_index={}
    first_time_index['pond renovation extra cost ------------------------']=area*(10000/60)
    #cun>1sotok>1kg>25tk per kg
    
    #shallow_machine 1horse power costs 10000 tk
    first_time_index['shallow_machine -----------------------------------']=10000
    #netting>5 bundle costs 5000 tk
    
    return first_time_index

def pond_annual_time(area):
    annual_time_index={}
    annual_time_index['stone lime 1kg(25tk) per decimal ----------------']=area*25
    annual_time_index['netting -----------------------------------------']=5000
    #pond lease means pond is already dug.
    annual_time_index['pond lease---------------------- ----------------']=(30000/60)*area
    annual_time_index['pabda fish fry (.80tk per piece) \nand 1166piece per decimal------------------------']=(56000/60)*area
    #transportation includes drum, labour, saline, polybag, oxygen, etc.
    annual_time_index['transportation and drums, labour,\n saline, polybag, oxygen, etc.-------------------']=6000
    #feed 2000 kg for 60 Sotok and per kg costs 85 tk total 1,70,000tk
    annual_time_index['feed---------------------------- ----------------']=(170000/60)*area
    #bangla fish (rui, katla, mrigel, silver, etc.) 150kg for 60 Sotok>300 piece>30000tk
    annual_time_index['bangla_fish(Roi, Mrigal, Grass-carp,\n silver, Katal, etc.-----------------------------']=(30000/60)*area
    annual_time_index['electricity--------------------------------------']=(36000/60)*area
    annual_time_index['medicine ----------------------------------------']=(20000/60)*area
    annual_time_index['labour ------------------------------------------']=(24000/60)*area
    annual_time_index['extra -------------------------------------------']=(24000/60)*area
    return annual_time_index

def income(area):
    #mortality 10%
    #30 fish(after 8 months) become 1kg
    #60 Sotok>initial 70000>after death remains=70000-(70000*10%)=63000 piece>2100kg>525000tk
    income_index={}
    income_index['pabda fish --- ----------------------------------']=(525000/60)*area
    #60 Sotok >bangla fish>300 piece>2kg per piece>600kg > (600*150)=90000tk
    income_index['bangla fish(Roi, Mrigal, Grass-carp,\n  silver fish, katal, etc. ----------------------']=(90000/60)*area
    return income_index

def create_bar(annual_values, annual_names):
    import matplotlib.pyplot as plt
    n=len(annual_values)

    xt=['lime','net','lease','fry','transportation','feed','bangla','electricity','medicine','labour','extra']
    position=[x for x in range(n)]
    plt.bar(position,annual_values)
    plt.title("Annual Cost for Each Item")
    plt.xticks(position,xt)
    plt.grid()
    plt.xlabel("items --->")
    plt.ylabel("taka --->")
    plt.show()










def user_input():
    print("""
-------------------------------------------------------------------------
Pabda Fish Fry Culture Cost Estimation
A project by
Showmik Ahmed Pranta
showmikahmedpranta@gmail.com
Data and literary support:
Md. Anisur Rahman
anisurheds@gmail.com""")
    land=float(input("Enter the area of pond with land border in Decimal: "))
    n=float(input("Enter the area of your pond water area in Decimal:  "))
    first=pond_first_time(n)
    annual=pond_annual_time(n)
    first_time_cost=0
    annual_time_cost=0
    for j in first.values():
        first_time_cost=first_time_cost+j
    print("\nFirst time cost: ")
    for i,j in first.items():
        print(i,'-------------->',int(j))
    print("Total first time cost = ---------------------------- --------------",int(first_time_cost))

    annual_names=[]
    annual_values=[]
    for j in annual.values():
        annual_time_cost=annual_time_cost+j
    print("\nAnnual cost ")
    for i,j in annual.items():
        annual_names.append(i)
        annual_values.append(int(j))
        print(i,'---------------->',int(j))
    print("\nTotal annual cost excluding first time cost = ---- ----------------",int(annual_time_cost))

    print("\nTotal cost first year = ---- --------------------------------------",int(first_time_cost+annual_time_cost))
    income_list=income(n)
    inco=0
    for j in income_list.values():
        inco=inco+j
    print("\nIncome list:")
    for i,j in income_list.items():
        print(i,'---------------->',int(j))
    print("\nannual income = ---------------------------------- ----------------",int(inco))

    print("\n**********************")
    print("\nBeginning year profit:")
    profit_beginning=inco-(first_time_cost+annual_time_cost)
    profit_percentage_beginning=(profit_beginning*100)/(first_time_cost+annual_time_cost)
    print("Profit beginning= --------------------------------- ---------------", int(profit_beginning))
    print("Profit percentage in the first year =   ---------- ----------------",int(profit_percentage_beginning))
    print("************************************")
    profit_second_year=inco-(annual_time_cost)
    profit_percentage_second_year=(profit_second_year*100)/annual_time_cost
    print("Profit second year onward yearly =   ------------- ----------------",int(profit_second_year))
    print("Profit percentage in the second year =   --------- ----------------", int(profit_percentage_second_year))
    create_bar(annual_values, annual_names)




if(__name__=='__main__'):
    user_input()

