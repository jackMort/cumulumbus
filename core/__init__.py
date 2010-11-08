from cumulumbus.core.servicehook_pool import servicehook_pool
servicehook_pool.discover_services()
print servicehook_pool.get_servicehooks()
