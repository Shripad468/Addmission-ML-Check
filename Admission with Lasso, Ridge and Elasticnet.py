#!/usr/bin/env python
# coding: utf-8

# # Shripad_Joshi Batch No 6 "Admission"

# random state is given for random selection of data after shuffle while splitting...
# it is important to get same data as the previous one

# ## here value of training set(84.15%) is greater than test set(75.34%) while test fails for our model then it's called OVERFITTING model.........which means our model is overfitting our training data 

# # Applying Regularization Technique

# ### 1) LASSO Regression Model

# At this particular time, lasso_reg score is 75.34% and regression.score is 75.34% which is same which means whether we use basic regression(without using regilarization) or LASSO, we are not able to get better scores. Therefore, we can say that our model did not overfit the data which means this score is best for this particular data

# ## 2) Ridge Regression Model

# At this particular time, Ridge Reg Score is 75.35% and lasso_reg score is 75.34% and regression.score is 75.34% which is same which means whether we use basic regression(without using regilarization) or LASSO, we are not able to get better scores. Therefore, we can say that our model did not overfit the data which means this score is best for this particular data

# ### 3) Elastic Net
