# makefile for Shard of Humanity

clean:
	@echo -e '  [ \e[1;31mSOH_MAKE\e[m ] Cleaning up...'
	@echo -e '  [ \e[1;31mSOH_MAKE\e[m ] Removing cache at src...'

	@rm -rf src/*.rpyc
	@rm -rf src/screens/*.rpyc
	@rm -rf src/scripts/*.rpyc
	@rm -rf src/resources/*.rpyc

	@echo -e '  [ \e[1;31mSOH_MAKE\e[m ] Cleanup completed'
