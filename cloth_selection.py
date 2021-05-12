print(" ********************  Welcome to the My Fashion shop  ******************** ")
print("We are happy to see you here ")
a = int(input("Press 1 for Shopping and 2 for Exit "))
jeans = 700
shirt = 600
tshirt = 500
sweater = 1000

slmj = []
slmt = []
slms = []
slmsw = []

slwj = []
slwt = []
slws = []
slwsw = []

slkj = []
slks = []
slksw = []
slkt = []

mj = 0
mt = 0
ms = 0
msw = 0
wj = 0
wt = 0
ws = 0
wsw = 0
kj = 0
ks = 0
ksw = 0
kt = 0

while a == 1:
    shopping_list_men = {}
    shopping_list_men_jeans = {}
    shopping_list_men_tshirts = {}
    shopping_list_men_shirts = {}
    shopping_list_men_sweaters = {}

    shopping_list_women = {}
    shopping_list_women_jeans = {}
    shopping_list_women_tshirts = {}
    shopping_list_women_shirts = {}
    shopping_list_women_sweaters = {}

    shopping_list_kid = {}
    shopping_list_kid_jeans = {}
    shopping_list_kid_tshirts = {}
    shopping_list_kid_shirts = {}
    shopping_list_kid_sweaters = {}

    b = int(input(
        "Select 1 for Men Section\nSelect 2 for Women Section\nSelect 3 for Kid Section"))
    if b == 1:  # go for men's section
        c = int(input(
            "Select 1 for Jeans\nSelect 2 for T-Shirts\nSelect 3 for Shirts\nSelect 4 for Sweaters"))
        if c == 1:
            # quantity 700 per jeans
            qtyMJ = int(input("Enter number of pieces"))
            bill_for_men_jeans = 700 * qtyMJ

            shopping_list_men_jeans["Section"] = "Men"
            shopping_list_men_jeans["Item"] = "Jeans"
            shopping_list_men_jeans["Quantity"] = qtyMJ
            shopping_list_men_jeans["Cost"] = bill_for_men_jeans

            slmj = list(shopping_list_men_jeans.values())

            a = int(input("Do you want to continue press 1 if not press 2"))
            if a == 1:

                continue
            else:

                break

        elif c == 2:
            qtyMT = int(input("Enter number of pieces"))  # 500 per t-shirt
            bill_for_men_tshirts = 500 * qtyMT

            shopping_list_men_tshirts["Section"] = "Men"
            shopping_list_men_tshirts["Item"] = "T-Shirt"
            shopping_list_men_tshirts["Quantity"] = qtyMT
            shopping_list_men_tshirts["Cost"] = bill_for_men_tshirts

            slmt = list(shopping_list_men_tshirts.values())

            a = int(input("Do you want to continue press 1 if not press 2"))
            if a == 1:

                continue
            else:

                break

        elif c == 3:
            qtyMS = int(input("Enter number of pieces"))  # 600 per shirt
            bill_for_men_shirts = 600 * qtyMS

            shopping_list_men_shirts["Section"] = "Men"
            shopping_list_men_shirts["Item"] = "Shirt"
            shopping_list_men_shirts["Quantity"] = qtyMS
            shopping_list_men_shirts["Cost"] = bill_for_men_shirts

            slms = list(shopping_list_men_shirts.values())

            a = int(input("Do you want to continue press 1 if not press 2"))
            if a == 1:
                continue
            else:

                break

        elif c == 4:
            qtyMSW = int(input("Enter number of pieces"))  # 1000 per sweaters
            bill_for_men_sweaters = 1000 * qtyMSW

            shopping_list_men_sweaters["Section"] = "Men"
            shopping_list_men_sweaters["Item"] = "Sweater"
            shopping_list_men_sweaters["Quantity"] = qtyMSW
            shopping_list_men_sweaters["Cost"] = bill_for_men_sweaters
            slmsw = list(shopping_list_men_sweaters.values())

            a = int(input("Do you want to continue press 1 if not press 2"))
            if a == 1:
                continue
            else:

                break

        else:
            print("Invalid choice")
            break

    if b == 2:  # go to womens section
        c = int(input(
            "Select 1 for Jeans\nSelect 2 for T-Shirts\nSelect 3 for Shirts\nSelect 4 for Sweaters"))
        if c == 1:
            # quantity 700 per jeans
            qtyWJ = int(input("Enter number of pieces"))
            bill_for_women_jeans = 700 * qtyWJ

            shopping_list_women_jeans["Section"] = "Women"
            shopping_list_women_jeans["Item"] = "Jeans"
            shopping_list_women_jeans["Quantity"] = qtyWJ
            shopping_list_women_jeans["Cost"] = bill_for_women_jeans
            slwj = list(shopping_list_women_jeans.values())

            a = int(input("Do you want to continue press 1 if not press 2"))
            if a == 1:
                continue
            else:

                break

        elif c == 2:
            qtyWT = int(input("Enter number of pieces"))  # 500 per t-shirt
            bill_for_women_tshirts = 500 * qtyWT

            shopping_list_women_tshirts["Section"] = "Women"
            shopping_list_women_tshirts["Item"] = "T-shirt"
            shopping_list_women_tshirts["Quantity"] = qtyWT
            shopping_list_women_tshirts["Cost"] = bill_for_women_tshirts
            slwt = list(shopping_list_women_tshirts.values())

            a = int(input("Do you want to continue press 1 if not press 2"))
            if a == 1:
                continue
            else:

                break

        elif c == 3:
            qtyWS = int(input("Enter number of pieces"))  # 600 per shirt
            bill_for_women_shirts = 600 * qtyWS

            shopping_list_women_shirts["Section"] = "Women"
            shopping_list_women_shirts["Item"] = "Shirt"
            shopping_list_women_shirts["Quantity"] = qtyWS
            shopping_list_women_shirts["Cost"] = bill_for_women_shirts
            slws = list(shopping_list_women_shirts.values())

            a = int(input("Do you want to continue press 1 if not press 2"))
            if a == 1:
                continue
            else:

                break

        elif c == 4:
            qtyWSW = int(input("Enter number of pieces"))  # 1000 per sweater
            bill_for_women_sweaters = 1000 * qtyWSW

            shopping_list_women_sweaters["Section"] = "Women"
            shopping_list_women_sweaters["Item"] = "Sweater"
            shopping_list_women_sweaters["Quantity"] = qtyWSW
            shopping_list_women_sweaters["Cost"] = bill_for_women_sweaters

            slwsw = list(shopping_list_women_sweaters.values())

            a = int(input("Do you want to continue press 1 if not press 2"))
            if a == 1:
                continue
            else:

                break

        else:
            print("Invalid choice")
            break

    if b == 3:  # go to kids section
        c = int(input(
            "Select 1 for Jeans\nSelect 2 for T-Shirts\nSelect 3 for Shirts\nSelect 4 for Sweaters"))
        if c == 1:
            # quantity 700 per jeans
            qtyKJ = int(input("Enter number of pieces"))
            bill_for_kid_jeans = 700 * qtyKJ

            shopping_list_kid_jeans["Section"] = "Kid"
            shopping_list_kid_jeans["Item"] = "Shirt"
            shopping_list_kid_jeans["Quantity"] = qtyKJ
            shopping_list_kid_jeans["Cost"] = bill_for_kid_jeans

            slkj = list(shopping_list_kid_jeans.values())

            a = int(input("Do you want to continue press 1 if not press 2"))
            if a == 1:
                continue
            else:

                break

        elif c == 2:
            qtyKT = int(input("Enter number of pieces"))  # 500 per t-shirt
            bill_for_kid_tshirts = 500 * qtyKT

            shopping_list_kid_tshirts["Section"] = "Kid"
            shopping_list_kid_tshirts["Item"] = "T-shirt"
            shopping_list_kid_tshirts["Quantity"] = qtyKT
            shopping_list_kid_tshirts["Cost"] = bill_for_kid_tshirts
            slkt = list(shopping_list_kid_tshirts.values())

            a = int(input("Do you want to continue press 1 if not press 2"))
            if a == 1:
                continue
            else:

                break

        elif c == 3:
            qtyKS = int(input("Enter number of pieces"))  # 600 per shirt
            bill_for_kid_shirts = 600 * qtyKS

            shopping_list_kid_shirts["Section"] = "Kid"
            shopping_list_kid_shirts["Item"] = "Shirt"
            shopping_list_kid_shirts["Quantity"] = qtyKS
            shopping_list_kid_shirts["Cost"] = bill_for_kid_shirts

            slks = list(shopping_list_kid_shirts.values())

            a = int(input("Do you want to continue press 1 if not press 2"))
            if a == 1:
                continue
            else:

                break

        elif c == 4:
            qtyKSW = int(input("Enter number of pieces"))  # 1000 per sweater
            bill_for_kid_sweaters = 1000 * qtyKSW

            shopping_list_kid_sweaters["Section"] = "Kid"
            shopping_list_kid_sweaters["Item"] = "Sweater"
            shopping_list_kid_sweaters["Quantity"] = qtyKSW
            shopping_list_kid_sweaters["Cost"] = bill_for_kid_sweaters

            slksw = list(shopping_list_kid_sweaters.values())

            a = int(input("Do you want to continue press 1 if not press 2"))
            if a == 1:
                continue
            else:

                break

        else:
            print("Invalid choice")
            break

    else:
        break


