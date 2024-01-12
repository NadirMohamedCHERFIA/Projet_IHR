import re
USERNAME = 'admin'
HASHED_PASSWORD = b'$2b$12$vqtcGu1yQFxmt2RmqyrVpuVA5M12mA/H9zTtCUBoilDSWAst6st1y'

# colors
bgColor = '#0A1045'
whiteColor = "#F2F2F2"
dangerColor = '#F25757'
successColor = '#10FFCB'
secondaryColor = '#E0E2DB'
alertColor = '#E6AF2E'
primaryColor = '#2176FF'


# font
font_var = 'Poppins'
font_configuration_lg = (font_var, 18, 'bold')
font_configuration_md = (font_var, 14, 'bold')


IP = "10.3.141.80"
PORT = 1025

dimensions = "1200x750"


buttons_width = 40
entries_width = 60

selected_theme = 'darkly'
selected_theme_label = 'Dark theme'

ip_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
