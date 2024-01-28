import subprocess

def run_simulation(simulation_index):
    fcd_output_file = f"fcd_output_run_{simulation_index}.xml"
    collision_output_file = f"collision_output_run_{simulation_index}.xml"

    # Replace this with the actual command or function to run your simulation
    simulation_command = ["sumo-gui",
                          "-c", "/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/weeklytask-7-12-23/new1.sumocfg",
                          "--random",
                          "--collision.action", "remove",
                          "--collision-output", collision_output_file,
                          "--max-num-vehicles", "60",
                          "--step-length", "0.1",
                          "--fcd-output", fcd_output_file,
                         ]
    subprocess.run(simulation_command)

num_simulations = 10

for i in range(num_simulations):
    run_simulation(i)