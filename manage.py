import sys
import os
sys.path.append("/private/var/mobile/Containers/Shared/AppGroup/BF6D28F7-8CDD-43FE-AAB3-F1369C817B0C/File Provider Storage/Repositories/test")

if __name__ == "__main__":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "takuya.settings")
	try:
		from django.core.management import execute_from_command_line
	except ImportError as exc:
		raise ImportError("Couldn't import Django. Are you sure it's installed??") from exc
	execute_from_command_line(sys.argv)
