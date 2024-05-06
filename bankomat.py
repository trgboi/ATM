# У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять этой картой, выполняя следующие операции, 
# для выполнения которых необходимо написать следующие функции:
# check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
# deposit(amount): Пополнение счёта.
# withdraw(amount): Снятие денег.
# exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.
# Пополнение счета:
# Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму. Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.
# Снятие средств:
# Функция withdraw(amount) позволяет клиенту снимать средства со счета. Сумма снятия также должна быть кратной MULTIPLICITY. 
# При снятии средств начисляется комиссия в процентах от снимаемой суммы, которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.
# Завершение работы:
# Функция exit() завершает работу с банковским счетом. Перед завершением, если на счету больше RICHNESS_SUM, начисляется налог на богатство в размере RICHNESS_PERCENT процентов.
# Проверка кратности суммы:
# Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY. 
# Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.
from decimal import Decimal, getcontext

# Точность вычислений
getcontext().prec = 2

# Константы для работы с банковским счетом
MULTIPLICITY = Decimal('100')  # Кратность суммы
MIN_REMOVAL = Decimal('0.05')  # Минимальная комиссия
MAX_REMOVAL = Decimal('0.1')   # Максимальная комиссия
RICHNESS_SUM = Decimal('10000')  # Сумма для налога на богатство
RICHNESS_PERCENT = Decimal('0.01')  # Процент налога на богатство


class BankAccount:
    def __init__(self):
        self.balance = Decimal('0')
        self.operations = []

    def check_multiplicity(self, amount):
        return amount % MULTIPLICITY == 0

    def deposit(self, amount):
        if self.check_multiplicity(amount):
            self.balance += amount
            self.operations.append(f"Пополнение: +{amount}")
        else:
            print("Сумма должна быть кратна 100")

    def withdraw(self, amount):
        if self.check_multiplicity(amount) and amount <= self.balance:
            commission = amount * MIN_REMOVAL if amount < RICHNESS_SUM else amount * MAX_REMOVAL
            self.balance -= amount + commission
            self.operations.append(f"Снятие: -{amount}, комиссия: {commission}")
        else:
            print("Недостаточно средств или сумма не кратна 100")

    def exit(self):
        if self.balance > RICHNESS_SUM:
            tax = self.balance * RICHNESS_PERCENT
            self.balance -= tax
            self.operations.append(f"Налог на богатство: -{tax}")
        print(f"Итоговый баланс: {self.balance}")
        print("Операции по счету:")
        for operation in self.operations:
            print(operation)


if __name__ == '__main__':
    
    account = BankAccount()
    account.deposit(Decimal('500'))
    account.withdraw(Decimal('300'))
    account.exit()
        
