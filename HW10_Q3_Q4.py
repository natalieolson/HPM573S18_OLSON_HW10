#Use a cost-utility plane to display the expected discounted
#incremental utility and cost form the anticoagulation drug. Report the results of your cost-utility analysis
#in a table. Make sure to include the 95% confidence intervals for all reported estimates (discounted cost,
#discounted utility, incremental discounted cost, incremental discounted utility and the ICER).

#Plot the incremental net monetary benefit curve when the
#anticoagulation drugs is used for varying values of willingness-to-pay. Show the 95% confidence region.


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

# report the CEA results
SupportMarkov.report_CEA_CBA(simOutputs_none, simOutputs_ANTICOAG)

