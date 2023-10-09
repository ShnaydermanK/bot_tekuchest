from database_manager import DatabaseManager
from excel_writer import ExcelWriter
from tekuchest_calculator import TekuchestCalculator
import warnings
import logging
from DBQUERY import ssql_query_spisok_roTSS, ssql_query_spisok_ro, sql_query_all,ssql_query_spisok_op,ssql_query_all_udal,ssql_query_all_office

warnings.filterwarnings('ignore')

# Настройка логгирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
#
class StartHandler:
    def __init__(self, bot):
        self.bot = bot

    def handle(self, message):
        self.bot.reply_to(message, "Привет! Общие данные по Управлениям + список (/run) "
                                   " Данные по Управлениям - удаленные сотрудники /RunUdal, "
                                   " Данные по Управлениям - удаленные сотрудники /RunOffice ,"
                                   "Данные по РО (/tekuchest_ro)")
#
class HandlerFactory:
    def __init__(self, bot):
        self.bot = bot
        self.database_manager = DatabaseManager("192.168.23.19", "dashboard_db", "readonly_user", "readonly1q2w3e4R")
        self.excel_writer = ExcelWriter('merged_tables.xlsx')
        self.tekuchest_calculator = TekuchestCalculator(self.database_manager, self.excel_writer)


class TekuchestRoHandler(HandlerFactory):
    def handle(self, message):
        self.excel_writer = ExcelWriter('merged_tables_ro.xlsx')
        self.tekuchest_calculator = TekuchestCalculator(self.database_manager, self.excel_writer)



        spisok_ro = self.database_manager.execute_query(ssql_query_spisok_roTSS)['РО'].unique()

        for value in spisok_ro:
            ssql_query_spisok_ro_1 = ssql_query_spisok_ro.format(value[:10])

            value=value[:10]


            self.tekuchest_calculator.calculate_tekuchest(value, ssql_query_spisok_ro_1)


        self.excel_writer.save_and_close()
        self.database_manager.close_connection()

        # Отправка файла с результатом выполнения кода

        self.bot.send_document(message.chat.id, open('merged_tables_ro.xlsx', 'rb'))
        logger.info(f'{message.from_user.username} загрузил файл')

class RunCodeHandler(HandlerFactory):

    def handle(self, message):
        spisok_ry = ['Боденчук', 'Гузеева', 'Кочетков', 'Куклина', 'Шванова', 'Воронюк']

        for value in spisok_ry:
            sql_query_all_1=sql_query_all.format(value)

            ssql_query_spisok_op_1 = ssql_query_spisok_op.format(value)


            self.tekuchest_calculator.calculate_tekuchest(value, sql_query_all_1)
            df_op = self.database_manager.execute_query(ssql_query_spisok_op_1)
            df_op.to_excel(self.excel_writer.writer, sheet_name=value + ' список', index=False)

        self.excel_writer.save_and_close()
        self.database_manager.close_connection()

        # Отправка файла с результатом выполнения кода
        self.bot.send_document(message.chat.id, open('merged_tables.xlsx', 'rb'))
        logger.info(f'{message.from_user.username} загрузил файл')

class RunUdalHandler(HandlerFactory):
    def handle(self, message):
        self.excel_writer = ExcelWriter('merged_tables_udal.xlsx')
        self.tekuchest_calculator = TekuchestCalculator(self.database_manager, self.excel_writer)
        spisok_ry = ['Боденчук', 'Гузеева', 'Кочетков', 'Куклина', 'Шванова', 'Воронюк']
        for value in spisok_ry:
            ssql_query_all_udal_1=ssql_query_all_udal.format(value)


            self.tekuchest_calculator.calculate_tekuchest(value, ssql_query_all_udal_1)


        self.excel_writer.save_and_close()
        self.database_manager.close_connection()

        # Отправка файла с результатом выполнения кода
        self.bot.send_document(message.chat.id, open('merged_tables_udal.xlsx', 'rb'))
        logger.info(f'{message.from_user.username} загрузил файл')

class RunOfficelHandler(HandlerFactory):
    def handle(self, message):
        self.excel_writer = ExcelWriter('merged_tables_office.xlsx')
        self.tekuchest_calculator = TekuchestCalculator(self.database_manager, self.excel_writer)
        spisok_ry = ['Боденчук', 'Гузеева', 'Кочетков', 'Куклина', 'Шванова', 'Воронюк']
        for value in spisok_ry:
            ssql_query_all_office_1=ssql_query_all_office.format(value)


            self.tekuchest_calculator.calculate_tekuchest(value, ssql_query_all_office_1)


        self.excel_writer.save_and_close()
        self.database_manager.close_connection()

        # Отправка файла с результатом выполнения кода
        self.bot.send_document(message.chat.id, open('merged_tables_office.xlsx', 'rb'))
        logger.info(f'{message.from_user.username} загрузил файл')


