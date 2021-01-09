import os, shutil
import logging
from logging import config
from settings import FOLDER, DAYS_COUNT, OLD

logging.config.fileConfig('logging.ini', disable_existing_loggers=False)

class ACSLogHandler(object):
	
	@classmethod
	def remove_old_log(cls,FOLDER,DAYS_COUT,OLD):
		"""
		:Accepting: FOLDER,DAYS_COUT,OLD constants from settings \n
		:Return: None
		"""
		for filename in os.listdir(FOLDER):
			try:
				file_path = os.path.join(FOLDER, filename)
				creation_time = os.stat(file_path).st_ctime		
				if os.path.isfile(file_path) or os.path.islink(file_path):
					if creation_time >= OLD:
						logging.info(f"[{__class__.__name__}]->[MATCH/Removed]->[Filename]->[{filename}]")				
						os.remove(file_path)						
				elif os.path.isdir(file_path):
					if creation_time >= OLD:
						logging.info(f"[{__class__.__name__}]->[MATCH/Removed]->[Directory]->[{filename}]")
						shutil.rmtree(file_path)						
			except Exception as e:		
				logging.info(f"[{__class__.__name__}]->[FAILED Delete][{filename}] \n Exception: {e}",exc_info=1)
				logging.info()		

if __name__ == "__main__":
	mng = ACSLogHandler()
	mng.remove_old_log(FOLDER,DAYS_COUNT,OLD)