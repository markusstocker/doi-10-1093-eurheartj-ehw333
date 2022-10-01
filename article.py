from orkg import ORKG

paper = {
    "predicates":[],
    "paper":{
        "doi":"10.1093/eurheartj/ehw333",
		"researchField":"R132",
		"title":"Iron-regulatory proteins secure iron availability in cardiomyocytes to prevent heart failure",
        "contributions":[
	    {
			"name": "Statistically significant hypothesis test with IRE binding dependent variable on failing and non-failing hearts (p<0.001)",
			"classes": [
            	"C1007"
        	],
			"values": {
				"P4003": [
					{
						"classes": [
							"C1003"
						],
						"values": {
							"P9003": [
								{
									"classes": [
										"C1004"
									],
									"values": {
										"P9004": [
											{
												"text": "0.0000000131112475"
											}
										]
									},
									"label": "0.0000000131112475"
								}
							]
						},
						"label": "the p-value of the statistical hypothesis test (p<0.001)"
					}
				],
				"P27011": [
					{
						"text": "http://purl.obolibrary.org/obo/GO_0030350"
					}
				],
				"P4015": [
					{
						"text": "https://github.com/markusstocker/doi-10-1093-eurheartj-ehw333/blob/main/data.csv"
					},
					{
						"@id": "R219781"
					}
				]
			}
		}]
    }
}

orkg = ORKG(host='https://orkg.org')

orkg.papers.add(params=paper, merge_if_exists=True)

