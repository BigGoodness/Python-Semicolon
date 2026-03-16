print("""

   ____________________________________________
   |Collection Rate|Amount Per Parcel|Base Pay|
   |Less than 50%  |              160|  5,000 |
   |50-59%         |              200|  5,000 |
   |60-69%         |              250|  5,000 |
   |>=70%          |              500|  5,000 |

    """)

Successful_deliveries = int(input("Enter the number of successful deliveries: "))

def deliveries(Successful_deliveries):

    wagesOfRider = 0

if Successful_deliveries < 50:
                 wagesOfRider = Successful_deliveries * 160 + 5000
elif Successful_deliveries >= 50 and Successful_deliveries <= 59:
                 wagesOfRider = Successful_deliveries * 200 + 5000 
elif Successful_deliveries >= 60 and Successful_deliveries <= 69:
                 wagesOfRider = Successful_deliveries * 250 + 5000
elif Successful_deliveries >= 70:
                 wagesOfRider = Successful_deliveries * 500 + 5000

print("The rider's wage is: ", wagesOfRider)
  
