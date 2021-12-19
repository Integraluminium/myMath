# myMath
myMath is my first Module in Python.

---
With the module stochastic you can create ___Bernoulli distributions___,
and you can show them using a histogram.
It is recommended to use the __binominal.py__ in the module __stochastic__.

With the myAlgebra script you can create ___Polynom functions___ which can be integrated
and can be deviated.

---
## Use of stochastic

    func = Binominal(1000, 0.5)   # Creates Bernoulli distribution with n = 1000 and p = 0.5
 
    func(5) == func.binompdf(5)
    
    func.binomcdf(0, 100)   # returns sum of distribution of binompdf from 0 to 100

    func.derivation     # returns sigma
    func.sim_get_sigma_distribution()   # returns distribution of 1*sigma

    