def tc(mj=0, mt=0, ms=0, msw=0, wj=0, wt=0, ws=0, wsw=0, kj=0, ks=0, ksw=0, kt=0):
    if len(slmj) > 0:
        mj = slmj[3]
    if len(slmt) > 0:
        mt = slmt[3]
    if len(slms) > 0:
        ms = slms[3]
    if len(slmsw) > 0:
        msw = slmsw[3]

    if len(slwj) > 0:
        wj = slwj[3]
    if len(slws) > 0:
        ws = slws[3]
    if len(slwt) > 0:
        wt = slwt[3]
    if len(slwsw) > 0:
        wsw = slwsw[3]

    if len(slkj) > 0:
        kj = slkj[3]
    if len(slkt) > 0:
        kt = slkt[3]
    if len(slks) > 0:
        ks = slks[3]
    if len(slksw) > 0:
        ksw = slksw[3]

    return (mj+mt+ms+msw+wj+wt+ws+wsw+kj+ks+kt+ksw)


total_cost = tc(mj, mt, ms, msw, wj, wt, ws, wsw, kj, ks, ksw, kt)


def discount(bill_amt=total_cost):

    if bill_amt <= 5000:
        disct = bill_amt * 0.05
        final_bill = bill_amt - disct
    elif (bill_amt >= 5001 and bill_amt <= 10000):
        disct = bill_amt * 0.07
        final_bill = bill_amt - disct
    elif (bill_amt >= 10001 and bill_amt <= 15000):
        disct = bill_amt * 0.1
        final_bill = bill_amt - disct
    else:
        disct = bill_amt * 0.12
        final_bill = bill_amt - disct

    return final_bill


