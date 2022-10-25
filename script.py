from math import ceil
import pandas as pd
from orkg import ORKG
from scipy.stats import ttest_ind

orkg = ORKG(host='https://sandbox.orkg.org')
orkg.templates.materialize_templates(['R12002', 'R12006', 'R12008'], verbose=False)
tp = orkg.templates

df = pd.read_csv('data.csv') 
tt = ttest_ind(df['non-failing heart (NF)'], 
               df['failing heart (F)'], 
               equal_var=False, nan_policy='omit')
pvalue = tt.pvalue
pvalue_ceil = ceil(pvalue * 1000) / 1000.0
pvalue_str = '{:.16f}'.format(pvalue)

tp.students_ttest(
  label='Statistically significant hypothesis test with IRE binding dependent variable on failing and non-failing hearts (p<{})'.format(pvalue_ceil), 
  has_dependent_variable='http://purl.obolibrary.org/obo/GO_0030350', # the study design dependent variable (iron-responsive element binding)
  has_specified_input=(df, 'Summary data showing iron-responsive element (IRE) binding activity in LV tissue samples'), # the input dataset
  has_specified_output=tp.pvalue('the p-value of the statistical hypothesis test (p<{})'.format(pvalue_ceil), 
    tp.scalar_value_specification('{}'.format(pvalue_str), pvalue_str)
  ),
).serialize_to_file('article.contribution.1.json', format='json-ld')
