import unittest
import datetime
import datetime
import calendar
from datetime import date
from dateutil.parser import parse


def get_days_in_month(month: date):
    """
    Get total numbers of days in a month.
    Args:
      month: date object value for the month.
    """
    return calendar.monthrange(month.year, month.month)


def _month_str_to_date(month: str) -> date:
    """
    Convert a month string to a date object.
    """
    return parse(month).date()


def monthly_charge(month, subscription, users):
    """Computes the monthly charge for a given subscription.

    @rtype: int
    @returns: the total monthly bill for the customer in cents, rounded
      to the nearest cent. For example, a bill of $20.00 should return 2000.
      If there are no active users or the subscription is None, returns 0.

    @type month: str
    @param month - Always present
      Has the following structure:
      "2022-04"  # April 2022 in YYYY-MM format

    @type subscription: dict
    @param subscription - May be None
      If present, has the following structure:
      {
        'id': 763,
        'customer_id': 328,
        'monthly_price_in_cents': 359  # price per active user per month
      }

    @type users: list
    @param users - May be empty, but not None
      Has the following structure:
      [
        {
          'id': 1,
          'name': "Employee #1",
          'customer_id': 1,

          # when this user started
          'activated_on': datetime.date(2021, 11, 4),

          # last day to bill for user
          # should bill up to and including this date
          # since user had some access on this date
          'deactivated_on': datetime.date(2022, 4, 10)
        },
        {
          'id': 2,
          'name': "Employee #2",
          'customer_id': 1,

          # when this user started
          'activated_on': datetime.date(2021, 12, 4),

          # hasn't been deactivated yet
          'deactivated_on': None
        },
      ]
    """
    # your code here!
    date_object = _month_str_to_date(month)
    month_start_date = first_day_of_month(date_object)
    month_end_date = last_day_of_month(date_object)

    # Refactor this to use Decimal object.
    total_cents = 0

    for user in users:
        if user.get("deactivated_on"):
            deactivated_date = user.get("deactivated_on") or month_end_date
            activation_start_date = max(
                user.get("activated_on", month_start_date), month_start_date
            )
            activation_end_date = max(deactivated_date, month_end_date)

            user_active_days = (activation_end_date - activation_start_date).days + 1

            monthly_subscription_price = subscription["monthly_price_in_cents"]
            _, month_total_days = get_days_in_month(date_object)

            print(monthly_subscription_price, month_total_days)

            daily_subscription_price = monthly_subscription_price / month_total_days

            total_cents += user_active_days * daily_subscription_price

            print(total_cents)

    return total_cents


####################
# Helper functions #
####################


def first_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the first day of that month. For example:

    >>> first_day_of_month(datetime.date(2022, 3, 17))  # Mar 17
    datetime.date(2022, 3, 1)                           # Mar  1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date.replace(day=1)


def last_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the last day of that month. For example:

    >>> last_day_of_month(datetime.date(2022, 3, 17))  # Mar 17
    datetime.date(2022, 3, 31)                         # Mar 31

    Input type: datetime.date
    Output type: datetime.date
    """
    last_day = calendar.monthrange(date.year, date.month)[1]
    return date.replace(day=last_day)


def next_day(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the next day. For example:

    >>> next_day(datetime.date(2022, 3, 17))   # Mar 17
    datetime.date(2022, 3, 18)                 # Mar 18

    >>> next_day(datetime.date(2022, 3, 31))  # Mar 31
    datetime.date(2022, 4, 1)                 # Apr  1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date + datetime.timedelta(days=1)


users = [
    {
        "id": 1,
        "name": "Employee #1",
        "activated_on": datetime.date(2019, 1, 1),
        "deactivated_on": None,
        "customer_id": 1,
    },
    {
        "id": 2,
        "name": "Employee #2",
        "activated_on": datetime.date(2019, 1, 1),
        "deactivated_on": None,
        "customer_id": 1,
    },
]

plan = {"id": 1, "customer_id": 1, "monthly_price_in_cents": 5_000}

no_users = []


# Note: the class must be called Test
class Test(unittest.TestCase):
    def test_works_when_no_users_are_active(self):
        self.assertEqual(monthly_charge("2018-10", plan, users), 0)

    def test_works_when_the_active_users_are_active_the_entire_month(self):
        expected_user_count = 2
        self.assertAlmostEqual(
            monthly_charge("2020-12", plan, users), expected_user_count * 5_000, delta=1
        )
