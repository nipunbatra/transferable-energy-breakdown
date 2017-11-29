"""
Run all the code on HCDM

"""

from subprocess import Popen
import os, sys
# region = "Austin"
# year = 2014
import delegator

# Enter your username on the cluster
username = 'nb2cz'

# Location of .out and .err files
SLURM_OUT = os.path.expanduser("~/slurm_out_aaai")

# Create the SLURM out directory if it does not exist
if not os.path.exists(SLURM_OUT):
	os.makedirs(SLURM_OUT)

# Max. num running processes you want. This is to prevent hogging the cluster
MAX_NUM_MY_JOBS = 300
# Delay between jobs when we exceed the max. number of jobs we want on the cluster
DELAY_NUM_JOBS_EXCEEDED = 10
import time

source = "SanDiego"
target = "Boulder"
# shell_script = "{}_{}.sh".format(source, target)
# f = open(shell_script, 'w')
for case in [4, 2]:
	# for constant_use in ['True', 'False']:
	for constant_use in ['False', 'True']:
		for static_use in ['False', 'True']:
			for setting in ['normal', 'transfer']:
				# for setting in ['normal','transfer']:
				for train_percentage in [6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
					for random_seed in range(4):
						SLURM_SCRIPT = "{}_{}_{}_{}_{}_{}_{}-{}.pbs".format(SLURM_OUT, setting, case, constant_use, static_use,
						                                                source, target, random_seed, train_percentage)
						CMD = 'python ../../code/graph_laplacian.py {} {} {} {} {} {} {} {}'.format(setting, case,
						                                                                            constant_use,
						                                                                            static_use, source,
						                                                                            target, random_seed,
						                                                                            train_percentage)
						OFILE = "{}/{}_{}_{}_{}_{}_{}_{}-{}.out".format(SLURM_OUT, setting, case, constant_use, static_use,
						                                                source, target, random_seed, train_percentage)
						EFILE = "{}/{}_{}_{}_{}_{}_{}_{}-{}.err".format(SLURM_OUT, setting, case, constant_use, static_use,
						                                                source, target, random_seed, train_percentage)
						lines = []
						lines.append("#!/bin/sh\n")
						lines.append('#SBATCH --time=1-16:0:00\n')
						lines.append('#SBATCH --mem=16\n')
						lines.append('#SBATCH -o ' + '"' + OFILE + '"\n')
						lines.append('#SBATCH -e ' + '"' + EFILE + '"\n')
						lines.append(CMD + '\n')
						with open(SLURM_SCRIPT, 'w') as f:
							f.writelines(lines)
						command = ['sbatch', SLURM_SCRIPT]
						while len(delegator.run('squeue -u %s' % username).out.split("\n")) > MAX_NUM_MY_JOBS + 2:
							time.sleep(DELAY_NUM_JOBS_EXCEEDED)

						delegator.run(command, block=False)
						print SLURM_SCRIPT
						sys.stdout.flush()

