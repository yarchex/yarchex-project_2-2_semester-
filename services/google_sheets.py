import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config.settings import settings
from utils.logger import logger

class GoogleSheetsExporter:
    def __init__(self):
        scope = ["https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(
            settings.GOOGLE_CREDS_JSON, scope)
        self.client = gspread.authorize(creds)

    async def export_order(self, order_data: dict):
        try:
            sheet = self.client.open("Poizon Orders").sheet1
            sheet.append_row([
                order_data["order_id"],
                order_data["user_id"],
                order_data["item_name"],
                order_data["price"]
            ])
        except Exception as e:
            logger.error(f"Google Sheets export error: {e}")
            raise
