install.packages("orkg_0.1.0.zip")
library(orkg)
orkg <- ORKG(host="https://orkg.org/")
orkg$templates$materialize_template(template_id = "R12002")
tp = orkg$templates$list_templates()
df = read.csv('data.csv')
tt = t.test(df[['non.failing.heart..NF.']], 
             df[['failing.heart..F.']],
               var.equal=FALSE)
pvalue = tt$p.value
pvalue_ceil = ceiling(pvalue * 1000) / 1000.0

instance <- tp$students_ttest(
  label=paste('Statistically significant hypothesis test with IRE binding dependent variable on failing and non-failing hearts (p<',pvalue_ceil,')'), 
  has_dependent_variable='http://purl.obolibrary.org/obo/GO_0030350', # the study design dependent variable (iron-responsive element binding)
  has_specified_input='https://github.com/markusstocker/doi-10-1093-eurheartj-ehw333/blob/main/data.csv', # the input dataset ('df' WIP)
  has_specified_output=tp$pvalue(paste('the p-value of the statistical hypothesis test (p<',pvalue_ceil,')'), tp$scalar_value_specification(pvalue)),
)
instance$serialize_to_file('article.contribution.1.json', format='json-ld')