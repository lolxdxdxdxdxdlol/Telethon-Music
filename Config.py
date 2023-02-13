import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6022338196:AAHsrG0yXNIdeF9CKRidw5wk_UVnb57Is2w")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AQG6Gi0AD3Dw3s2Bu_p6xe9EzSO8naqW5RZ_MxJjS_7D1t_PKb_eUvitWQHjAaB0cCADwPmmtDaQHU7NeoufLx0phnTqqbagj9okJIvtn-4lRQzi4nOAu6HzCmDvIv67vLbu84fcRBFxZKFqJzpboU_N_iM267mX99JSjL98efM0TVM2LYDerwrq2ZGZABR_dGEJjqhuUc03cFa7S6CNROTIKLw5v9vbWOHC-4fhBM429-o2p68tOHzR0Tslg_RXKP-P9VzfKE_Y2D-vDJd_M58xrr_MjjQ5WqZt72sImkJ-rlqBsntzTvagyO9H_DbArB5lc6VCYMlHe9j85_xA7d3EvUt1dwAAAAFOyY7PAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@vvv")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "100")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
