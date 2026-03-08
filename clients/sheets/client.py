import datetime

import gspread
from django.conf import settings
from google.oauth2.service_account import Credentials

from clients.sheets.dto import NewProductData


class SpreadsheetClient:
    def __init__(self, ):
        self.service_account_file = settings.SERVICE_ACCOUNT_FILE
        scopes = ['https://www.googleapis.com/auth/spreadsheets']
        credentials = Credentials.from_service_account_file(self.service_account_file, scopes=scopes)
        self.client = gspread.authorize(credentials)
        self._init_spreadsheets_id()

    def _init_spreadsheets_id(self):
        self.product_id = settings.SPREADSHEET_PRODUCT_ID

    def create_product_row(self, data: NewProductData):
        sheet = self.client.open_by_key(self.product_id).worksheet("Лист1")
        sheet.append_row(
            [
                f'{datetime.datetime.now()}',
                f'{data.source}',
                f'{data.bought_products}',
                f'{data.city}',
                f'{data.age}',
                f'{data.specialization}',
                f'{data.income_rub}',
                f'{data.operations_status}',
                f'{data.study_goal}',
                f'{data.current_difficulties}',
                f'{data.attempted_solutions}',
                f'{data.subscription_info}',
                f'{data.top_questions}',
                f'{data.warmup_level}',
                f'{data.workload_level}',
                f'{data.full_name}',
                f'{data.instagram}',
                f'{data.telegram_channel}',
                f'{data.telegram}',
                f'{data.phone}',
                f'{data.email}',
                f'{data.policy_agreement}',
            ]
        )
