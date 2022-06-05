.PHONY fix
fix:
	black ./ && flake8 ./ && isort ./