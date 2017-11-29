"""
Run all the code on HCDM

"""
source = "SanDiego"
target = "Austin"
feature = "energy"
for appliance in ['hvac','fridge','mw','dw','oven','wm']:

	for setting in ['transfer', 'normal']:
		for train_percentage in [6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
			for random_seed in range(4):
				CMD = 'python ../../code/mf_baseline.py {} {} {} {} {} {} {} &> ../../logs/{}-{}-{}-{}-{}-{}-{}.out &'.format(setting, source, target, appliance,
			                                                                                                     feature,
			                                                                                                     random_seed,
			                                                                                                     train_percentage,
			                                                                                                                setting,
			                                                                                                                source,
			                                                                                                                target,
			                                                                                                                appliance,
			                                                                                                                feature,
			                                                                                                                random_seed,
			                                                                                                                train_percentage
				                                                                                                            )
				print(CMD)

