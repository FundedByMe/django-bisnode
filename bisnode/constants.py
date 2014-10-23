from django.utils.translation import ugettext_lazy as _

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
    (HIGH, _("Highest credit worthiness")),
    (GOOD, _("Good credit worthiness")),
    (WORTHY, _("Credit worthy")),
    (NEW, _("New company")),
    (BELOW_AVERAGE, _("Credit with safety measurements")),
    (BAD, _("Credit advised against")),
    (MISSING, _("Rating not applicable")),
)


WELL_ESTABLISHED = 'AGE010'
ESTABLISHED = 'AGE020'
SMALLER_SCALE = 'AGE030'
LESS_THAN_TWO_YEARS = 'AGE040'

OPERATION_CHOICES = (
    (WELL_ESTABLISHED, _('Well-established')),
    (ESTABLISHED, _('Established')),
    (SMALLER_SCALE, _('2-4 years')),
    (LESS_THAN_TWO_YEARS, _('Less than two years')),
)

OPERATION_CHOICES_DICT = dict(OPERATION_CHOICES)


SATISFACTORY = 'OWN030'
NOTES_ON_RECORD = 'OWN100'
NEGATIVE_ON_RECORD = 'OWN040'
CURRENT_NEGATIVE = 'OWN050'
NEGATIVE_GROUP = 'OWN090'
INCOMPLETE = 'OWN080'

MANAGEMENT_CHOICES = (
    (SATISFACTORY, _('Satisfactory')),
    (NOTES_ON_RECORD, _('Notes on record')),
    (NEGATIVE_ON_RECORD, _('Negative info on record')),
    (NEGATIVE_GROUP, _('Negative info - group')),
    (CURRENT_NEGATIVE, _('Current negative info')),
    (INCOMPLETE, _('Incomplete'))
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
    (VERY_GOOD_FINANCES, _('Very good')),
    (GOOD_FINANCES, _('Good')),
    (SATISFACTORY_FINANCES, _('Satisfactory')),
    (UNSATISFACTORY_FINANCES, _('Unsatisfactory')),
    (WEAK_FINANCES, _('Weak')),
    (SEE_SPECIFICATIONS, _('See financial specifications')),
    (NOT_UPDATED, _('Annual accounts not updated')),
    (NOT_UPDATED2, _('Annual accounts not updated')),
    (NOT_UPDATED3, _('Annual accounts not updated')),
    (UNAVAILABLE, _('Annual accounts unavailable'))
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
    (VERY_GOOD_SOLVENCY, _('Very good')),
    (VERY_GOOD_NOTES_ON_RECORD, _('Very good - notes on record')),
    (GOOD_SOLVENCY, _('Good')),
    (GOOD_NOTES_ON_RECORD, _('Good - notes on record')),
    (SATISFACTORY_SOLVENCY, _('Satisfactory')),
    (SATISFACTORY_NOTES_ON_RECORD, _('Satisfactory - notes on record')),
    (UNSATISFACTORY_SOLVENCY, _('Unsatisfactory')),
    (WEAK_SOLVENCY, _('Weak')),
    (VERY_WEAK_SOLVENCY, _('Very weak')),
)

SOLVENCY_CHOICES_DICT = dict(SOLVENCY_CHOICES)
