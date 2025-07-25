import os
from dotenv import load_dotenv

load_dotenv()

ORANGEHRM_URL = os.getenv("ORANGEHRM_URL", "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
VALID_USERNAME = os.getenv("VALID_USERNAME", "Admin")
VALID_PASSWORD = os.getenv("VALID_PASSWORD", "admin123")
INVALID_USERNAME = os.getenv("INVALID_USERNAME", "invalid_user")
INVALID_PASSWORD = os.getenv("INVALID_PASSWORD", "invalid_pass") 