print("**********************  MY FASHION SUPER MART  ****************************")
print("SECTION  ITEM  QTY  TOTAL COST")

if len(slmj) > 0:
    for i in slmj:
        print(i, end="    ")
    print("")
if len(slms) > 0:
    for i in slms:
        print(i, end="    ")
    print("")
if len(slmsw) > 0:
    for i in slmsw:
        print(i, end="    ")
    print("")
if len(slmt) > 0:
    for i in slmt:
        print(i, end="    ")
    print("")


if len(slwj) > 0:
    for i in slwj:
        print(i, end="    ")
    print("")
if len(slwt) > 0:
    for i in slwt:
        print(i, end="    ")
    print("")
if len(slws) > 0:
    for i in slws:
        print(i, end="    ")
    print("")
if len(slwsw) > 0:
    for i in slwsw:
        print(i, end="    ")
    print("")


if len(slkj) > 0:
    for i in slkj:
        print(i, end="    ")
    print("")
if len(slkt) > 0:
    for i in slkt:
        print(i, end="    ")
    print("")
if len(slks) > 0:
    for i in slks:
        print(i, end="    ")
    print("")
if len(slksw) > 0:
    for i in slksw:
        print(i, end="    ")
    print("")

print("-------------------------------------------------------------------------------------------------------------")

print("                Total : "+str(total_cost))
amount_after_discount = discount()
print("amount_after_discount : " + str(amount_after_discount))

print("-------------------------------------------------------------------------------------------------------------")

tc_with_gst = amount_after_discount*(1+0.09)
tax = tc_with_gst - amount_after_discount
print("                TAX : "+str(tax))
print("  TOTAL COST WITH GST : "+str(tc_with_gst))

print("-------------------------------------------------------------------------------------------------------------")
print("          Thank You For Shopping, Please Visit Again...")
