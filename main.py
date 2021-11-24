loan_amount = float(input("Введите размер кредита (желаемая сумма ДС): "))
loan_rate = float(input("Введите процентную ставку по кредиту (процент годовых): "))
# Вычисляем месячный процент начислений, средств, соответствующий указанному годовому %
monthly_deduction_rate = (1 + loan_rate / 100) ** (1 / 12) - 1
monthly_loan_payment = float(input("Введите желаемый ежемесяцный платеж: "))
if monthly_loan_payment < loan_amount * monthly_deduction_rate:
    print("Кредит не может быть выдан. Размер платежа должен погашать начисления % по кредиту.")
else:
    print("Кредит может быть выдан на следующих условиях:")
    remaining_debt = loan_amount
    loan_months = 0
    interest_charges = payment = debt_decrease = 0
    overall_loan_price = 0
    print()
    labels = ("month".rjust(8), "remaining debt".rjust(15), "charges".rjust(15),
              "debt decrease".rjust(15), "payment".rjust(15))
    print(*labels)  # над таблицей выводим заголовки столбцов
    print('-' * (8 + 15 * 4 + 4))  # и черту соответствующей длины
    print(f'{loan_months:8} {remaining_debt:15.2f} {interest_charges:15.2f}',
          f'{debt_decrease:15.2f} {payment:15.2f}')  # момент взятия кредита
    while remaining_debt > 0.01:  # пока долг больше одной копейки
        loan_months += 1  # +1 месяц расчета
        # Вычисляем размер начисленных процентов по кредиту
        interest_charges = remaining_debt * monthly_deduction_rate
        # Вычисляем чему должен быть равен платеж в этом месяце
        if monthly_loan_payment > remaining_debt + interest_charges:
            payment = remaining_debt + interest_charges
        else:
            payment = monthly_loan_payment
        # вычисляем размер погашения основной части долга
        debt_decrease = payment - interest_charges
        remaining_debt -= debt_decrease
        # параллельно суммируем общий объем выплат по кредиту
        overall_loan_price += payment
        # выводим все рассчитанные значения в очередную строку таблицы
        print(f'{loan_months:8} {remaining_debt:15.2f} {interest_charges:15.2f}',
              f'{debt_decrease:15.2f} {payment:15.2f}')
    print("Месяцев на погашение кредита: ", loan_months)
    print("Полная стоимость кредита: ", f'{overall_loan_price:0.2f}')

