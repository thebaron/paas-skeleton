# .paas-skeleton/elasticsearch/makefile.inc
# TODO: make this complain if VE_ROOT isn't set
ELASTICSEARCH_URL := https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.90.7.tar.gz
ELASTICSEARCH_ROOT := $(VE_ROOT)/share/elasticsearch

$(ELASTICSEARCH_ROOT): $(VE_ROOT)
	if [ ! -d $(ELASTICSEARCH_ROOT) ]; then mkdir -p $(VE_ROOT)/share/; curl $(ELASTICSEARCH_URL) -so - | tar -zxvC $(VE_ROOT)/share/; mv $(VE_ROOT)/share/elasticsearch-* $(ELASTICSEARCH_ROOT); ln -s $(ELASTICSEARCH_ROOT)/bin/elasticsearch $(VE_ROOT)/bin/elasticsearch; fi
