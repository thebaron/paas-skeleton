check-paas-skeleton-env: $(PROJECT_HOME_DIR)/etc/project-environment.sh $(PROJECT_HOME_DIR)/etc/environment.d/*
ifndef PROJECT_HOME_DIR
	$(error PROJECT_HOME_DIR environment variable is undefined, did you source env.sh?)
endif

.PHONY: clean-build
clean-build:
        if [[ "x$(PROJECT_HOME_DIR)x" != "xx" ]]; then rm -rf $(PROJECT_HOME_DIR)/build; fi
