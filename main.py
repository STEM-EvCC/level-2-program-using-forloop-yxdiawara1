mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
total_missions = 0
succeful_missions =0
missions_before_2000 = []


# the loop throught the missions
 
for i in range(len (mission_names)):
    total_missions += 1 

    if mission_success[i]:
        succeful_missions += 1

    if mission_years[i] < 2000:
        missions_before_2000.append(mission_names[i])

    # calculate success rate fore the year 2002: ")
    success_rate = (succeful_missions/ total_missions) * 100
        
        # print result 

print(f" Total number of mission: {total_missions} " )
print(f"Number of successful missions: {succeful_missions}")
print(f"Succees rate: {success_rate:.2f}%")
print("Mission launched before the year 2000:")
for mission in missions_before_2000:
    print(f"- {mission}")
