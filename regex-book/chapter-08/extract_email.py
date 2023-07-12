import re

'''
Extract Email IDs with Regex:
- A big file is read with numerous email IDs
- Task is to extract all
'''
my_file = 'Post queries at markzuck@meta.org or call out tesla boy elonmusk@spacex.com '\
            'You can also reach the professor at thedoctor@co.uk.gov'
email_list = re.findall(r'\S+@\S+', my_file)
print('The email IDs are:', email_list)
