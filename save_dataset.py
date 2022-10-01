from multiprocessing import resource_sharer
from orkg import ORKG

orkg = ORKG(host='https://orkg.org')

id = orkg.resources.save_dataset(file='data.csv', label='Summary data showing iron-responsive element (IRE) binding activity in LV tissue samples', dimensions=[]).content['id']

print(id)

