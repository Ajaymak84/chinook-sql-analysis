import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("Chinook_Sqlite.sqlite")
print("Connected")

query1 = '''select T.Trackid,T.Name,T.Composer,sum(I.Quantity)as TotalNumbersold
from Track T JOIN
InvoiceLine I on T.TrackId = I.TrackId
GROUP by T.TrackId,T.Name,T.Composer
ORDER BY TotalNumbersold DESC
limit 10;'''

query2 = '''Select Country 
from (
select BillingCountry as Country,sum(Total) as Total_rev
from Invoice
GROUP BY BillingCountry
ORDER by Total_rev DESC
limit 1) t;'''

query3 = '''select e.firstname,e.LastName,c.supportrepid,round(sum(i.Total),2) as Total_rev
from customer c join employee e ON
c.supportrepid = e.employeeid
join Invoice i on i.CustomerId = c.CustomerId
GROUP by e.FirstName,e.LastName,c.supportrepid
ORDER BY TotaL_rev DESC
LIMIT 1;'''

bestsellingtracks = pd.read_sql_query(query1,conn)
MostrevenueCountry = pd.read_sql_query(query2,conn)
topperformingsalesemployee = pd.read_sql_query(query3,conn)

print(bestsellingtracks)
print(MostrevenueCountry)
print(topperformingsalesemployee)

plt.figure(figsize=(12,6))

plt.bar(
    bestsellingtracks['Name'],
    bestsellingtracks['TotalNumbersold']
)

plt.xticks(rotation=45)

plt.show()

conn.close()