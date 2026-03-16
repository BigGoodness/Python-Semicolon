menu = """
======== MENU FUNCTIONS ===========
1. Phone Book
2. Messages
3. Chat
4. Call Register
5. Tones
6. Settings
7. Call Divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. printofiles
13. SIM Services
===================================
 """
print(menu)
option =int(input("Enter Option: "))

match option:
    case 1: 
        menu = """
        ======== PHONE BOOK ===========
        1. Search
        2. Service Nos.
        3. Add name
        4. Erase
        5. Edit
        6. Assign tone
        7. Send b'card
        8. Option
        9. Speed dials
        10. Voice tags
        =================================== """
        print(menu)
        print("Enter option: ")

        option =int(input("Enter Option: "))
        match option:
            case 1 : print("Search")
            case 2 : print("Service Nos")
            case 3 : print("Add Names")
            case 4 : print("Erase")
            case 5 : print("Edit")
            case 6 : print("Assign tone")
            case 7 : print("Send b'card")
            case 8 : 
                menu = """
                ======== OPTIONS ===========
                1. Type of views
                2. Memory Status
                ============================= 
                """
                print(menu)
                option = int(input("Enter Option: "))
                match(option):
                    case 1 : print("Type of view")
                    case 2 : print("Type of view")
                    case 3 : print("Enter valid number")

            case 9 : print("Speed dials")
            case 10 : print("voice tags")
            

    case 2 : 
        menu =""" 
        ======== MESSAGES ===========
        1. Write Message
        2. Inbox
        3. Outbox
        4. Picture Messages
        5. Template
        6. Smileys
        7. Messages settings
        8. Info Service
        9. Voice mailbox number
        10. Service command editor
        =================================== """
        print(menu)
        option =int(input("Enter Option: "))
        match (option):
            case 1 : print(" Write message")
            case 2 : print("inboxx")
            case 3 : print("outbox")
            case 4 : print("picture message")
            case 5 : print("Template")
            case 6 : print("Smileys")
            case 7 : 
                menu =""" 
        ======== MESSAGE SETTINGS ===========
        1. Set 1
        2. Common 3
        =================================== """
                print(menu)
                option =int(input("Enter Option: "))
                match(option):
                    case 1 :
                        menu =""" 
                ======== MESSAGE SETTINGS ===========
                1. Message centre number
                2. Message send as
                3. Message validity
                =================================== 
                        """
                        print(menu)
                        option =int(input("Enter Option: "))
                        match(option):
                            case 1 : print("Message centre number")
                            case 2 : print("Message send as")
                            case 3 : print("message validity")
                            
                        

                    case 2 :
                        menu =""" 
                ======== MESSAGE SETTINGS ===========
                1. Delivery
                2. Reply via same centre
                3. Character support
                =================================== """
                        print(menu)
                        print("Enter option: ")
                        option =int(input("Enter Option: "))
                        match(option):
                            case 1 : print("Delivery")
                            case 2 : print("Reply via same centre")
                            case 3 : print("character support")
                            
                            case 8 : print("Template")
                            case 9 : print("voice mailbox number")
                            case 10 : print("Services command editor")
                        

          
    case 3 : print("Chat")
    case 4 :
        menu = """
    ======== CALL REGISTER ===========
    1. Missed Calls
    2. Received
    3. Dailled Numbers
    4. Erase recebt call lists
    5. show call duration
    6. show call costs
    7. call cost settings
    8. printepaid credit
    =================================== """
        print(menu)
        option =int(input("Enter Option: "))
        match (option):
            case 1 : print("Missed calls")
            case 2 : print("Received calls")
            case 3 : print("Dailled numbers")
            case 4 : print("Erase recent call lists")
            case 5 : 
                menu = """
            ======== SHOW ALL CALL DURATION ===========
            1. Last call duration
            2. All call's duration 
            3. Received calls' duration
            4. Dialled calls' duration
            5. Clear Timers
            =================================== """
                print(menu)
                option =int(input("Enter Option: "))
                match (option):
                    case 1 : print("Last call duration")
                    case 2 : print("All calls duration")
                    case 3 : print("Recieved calls duration")
                    case 4 : print("Dialled calls duration")
                    case 5 : print("Clear timers")

            case 6 : 
                menu = """
            ======== SHOW CALL COST  ===========
            1. Last call cost
            2. All calls cost 
            3. clear counters
            =================================== """
                print(menu)
                option =int(input("Enter Option: "))
                match (option):
                    case 1 : print("Last call cost")
                    case 2 : print("All calls cost")
                    case 3 : print("clear counters")
                        
            case 7 :
                menu = """
            ======== CALL COST SETTINGS  ===========
            1. Call cost limit
            2. Show costs in
            =================================== """
                print(menu)
                option =int(input("Enter Option: "))
                match (option):
                    case 1 : print("call cost limit")
                    case 2 : print("show costs in")
                    
            case 8 :print("printepaid credit")

          

    case 5 : 
        menu = """
    ======== TONES ===========
    1. Ringing tone
    2. Ringing volume
    3. incoming call alert
    4. Composer
    5. Message alert tone
    6. Keypad tones
    7. Warning and game tones
    8. Vibrating alert
    9. Screen saver
    =================================== 
        """
        print(menu)
        option =int(input("Enter Option: "))
        match (option):
            case 1 : print("Ringing tone")
            case 2 : print("Ringing volume")
            case 3 : print("Incoming alert")
            case 4 : print("Composer")
            case 5 : print("Message alert tone")
            case 6 : print("Keypad tones")
            case 7 : print("Warning and game tones")
            case 8 : print("Vibrating alert")
            case 9 : print("Screen saver")

    case 6 : 
        menu = """
    ======== SETTINGS ===========
    1. Call settings
    2. Phone Settings
    3. Security Settings
    4. Restore Factory Settings
    =================================== """
        print(menu)
        option =int(input("Enter Option: "))
        match (option):
            case 1 : 
                menu = """
            ======== CALL SETTINGS ===========
            1. Automatic redial
            2. Speed dialing
            3. Call waiting options
            4. Own number sending
            5. Phone line in use
            6. Automatic answer
            =================================== """
                print(menu)
                option =int(input("Enter Option: "))
                match (option):
                    case 1 : print("Automatic redial")
                    case 2 : print("Speed dialing")
                    case 3 : print("Call waiting")
                    case 4 : print("Own number")
                    case 5 : print("Phone line in use")
                    case 6 : print("Automatic answer")
            
            case 2 :
                menu = """
            ======== PHONE SETTINGS ===========
            1. Language
            2. Cell info display
            3. Welcome note
            4. Network Selection
            5. Lights
            6. Confirm SIM service actions
            =================================== """
                print(menu)
                print("Enter option: ")
                option =int(input("Enter Option: "))
                match (option):
                    case 1 : print("Language")
                    case 2 : print("cell info display")
                    case 3 : print("welcome note")
                    case 4 : print("Network selection")
                    case 5 : print("Lights")
                    case 6 : print("Confirm SIM service actions")
                    
            case 3 : 
                menu = """
            ======== SECURITY SETTINGS ===========
            1. PIN code request
            2. Call barring service
            3. Fixed dailing
            4. closed user group
            5. Phone security
            6. Change access codes
            =================================== """
                print(menu)
                print("Enter option: ")
                option =int(input("Enter Option: "))
                match (option):
                    case 1 : print("PIN code request")
                    case 2 : print("call barring service")
                    case 3 : print("Fixed dailing")
                    case 4 : print("Closed user group")
                    case 5 : print("Phone security")
                    case 6 : print("Change access code")
                        

            case 4 : print("Restore factory settings")
                    

    case 7 :print("Call divert") 
    case 8 :print("Games") 
    case 9 :print("Calculator") 
    case 10 :print("Reminders") 
    case 11 :
        menu = """
    ======== CLOCK ===========
    1. Alarm clock
    2. Clock settings
    3. Date settings
    4. StopWatch
    5. Countdown timer
    6. Auto update of date and time
    =================================== """
        print(menu)
        print("Enter option: ")
        option =int(input("Enter Option: "))
        match (option):
            case 1 : print("Alarm clock")
            case 2 : print("Clock settings")
            case 3 : print("Date settings")
            case 4 : print("stopwatch")
            case 5 : print("Countdown timer")
            case 6 : print("Auto upate of date and time")
           
    case 12 :print("printofiles") 
    case 13 :print("SIM Service") 





