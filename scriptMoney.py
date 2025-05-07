#math library
import math

#colored text library
from colorama import init, Fore, Style
init(autoreset=True)

#import textx for parsing and processing the lang
from textx import metamodel_from_file

scriptMoney_mm = metamodel_from_file('scriptMoney.tx')
scriptMoney_model = scriptMoney_mm.model_from_file('program3.sm')

class scriptMoney:
    def __init__(self):
        #intializes all values to zero
        self.account_type = None
        self.year = 0
        self.rate = 0
        self.amount = 0.0
        self.depositTotal = 0.0
        self.withdrawalTotal = 0.0
        #returns the expression of the userinput based of it is an int, float or str
    def eval_expr(self, expr):
        if isinstance(expr, (int, float)):
            return expr
        elif isinstance(expr, str):
            return expr
    #annual percentage yield calculations
    def calc_apy(self, rate, n):
        apy = math.pow(1 + rate/ n, n) - 1
        return apy

    #creates a dictionary to showcase the user the pros and cons of each savings/investment type
    pro_con_dict = { 
        "Traditional Savings": {
            "Pros": ["Safe and FDIC-insured", "Easy to open and access", "No risk of losing principal", "Risk-Free Savings"],
            "Cons": ["Very low interest rates"]
        },
        "High Yield": {
            "Pros": ["Easy to open and access", "Higher Interest Rates compared to Traditional Accounts", "Felixibility", "Risk-Free Savings"],
            "Cons": ["Not good for everday transactions", "More requirements than a Traditional account", "Fluctuating interest rates"]
        },
        "CD" : {
            "Pros": ["Higher Fixed Interest rate", "Low Risk", "Good for short-long term investments/savings"],
            "Cons": ["Unable to take out money due it being locked", "Early withdrawal penalities", "Lower potential returns"]
        },
        "Bonds": {
            "Pros": ["Less Risky than Stocks", "High Returns", "Predictable Returns"],
            "Cons": ["Value drops when interest rates rise", "Bonds can be called early", "Yields will not keep up with inflation"]
        },
        "Roth IRA": {
            "Pros": ["Tax-Free growth and withdrawals in retirement", "Contributions can be withdrawn anytime without penalty"],
            "Cons": ["There is an income limit to contribute", "Earnings cannot be withdrawn until the user is 59.5 years old and the account needs to be 5 years old", "No tax deduction for contributing"]
        },
    }
    #user data for dictionary to store data for deposited and withdrawal money
    def interpret(self, model):
        for statement in model.statements:
            #checks if the user inputs the savings option
            if statement.__class__.__name__ == "SavingsStatement":
                #handle calulations for different types
                self.year = self.eval_expr(statement.year)
                self.rate = self.eval_expr(statement.rate)
                self.amount = self.eval_expr(statement.amount)
                #writes an error if the user does not input each value
                if None in (self.year, self.amount):
                    raise ValueError("Please enter values for your year, and the amount of money you would like!")
                #cases for each type of account the user decides to put
                match statement.account_type:
                    case "Traditional":
                        print(Style.BRIGHT + f"Traditional bank savings are offered by banks and you're allowed to store money securely")
                        trad_pro_con = self.pro_con_dict.get("Traditional Savings")
                        print("Pros: ")
                        for pro in trad_pro_con.get("Pros", []):
                            print(f"• {pro}")
                        print("Cons: ")
                        for con in trad_pro_con.get("Cons", []):
                            print(f"• {con}")
                        print(f"Year(s) you have entered: " + str(self.year))
                        print(f"Traditional precentage rate is at 0.051%")
                        print(f"The amount of money you have inputed: " + str(self.amount))
                        trad_total = self.amount * (0.51/100) * self.year
                        print(f"The amount that you have saved")
                        print(Fore.GREEN +str(trad_total))
                        print(f"The amount that you saved in total ")
                        print(Fore.GREEN + str(self.amount + trad_total))
                    case "High Yield":
                        print(Style.BRIGHT + f"High-Yield savings are similar to a traditional savings, however it has higher interest rates, but usually offered by online banks or financial institutions with lower overhead cost")
                        high_yield_pro_con = self.pro_con_dict.get("High Yield")
                        print("Pros: ")
                        for pro in high_yield_pro_con.get("Pros", []):
                            print(f"• {pro}")
                        print("Cons: ")
                        for con in high_yield_pro_con.get("Cons", []):
                            print(f"• {con}")
                        print(f"Year(s) you have entered: " + str(self.year))
                        print(f"The percentage rate you have entered: " + str(self.rate))
                        print(f"The amount of money you have inputed: " + str(self.amount))
                        apy = self.calc_apy(self.rate/100, 12) 
                        high_yield_total = self.amount * math.pow(1 + apy, self.year)
                        print(f"The amount you have saved with High-Yield:")
                        print(Fore.GREEN +str(high_yield_total))
                        print(f"The amount you have saved in total with High-Yield:")
                        print(Fore.GREEN +str(high_yield_total + self.amount))
                    case "CD":
                        print(Style.BRIGHT + f"CD or certificate of deposit is a low-risk savings/interest product offered by banks and credit unions")
                        CD_pro_con = self.pro_con_dict.get("CD")
                        print("Pros: ")
                        for pro in CD_pro_con .get("Pros", []):
                            print(f"• {pro}")
                        print("Cons: ")
                        for con in CD_pro_con .get("Cons", []):
                            print(f"• {con}")
                        print(f"Year(s) you have entered: " + str(self.year))
                        print(f"The percentage rate you have entered: " + str(self.rate))
                        print(f"The amount of money you have inputed: " + str(self.amount))
                        apy = self.calc_apy(self.rate/100, 12) 
                        cd_total = self.amount * math.pow(1 + apy, self.year)
                        print(f"The amount you have saved with CDs:")
                        print(Fore.GREEN +str(cd_total))
                        print(f"The amount you have saved in total with CDs:")
                        print(Fore.GREEN +str(cd_total + self.amount))
            #checks if the user inputs investments as their option
            elif statement.__class__.__name__ == "InvestmentStatement":
                    #handle calulations for different types
                    self.year = self.eval_expr(statement.year)
                    self.rate = self.eval_expr(statement.rate)
                    self.amount = self.eval_expr(statement.amount)
                    #raises an error if the user does not input the year, rate, or the amount of money
                    if None in (self.year, self.rate, self.amount):
                        raise ValueError("Please enter values for your year, percentage rate, and the amount of money you would like!")
                    match statement.account_type:
                        case "Bonds":
                            print(Style.BRIGHT + f"Bonds are a type of investments there the investor lends money to the government or corporation, in return the buyer expects the money to allocate interest after a set time period." )
                            bonds_pro_con = self.pro_con_dict.get("CD")
                            print("Pros: ")
                            for pro in bonds_pro_con.get("Pros", []):
                                print(f"• {pro}")
                            print("Cons: ")
                            for con in bonds_pro_con.get("Cons", []):
                                print(f"• {con}")
                            print(f"Year(s) you have entered: " + str(self.year))
                            print(f"The percentage rate you have entered: " + str(self.rate))
                            print(f"The amount of money you have inputed: " + str(self.amount))
                            bondTotal = self.amount * (0.006) * self.year
                            print(f"The amount you have invest with Bonds:")
                            print(Fore.GREEN +str(bondTotal))
                            print(f"The amount you have invest in total with Bonds:")
                            print(Fore.GREEN +str(bondTotal + self.amount))
                        case "CD":
                            print(Style.BRIGHT + f"CD or certificate of deposit is a low-risk savings/interest product offered by banks and credit unions")
                            CD_pro_con = self.pro_con_dict.get("CD")
                            print("Pros: ")
                            for pro in CD_pro_con.get("Pros", []):
                                print(f"• {pro}")
                            print("Cons: ")
                            for con in CD_pro_con.get("Cons", []):
                                print(f"• {con}")
                            print(f"Year(s) you have entered: " + str(self.year))
                            print(f"The percentage rate you have entered: " + str(self.rate))
                            print(f"The amount of money you have inputed: " + str(self.amount))
                            apy = self.calc_apy(self.rate/100, 12) 
                            cd_total = self.amount * math.pow(1 + apy, self.year)
                            print(f"The amount you have saved with CDs:")
                            print(Fore.GREEN +str(cd_total))
                            print(f"The amount you have saved in total with CDs:")
                            print(Fore.GREEN +str(cd_total + self.amount))
                        case "Roth IRA":
                            print(Style.BRIGHT + f"Roth IRA is an individual retirement account, where you can contribute with after-tax dollars")
                            roth_ira_pro_con = self.pro_con_dict.get("Roth IRA")
                            print("Pros: ")
                            for pro in roth_ira_pro_con.get("Pros", []):
                                print(f"• {pro}")
                            print("Cons: ")
                            for con in roth_ira_pro_con.get("Cons", []):
                                print(f"• {con}")
                            print(f"Year(s) you have entered: " + str(self.year))
                            print(f"The percentage rate you have entered: " + str(self.rate))
                            print(f"The amount of money you have inputed: " + str(self.amount))
                            roth_IRA_total = self.amount * (((math.pow(1 + (self.rate / 100), self.year) - 1) / (self.rate / 100)) * (1 + (self.rate / 100)))
                            print(f"The estimated future value of your Roth IRA")
                            print(Fore.GREEN + str(roth_IRA_total))
            #calculates deposites and withdrawals and the total amount of money the user has inputed
            elif statement.__class__.__name__ == "DepositStatement":
                    self.amount = self.eval_expr(statement.amount) 
                    depositTotal = self.amount
                    self.depositTotal = depositTotal
                    print("Deposited Amount: " + Fore.GREEN + str(depositTotal))
            elif statement.__class__.__name__ == "WithdrawalStatement":
                    self.amount = self.eval_expr(statement.amount)
                    withdrawalTotal = self.amount
                    self.withdrawalTotal = withdrawalTotal
                    print("Withdrew Amount: " + Fore.RED + "-" + str(withdrawalTotal))
            elif statement.__class__.__name__ == "ShowStatement":
                    withdrawal = self.withdrawalTotal
                    deposited = self.depositTotal
                    if statement.show_str == "balance":
                        balance = deposited - withdrawal
                        print(f"Balance Total: " + str(balance))
                    else:
                        print(statement.show_str)
            #fizzbuzz, user can enter the strings and number values
            elif statement.__class__.__name__ == "FizzBuzzStatement":
                    self.num1 = self.eval_expr(statement.num1)
                    self.num2 = self.eval_expr(statement.num2)
                    self.fizz_str = self.eval_expr(statement.fizz_str)
                    self.buzz_str = self.eval_expr(statement.buzz_str)
                    for i in range(self.num1, (self.num2 + 1)):
                        if (i % 3 == 0 and i % 5 == 0):
                            print(self.fizz_str + self.buzz_str)
                        elif (i % 5 == 0):
                            print(self.buzz_str)
                        elif (i % 3 == 0):
                            print(self.fizz_str)
                        else:
                            print(i)

scriptMoney = scriptMoney()
scriptMoney.interpret(scriptMoney_model)
