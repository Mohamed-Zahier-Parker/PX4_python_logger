import numpy 
import matplotlib.pyplot as plt

#Read data from file
with open("/home/alan/Documents/PX4_Graph_Plotting_Code/Python_code_to_plot_cpp_log_data/Landing_Procedure_Data.txt") as f:
    contents = f.readlines()

x_string=contents[0]
z_string=contents[1]
size=int(contents[2])
L_track=float(contents[4]) 
x=[]
z=[]
prev_delim_loc=0
first_delim_loc=x_string.find(",")

#Convert data from string to float
for index, character in enumerate(x_string):
    if character==",":
        if(index==first_delim_loc):
            x.append(float(x_string[prev_delim_loc:index]))
        else:
            x.append(float(x_string[prev_delim_loc+1:index]))
        prev_delim_loc=index

prev_delim_loc=0
first_delim_loc=z_string.find(",")
for index, character in enumerate(z_string):
    if character==",":
        if(index==first_delim_loc):
            z.append(float(z_string[prev_delim_loc:index]))
        else:
            z.append(float(z_string[prev_delim_loc+1:index]))
        prev_delim_loc=index

# Plot graph
graph1,=plt.plot(x,z)
#plt.ylabel('Altitude(m)')
#plt.xlabel('Ground distance(m)')
#plt.title("Altitude vs distance graph of landing procedure")


# Print extra data
print("L_Track : ",L_track,"\n")

#State graph
state_string=contents[5]
state=[]
prev_delim_loc=0
first_delim_loc=state_string.find(",")
for index, character in enumerate(state_string):
    if character==",":
        if(index==first_delim_loc):
            state.append(int(state_string[prev_delim_loc:index]))
        else:
            state.append(int(state_string[prev_delim_loc+1:index]))
        prev_delim_loc=index

# Plot state graph
graph2,=plt.plot(x,state)
#plt.ylabel('State')
#plt.xlabel('Ground distance(m)')
#plt.title("State vs distance graph of landing procedure")


#Climbrate Graph
hdot_string=contents[6]
hdot=[]
prev_delim_loc=0
first_delim_loc=hdot_string.find(",")
for index, character in enumerate(hdot_string):
    if character==",":
        if(index==first_delim_loc):
            hdot.append(float(hdot_string[prev_delim_loc:index]))
        else:
            hdot.append(float(hdot_string[prev_delim_loc+1:index]))
        prev_delim_loc=index

# Plot climbrate graph
graph3,=plt.plot(x,hdot)
#plt.ylabel('hdot')
#plt.xlabel('Ground distance(m)')
#plt.title("hdot vs distance graph of landing procedure")

#Gliding Climbrate Graph
hdot_bar_ref_string=contents[7]
hdot_bar_ref=[]
prev_delim_loc=0
first_delim_loc=hdot_bar_ref_string.find(",")
for index, character in enumerate(hdot_bar_ref_string):
    if character==",":
        if(index==first_delim_loc):
            hdot_bar_ref.append(float(hdot_bar_ref_string[prev_delim_loc:index]))
        else:
            hdot_bar_ref.append(float(hdot_bar_ref_string[prev_delim_loc+1:index]))
        prev_delim_loc=index

# Plot gliding climbrate graph
graph4,=plt.plot(x,hdot_bar_ref)
#plt.ylabel('hdot_bar_ref')
#plt.xlabel('Ground distance(m)')
#plt.title("hdot_bar_ref vs distance graph of landing procedure")

#Airspeed Graph
airspeed_string=contents[8]
airspeed=[]
prev_delim_loc=0
first_delim_loc=airspeed_string.find(",")
for index, character in enumerate(airspeed_string):
    if character==",":
        if(index==first_delim_loc):
            airspeed.append(float(airspeed_string[prev_delim_loc:index]))
        else:
            airspeed.append(float(airspeed_string[prev_delim_loc+1:index]))
        prev_delim_loc=index

# Plot gliding climbrate graph
graph5,=plt.plot(x,airspeed)


#Plot all graphs
plt.legend([graph1,graph2,graph3,graph4,graph5],['Altitude','state','climbrate','glideslope climbrate','airspeed'])
plt.ylabel('States')
plt.xlabel('Intrack Distance(m)')
plt.show()     
        
        
