import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

class TekuchestCalculator:
    def __init__(self, database_manager, excel_writer):
        self.database_manager = database_manager
        self.excel_writer = excel_writer

    def calculate_tekuchest(self, value, query):
        df = self.database_manager.execute_query(query)
        df['date_uval'] = pd.to_datetime(df['date_uval'])
        df['first_date'] = pd.to_datetime(df['first_date'])
        # Получаем текущую дату
        now = datetime.datetime.now()

        # Получаем первый день прошлого месяца
        previous_month_start = now - relativedelta(months=4)
        previous_month_start = previous_month_start.replace(day=1)

        # Получаем первый день следующего месяца
        next_month_start = now + relativedelta(months=2)
        next_month_start = next_month_start.replace(day=1)

        # Создаем список всех дат прошлого месяца
        dates = pd.date_range(start=previous_month_start, end=next_month_start, freq='D')

        # Преобразуем каждую дату в формат без времени
        dates = [date.date() for date in dates]

        # Создаем DataFrame с указанными датами в качестве столбцов
        employees_count = pd.DataFrame({'Date': dates})
        employees_free = pd.DataFrame({'Date': dates})

        # Выводим получившийся DataFrame
        employees_count['Date'] = pd.to_datetime(employees_count['Date'])
        employees_free['Date'] = pd.to_datetime(employees_free['Date'])

        def count_employees_on_date(date, df):
            return len(df[(df['first_date'] <= date)])

        employees_count['employees_count'] = employees_count['Date'].apply(lambda x: count_employees_on_date(x, df))

        def count_employees_free_on_date(date, df):
            return len(df[(df['date_uval'] <= date)])

        employees_free['employees_count'] = employees_free['Date'].apply(lambda x: count_employees_free_on_date(x, df))

        employees = pd.merge(employees_count, employees_free, on="Date", how='left')
        employees['employees_life'] = employees['employees_count_x'] - employees['employees_count_y']
        employees['Month'] = employees['Date'].dt.month
        mean_spisoch_employees = employees.groupby(['Month'], as_index=False)['employees_life'].mean()
        all_free_month = employees.groupby(['Month'], as_index=False)['employees_count_y'].max()

        tekuchest = pd.merge(mean_spisoch_employees, all_free_month, on='Month', how='left')
        tekuchest['%Текучести'] = tekuchest['employees_count_y'] / tekuchest['employees_life']
        tekuchest = tekuchest.rename(
            columns={'Month': 'Месяц', 'employees_life': 'Среднесписочная чис', 'employees_count_y': 'Уволенных'})

        tekuchest['Разница Уволенных'] = tekuchest['Уволенных'].diff().fillna(tekuchest.loc[0, 'Уволенных'])
        tekuchest['Текучесть'] = tekuchest['Разница Уволенных'] / tekuchest['Среднесписочная чис']
        tekuchest = tekuchest[['Месяц', 'Среднесписочная чис', 'Разница Уволенных', 'Текучесть']].rename(
            columns={'Разница Уволенных': 'Уволено'})

        # Остальной код по расчету текучести...

        # Запись таблицы в файл Excel с названием файла в ячейке
        tekuchest.to_excel(self.excel_writer.writer, sheet_name=value, index=False)
