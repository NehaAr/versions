# first line: 1
def autosave(file):
  get_ipython().system('mv file /content/versions')
  get_ipython().system('git add .')
  get_ipython().system('git commit -m "New Version Added"')
  get_ipython().system('git push origin main')
