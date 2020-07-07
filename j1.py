import jenkins
server = jenkins.Jenkins('http://localhost:8080', username='Tejaswini', password='Teju@407')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))


'''server = jenkins.Jenkins('http://localhost:8080')
print (server.jobs_count())
'''
server.create_job('empty2', jenkins.EMPTY_CONFIG_XML)
jobs = server.get_jobs()
print (jobs)
#my_job = server.get_job_config('cool-job')
#print(my_job) # prints XML configuration
server.build_job('empty2')
server.disable_job('empty2')
server.copy_job('empty2', 'empty2_copy')
server.enable_job('empty2_copy')
server.reconfig_job('empty2_copy', jenkins.RECONFIG_XML)

server.delete_job('empty2')
server.delete_job('empty2_copy')
'''
# build a parameterized job
# requires creating and configuring the api-test job to accept 'param1' & 'param2'
server.build_job('api-test', {'param1': 'test value 1', 'param2': 'test value 2'})
last_build_number = server.get_job_info('api-test')['lastCompletedBuild']['number']
build_info = server.get_build_info('api-test', last_build_number)
print (build_info)'''

# get all jobs from the specific view
jobs = server.get_jobs(view_name='View Name')
print (jobs)

server.create_view('EMPTY', jenkins.EMPTY_VIEW_CONFIG_XML)
view_config = server.get_view_config('EMPTY')
views = server.get_views()
server.delete_view('EMPTY')
print (views)
