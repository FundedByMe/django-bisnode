
class MockBisnodeRatingReport(object):
    generalCompanyData = [{'ratingCode': 'AA',
                           'dateOfRating': '20140201',
                           'dateReg': '19561101'}]

    def __init__(self, rating=None):
        self.generalCompanyData[0]['ratingCode'] = rating


class MockBisnodeStandardReport(object):
    generalCompanyData = [{'ratingCode': 'AA',
                           'dateOfRating': '20140201',
                           'dateReg': '19561101',
                           'historyCode': 'AGE010',
                           'shareholdersCode': 'OWN030',
                           'financeCode': 'ECO020',
                           'abilityToPay1': 'PAY020',
                           'noOfEmployees1': '11',
                           'shareCapital': '00003000000'}]

    def __init__(self, rating=None, finances=None,
                 number_of_employees=None, share_capital=None):
        self.generalCompanyData[0]['ratingCode'] = rating
        self.generalCompanyData[0]['financeCode'] = finances
        self.generalCompanyData[0]['noOfEmployees1'] = str(number_of_employees)
        self.generalCompanyData[0]['shareCapital'] = str(share_capital.amount)
