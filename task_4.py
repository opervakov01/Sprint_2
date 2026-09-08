class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def from_hours(cls, name, hours, email=None):
        email = cls._get_email(name, email)
        return cls(name=name, hours=hours, email=email)

    @classmethod
    def from_rest_days(cls, name, rest_days, email=None):
        calculated_hours = (7 - rest_days) * 8
        email = cls._get_email(name, email)
        return cls(name=name, hours=calculated_hours, rest_days=rest_days, email=email)

    @staticmethod
    def _get_email(name, email=None):
        if email is not None:
            return email
        else:
            return f"{name}@email.com"

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        return self.hours * self.hourly_payment
