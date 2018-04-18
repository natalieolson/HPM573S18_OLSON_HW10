#Estimate the change in the expected discounted cost, the
#expected discounted utility, and the expected number of strokes when the anticoagulation drug is used.
#Report the 95% confidence intervals for all your estimates.


import ParameterClassesV2 as P
import MarkovModelClassesV2 as MarkovCls
import SupportMarkovModelV2 as SupportMarkov


# create a cohort
cohort_none = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)
# simulate the cohort
simOutputs_none = cohort_none.simulate()

# simulating combination therapy
# create a cohort
cohort_ANTICOAG = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.ANTICOAG)
# simulate the cohort
simOutputs_ANTICOAG = cohort_ANTICOAG.simulate()

# print comparative outcomes
SupportMarkov.print_comparative_outcomes(simOutputs_none, simOutputs_ANTICOAG=)
