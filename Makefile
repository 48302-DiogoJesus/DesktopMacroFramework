reqs:
	pipreqs --force DesktopAutomationFramework && mv DesktopAutomationFramework/requirements.txt . 

install:
	pip install --upgrade --force-reinstall . && rm -rf build && rm -rf DesktopAutomationFramework.egg-info
