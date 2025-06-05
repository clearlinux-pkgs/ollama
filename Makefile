PKG_NAME := ollama
URL = https://github.com/ollama/ollama/archive/refs/tags/v0.9.0.tar.gz
ARCHIVES =   $(CGIT_BASE_URL)/projects/ollama-vendor/snapshot/ollama-vendor-0.1.tar.gz ./

include ../common/Makefile.common
