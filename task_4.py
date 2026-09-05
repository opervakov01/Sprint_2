class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours=None, rest_days=None, email=None):
        if hours is not None:
            return hours
        elif rest_days is not None:
            calculated_hours = (7 - rest_days) * 8
            return calculated_hours
        else:
            raise ValueError("Недостаточно данных для расчёта часов: укажите либо hours, либо rest_days")

    @classmethod
    def get_email(cls, name, email=None):
        if email is not None:
            return email
        else:
            generated_email = f"{name}@email.com"
            return generated_email

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        
        if self.hours is None:
            self.hours = self.get_hours(self.name, self.hours, self.rest_days, self.email)       
        if self.email is None:
            self.email = self.get_email(self.name, self.email) 
        return self.hours * self.hourly_payment
