import os 


BASE_DIR2 = os.path.dirname((os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR2,'blog_site\\blog')

print(TEMPLATES_DIR,os.listdir())