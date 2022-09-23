from math import ceil
import pandas as pd
from orkg import ORKG
from scipy.stats import ttest_ind

orkg = ORKG(host='https://orkg.org/orkg')
orkg.templates.materialize_templates(['R12002', 'R12006', 'R12008'])
tp = orkg.templates

df = pd.read_csv('data.csv') 
tt = ttest_ind(df['non-failing heart (NF)'], 
               df['failing heart (F)'], 
               equal_var=False, nan_policy='omit')
pvalue = tt.pvalue
pvalue_ceil = ceil(pvalue * 1000) / 1000.0

tp.students_ttest(
  'Statistically significant hypothesis test with IRE binding dependent variable on failing and non-failing hearts (p<{})'.format(pvalue_ceil),
  'http://purl.obolibrary.org/obo/GO_0030350', # the study design dependent variable
  tp.pvalue('the p-value of the statistical hypothesis test (p<{})'.format(pvalue_ceil), tp.scalar_value_specification(pvalue)),
  'https://github.com/markusstocker/doi-10-1093-eurheartj-ehw333/blob/main/data.csv', # the input dataset ('df' WIP)
).serialize_to_file('article.contribution.1.json', format='json-ld')
