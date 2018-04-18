#Use your simulation model to estimate the discounted total cost and discounted total utility of patients
#  who start in the state “Well” for both treatment scenarios.


import ParameterClassesV2 as P
import MarkovModelClassesV2 as MarkovCls
import SupportMarkovModelV2 as SupportMarkov

# create and simulate cohort under anticoagulation treatment
cohort_anticoag = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTICOAG)

simOutputs_anticoag = cohort_anticoag.simulate()


# print outcomes (means and CIs)
SupportMarkov.print_outcomes(simOutputs_anticoag, 'Treatment:')


# create and simulate cohort without treatment
cohort_none = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTICOAG)

simOutputs_none = cohort_none.simulate()


# print outcomes (means and CIs)
SupportMarkov.print_outcomes(simOutputs_none, 'Treatment:')


