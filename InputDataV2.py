# simulation settings
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
     # annual discount rate
DISCOUNT = 0.03
DELTA_T = 1       # years

# transition matrix
TRANS_MATRIX = [
    [0.75,  0.15,   0.0,    0.1],   # Well
    [0,     0.0,    1.0,    0.0],   # Stroke
    [0,     0.25,   0.55,   0.2],   # Post-Stroke
    [0.0,   0.0,    0.0,    1.0],   # Dead
    ]

# annual cost of each health state
ANNUAL_STATE_COST = [
    0.0,   # Well
    5000.0,   # Stroke
    200.0,  # Post-Stroke
    0.0 #Dead
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    1.0,   # Well
    0.8865,   # Stroke
    0.9,   # Post-Stroke
    0.0 #Dead
    ]

# annual drug costs
Anticoagulation_Cost = 2000

# treatment relative risk
RR_STROKE = 0.65
RR_BLEEDING = 1.05
