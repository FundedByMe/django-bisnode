
class MockBisnodeRatingReport(object):
    generalCompanyData = [{'ratingCode': 'AA',
                           'dateOfRating': '20140201'}]

    def __init__(self, rating=None):
        self.generalCompanyData[0]['ratingCode'] = rating
