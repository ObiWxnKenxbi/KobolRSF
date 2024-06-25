from phaseintegrator import PhaseIntegrator

cv = 0.5
integrator = PhaseIntegrator(cv, start_time=0, end_time=200, num_steps=1000)
integrator.run()