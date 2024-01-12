import re
USERNAME = 'admin'
HASHED_PASSWORD = b'$2b$12$vqtcGu1yQFxmt2RmqyrVpuVA5M12mA/H9zTtCUBoilDSWAst6st1y'

IP = "10.3.141.80"
PORT = 1025

dimensions = "1200x750"

font_var = 'Poppins'

buttons_width = 40
entries_width = 60

selected_theme = 'darkly'
selected_theme_label = 'Dark theme'

ip_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
