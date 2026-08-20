Language level is identified using the Flesch-Kincaid method. 

Appropriateness has been measured using:

a) the average level of education for workers in relevant industries for each union (using 2021 ABS data)

b) the style guide suggested by the Australian Government Style Manual (can be found at: https://www.stylemanual.gov.au/accessible-and-inclusive-content/literacy-and-access)

The results have been summarised in a Substack post. You can find the post here: [insert URL]

**Suggested Workflow**

1) `education_by_industry_analysis.ipynb`
2) `textual_analysis.ipynb`
3a) `cross_referencing_by_industry_analysis.ipynb`
3b) `body_readability_analysis.ipynb`

(Order of 3a and 3b irrelevant - they simply handle for different  (individual unions vs state and nationwide union councils)

**Other files**
* readability_to_grade.py: contains a mapping function (`R2G`) that maps Flesch-Kincaid score to an equivalent education level. Used in `body_readability_analysis.ipynb` and `cross_referencing_by_industry_analysis.ipynb`.

**Note:** This repository is demonstrate how I got the results discussed in the article. You are welcome to repeat the workflow by using `Data/get_text_data.py` followed by `Data/clean_text.ipynb` at the beginning of the workflow - however, you are likely to get different results, as the data I used will be overwritten.

Data is accurate as of 2026-08-04."# ucsrl" 
