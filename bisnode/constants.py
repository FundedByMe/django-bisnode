COMPANY_STANDARD_REPORT = "NRGCompanyReportStandard"
COMPANY_RATING_REPORT = "NRGCompanyReportRating"

HIGH = 'AAA'
GOOD = 'AA'
WORTHY = 'A'
NEW = 'AN'
BELOW_AVERAGE = 'B'
BAD = 'C'
MISSING = '-'

RATING_CHOICES = (
    (HIGH, "Highest credit worthiness"),
    (GOOD, "Good credit worthiness"),
    (WORTHY, "Credit worthy"),
    (NEW, "New company"),
    (BELOW_AVERAGE, "Credit with safety measurements"),
    (BAD, "Credit advised against"),
    (MISSING, "Rating not applicable"),
)


WELL_ESTABLISHED = 'AGE010'
ESTABLISHED = 'AGE020'
SMALLER_SCALE = 'AGE030'
LESS_THAN_TWO_YEARS = 'AGE040'

OPERATION_CHOICES = (
    (WELL_ESTABLISHED, 'Well-established'),
    (ESTABLISHED, 'Established'),
    (SMALLER_SCALE, '2–4 years'),
    (LESS_THAN_TWO_YEARS, 'Less than two years'),
)

OPERATION_CHOICES_DICT = dict(OPERATION_CHOICES)


SATISFACTORY = 'OWN030'
NOTES_ON_RECORD = 'OWN100'
NEGATIVE_ON_RECORD = 'OWN040'
CURRENT_NEGATIVE = 'OWN050'
NEGATIVE_GROUP = 'OWN090'
INCOMPLETE = 'OWN080'

MANAGEMENT_CHOICES = (
    (SATISFACTORY, 'Satisfactory'),
    (NOTES_ON_RECORD, 'Notes on record'),
    (NEGATIVE_ON_RECORD, 'Negative info on record'),
    (NEGATIVE_GROUP, 'Negative info – group'),
    (CURRENT_NEGATIVE, 'Current negative info'),
    (INCOMPLETE, 'Incomplete')
)

MANAGEMENT_CHOICES_DICT = dict(MANAGEMENT_CHOICES)


VERY_GOOD_FINANCES = 'ECO010'
GOOD_FINANCES = 'ECO020'
SATISFACTORY_FINANCES = 'ECO030'
UNSATISFACTORY_FINANCES = 'ECO040'
WEAK_FINANCES = 'ECO050'
SEE_SPECIFICATIONS = 'ECO060'
NOT_UPDATED = 'ECO070'
NOT_UPDATED2 = 'ECO090'
NOT_UPDATED3 = 'ECO100'
UNAVAILABLE = 'ECO110'

FINANCES_CHOICES = (
    (VERY_GOOD_FINANCES, 'Very good'),
    (GOOD_FINANCES, 'Good'),
    (SATISFACTORY_FINANCES, 'Satisfactory'),
    (UNSATISFACTORY_FINANCES, 'Unsatisfactory'),
    (WEAK_FINANCES, 'Weak'),
    (SEE_SPECIFICATIONS, 'See financial specifications'),
    (NOT_UPDATED, 'Annual accounts not updated'),
    (NOT_UPDATED2, 'Annual accounts not updated'),
    (NOT_UPDATED3, 'Annual accounts not updated'),
    (UNAVAILABLE, 'Annual accounts unavailable')
)

FINANCES_CHOICES_DICT = dict(FINANCES_CHOICES)


VERY_GOOD_SOLVENCY = 'PAY010'
VERY_GOOD_NOTES_ON_RECORD = 'PAY020'
GOOD_SOLVENCY = 'PAY030'
GOOD_NOTES_ON_RECORD = 'PAY040'
SATISFACTORY_SOLVENCY = 'PAY050'
SATISFACTORY_NOTES_ON_RECORD = 'PAY060'
UNSATISFACTORY_SOLVENCY = 'PAY070'
WEAK_SOLVENCY = 'PAY080'
VERY_WEAK_SOLVENCY = 'PAY090'

SOLVENCY_CHOICES = (
    (VERY_GOOD_SOLVENCY, 'Very good'),
    (VERY_GOOD_NOTES_ON_RECORD, 'Very good – notes on record'),
    (GOOD_SOLVENCY, 'Good'),
    (GOOD_NOTES_ON_RECORD, 'Good – notes on record'),
    (SATISFACTORY_SOLVENCY, 'Satisfactory'),
    (SATISFACTORY_NOTES_ON_RECORD, 'Satisfactory – notes on record'),
    (UNSATISFACTORY_SOLVENCY, 'Unsatisfactory'),
    (WEAK_SOLVENCY, 'Weak'),
    (VERY_WEAK_SOLVENCY, 'Very weak'),
)

SOLVENCY_CHOICES_DICT = dict(SOLVENCY_CHOICES)
