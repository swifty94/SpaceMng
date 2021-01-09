import time
#
#	User-specific constants
#
# 	Define path to logs folder and number of days here
#

#   FOLDER = 'E:/FTACS5/standalone/log/'
FOLDER = '/path/to/acs/log/'

#   If log older than DAYS_COUNT > remove it
DAYS_COUNT = 30

# Dont touch this !
OLD = time.time() - (DAYS_COUNT * 24 * 60 * 60)