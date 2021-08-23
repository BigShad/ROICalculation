class Roi_calculation ():
    TAX_RATE = {
        "hawai":0.28,
        "alabama":0.41,
        "colorado":0.51,
        "louisiana":0.55,
        "district of columbia":0.56,
        "south carolina":0.57,
        "delaware":0.57,
        "west virginia":0.58,
        "nevada":0.60,
        "wyoming":0.61,
        "arkansas":0.62,
        "utah":0.63,
        "arizona":0.66,
        "idaho":0.69,
        "tenesse":0.71,
        "california":0.76,
        "new mexico":0.80,
        "mississippi":0.81,
        "virginia":0.82,
        "montana":0.84,
        "north carolina":0.84,
        "idiana":0.85,
        "kentucky":0.86,
        "florida":0.89,
        "oklahoma":0.90,
        "georgia":0.92,
        "missouri":0.97,
        "oregon":0.97,
        "north dakota":0.98,
        "washington":0.98,
        "maryland":1.09,
        "minnesota":1.12,
        "alaska":1.19,
        "massachusetts":1.23,
        "south dakota":1.31,
        "maine":1.36,
        "kansas":1.41,
        "michigan":1.54,
        "ohio":1.56,
        "iowa":1.57,
        "pennsylvenia":1.58,
        "rhode island":1.63,
        "new york":1.72,
        "nebraska":1.73,
        "texas":1.80,
        "wisconsin":1.90,
        "new jersey":2.49,
        "illinois":2.27,
        "new hampshire":2.18,
        "connecticut":2.14,
        "vermont":1.90,

    }
    INSURANCE = {
        "1":1485,
        "2":1723,
        "3":1971,
        "4":2169,
        "5":2830,
    }
    def income (self):
        self.rentalIncome = input("How much is Your montlhy rental income? ")
        self.poll = input("Do you have any other monthly sources of income?(yes/no) ")
        if self.poll == "yes":
            self.otherIncome = input("How much are your are your other sources of income?")
        else:
            self.otherIncome = 0
        self.totalIncome = int(self.rentalIncome) + int(self.otherIncome)
        print(f"Your total monhly income is {self.totalIncome}$")

    def Expenses (self):
        self.propertyValue = input("How much is the property? ")
        self.state = input("What state is the property located? ")
        for key,value in self.TAX_RATE.items():
            if self.state.lower() == key:
                self.tax = (int(self.propertyValue) * (int(value) / 100)) / 12
                print(f"Your anual tax is {self.tax * 12}$ and monthly tax payment is {self.tax}$")
        prompt = "what's your coverage amount?(to get average)\n-(1) for $100,000-$200,000.\n-(2) for $200,000-$300,000.\n-(3) for $300,000-$400,000.\n-(4) for $400,000-$500,000.\n-(5) for Greater than $500,000.\n-(6) to enter accurate amount.\n"
        self.coverage = input(prompt)
        if self.coverage == "6":
            self.insurance = input("What is your monthly insurance rate?")
        else:
            for key,value in self.INSURANCE.items():
                if self.coverage == key:
                    self.insurance = value / 12
                    print(f"Your average anual insurance is {self.insurance * 12}$ and monthly insurance rate {self.insurance}$")
        
        self.poll1 = input("Do you pay for utilities?(yes/no) ")
        if self.poll1 == 'yes':
            self.utilities = input('How much do you pay for all your monthly utilities? ')
        else:
            self.utilities = 0

        # self.opex =
        # self.capEx =
        self.propertyManager = int(self.rentalIncome) /10
        print(f"Your monthly property manager rate is {self.propertyManager}$ for the average being 10% of your rental income.")
        self.maintenance = input("How much do you spend for monthly maintnaince? ")
        print("Now let's calculate your monthly mortage payment.")
        self.loanBalance = input("What is the loan balance that needs to be paid off? ")
        self.loanYear = input("How many years will it take you to pay? ")
        self.loanInterest = input("What is the loan interest? ")
        self.interest = float(self.loanInterest) /100
        self.Mortage = float(self.loanBalance) * (float(self.interest) * ((1 + float(self.interest)) ** (float(self.loanYear) * 12))) / ((1 + float(self.interest)) ** (float(self.loanYear) * 12) - 1)
        print(f"Your monthly mortage payment is {self.Mortage}")
        self.totaExpenses = float(self.tax) + float(self.insurance) + float(self.propertyManager) + float(self.maintenance) + float(self.Mortage)
        print(f"Your total monthly expenses is {self.totaExpenses}$")

    def cashFlow (self):
        self.cFlow = int(self.totalIncome) - int(self.totaExpenses)
        if self.cFlow >= 0:
            print(f"Your monthly cash flow is {self.cFlow}$")
        else:
            print(f"Your have a negative monthly cash flow of {self.cFlow}$")

    def cashRoi (self):
        self.downPay = input("How much is the downpayment? ")
        self.closingCost = input("How much is the closing cost? ")
        self.rehabCost = input("How much did you spend for rehabilitation")
        self.cashOnCash = (int(self.cFlow) * 12) / (int(self.downPay) + int(self.closingCost) + int(self.rehabCost))
        print(f"Your anual cash on cash ROI is {self.cashOnCash}%")

         
        


p = Roi_calculation()
                                                                                                                                                 
p.income()
p.Expenses()
p.cashFlow()
p.cashRoi()
                        