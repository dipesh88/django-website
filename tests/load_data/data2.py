import datetime
t = datetime.datetime.today()
crr_month,crr_year = t.month,t.year

Lusers = []
Dexpenses = {}

# Expenses list for multiple expenses tests
# The full expense tuple is (1,2016,$100,50%,'desc','place','notes')
expenses = [
    (130,50,'School Books','Books Store',''),
    (90,50,'Sneakers','Amazon',''),
    (450,50,'Soccer League','Soccer League',''),
    (240,50,'Scouts','Scouts',''),
    (30,50,'Snacks and drinks for School event','Whole Foods','mid-year party'),
    (110,50,'Coat','Target',''),
    (150,50,'Math tutor','Elaine',''),
    (150,50,'School Payment','School','half year payment'),
    (75,50,'Shoes','Zappos',''),
    (28,50,'Disney Toys','Disney','Elsa, Baz'),
    (20,50,"Friend's birthday gift",'Scouts',''),
    (32,50,'Coloring set','Crayola','for the holiday'),
    (80,50,'Dress for School party','Store',''),
    (350,50,'Smart phone','Amazon',''),
]