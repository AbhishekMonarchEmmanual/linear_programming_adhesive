import pandas as pd
import numpy as np
from docplex.mp.model import Model
import cplex
import streamlit as st

st.title("CALCULATING NUMBER OF BAG AND MAXIMUM PROFIT FOR TILE ADHESIVE BUISNESS")
m= Model(name= "ADHESIVE PRODCUTION")

# We are creating the value variables that point to number of bags
noaacblock30adhesive = m.continuous_var(name = "AAC BLOCK ADHESIVE NUMBER 30 kg")
noaacblock40adhesive = m.continuous_var(name = "AAC BLOCK ADHESIVE NUMBER 40 kg")
nofloortile20adhesive = m.continuous_var(name = "FLOOR TILE ADHESIVE NUMBER 20 kg")
nowalltile20adhesive = m.continuous_var(name = "WALL TILE ADHESIVE NUMBER 20 kg")
nostonetile20adhesive = m.continuous_var(name = "STONE TILE ADHESIVE NUMBER 20 kg")
# Cost of making each bag
aacblock30cost = 186
aacblock40cost = 246
floortile20cost = 127
walltile20cost = 240
stonetile20cost = 151
st.write("COST OF MAKING EACH BAG")

st.write({
    'aacblock adhesive cost 30' : "186 rs" ,
    'aacblock adhesive cost 40 kg' : "246 rs",
    'floor adhesive tile cost 20 kg' : "127 rs",
    'wall tile adhesive  cost 20 kg' : "240 rs",
    'stone tile adhesive cost 20 kg' : "151 rs"
    })

st.write("PROFIT ON EACH BAG (ON DEALER PRICE )")

aacblock30profit = 114
aacblock40profit = 134
floortile20profit = 93
walltile20profit = 113
stonetile20profit = 200

st.write({
    'aacblock adhesive cost 30' : '114 rs',
    'aacblock adhesive cost 40 kg' : '134 rs',
    'floor adhesive tile cost 20 kg' : '93 rs',
    'wall tile adhesive  cost 20 kg' : '113 rs',
    'stone tile adhesive cost 20 kg' : '200 rs'
    })
st.write("GIVE CONSTRAINT VALUES")
st.text("YOU NEED TO GIVE PRODUCTION NUMBER OF BAGS IN MONTH THAT SHOULD NOT EXCEED FOR EACH BAG")
st.text("FOR EXAMPLE GIVE VALUE FOR AAC BLOCK ADHESIVE = 200")
st.text("means that prodcution of bag for particular prodcut should not exceed 200")
st.write("GIVE CONSTRAINT VALUE FOR AAC BLOCK ADHESIVE 30 kg")
aac_30= st.text_input("",  key ="aac_30")
st.write("GIVE CONSTRAINT VALUE FOR AAC BLOCK ADHESIVE 40 kg")
aac_40 = st.text_input("",  key = "aac_40")
st.write("GIVE CONSTRAINT VALUE FOR FLOOR TILE ADHESIVE 20 kg")
floor_tile_adhesive = st.text_input("",  key= "floor_tile")
st.write("GIVE CONSTRAINT VALUE FOR WALL TILE ADHESIVE 20 kg")
wall_tile_adhesive = st.text_input("", key= "wall_tile_adhesive")
st.write("GIVE CONSTRAINT VALUE FOR STONE TILE ADHESIVE 20 kg")
stone_tile_adhesive= st.text_input("", key= "stone_tile")

if st.checkbox("should we create constraint values for number of bags"):
    aacblock30constraint = m.add_constraint(noaacblock30adhesive <=int(aac_30))
    aacblock40constraint = m.add_constraint(noaacblock40adhesive <=int(aac_40))
    floortile20constraint = m.add_constraint(nofloortile20adhesive <=int(floor_tile_adhesive))
    walltile20constraint = m.add_constraint(nowalltile20adhesive <=int(wall_tile_adhesive))
    stonetile20constraint = m.add_constraint(nostonetile20adhesive <=int(stone_tile_adhesive))
    
    st.write("NOW LETS MAKE ANOTHER CONSTRAINT")
    st.write("TOTAL PRODCUTION CONSTRAINT : MONTHLY COST OF PRODUCING ALL PRODCUT")
    st.write("THE VALUE THAT YOU WILL PROVIDE SIGNIFY THE AMOUNT YOU DONT WANT")
    st.write("EXCEED TO CREATE ALL THE PRODCUTS FOR EX : 200000")
    st.write("SIGNIFY TOTAL COST TO CREATE YOUR PRODCUT SHOULD BE LESS THAT 2LAC")
    
    production_cost= st.text_input("TOTAL COST OF PRODUCTION CONTRAINTS",)

    
    
    if st.checkbox("CLICK TO GENERATE REPORT"):
        totalproductionconstraint = m.add_constraint(m.sum([noaacblock30adhesive*aacblock30cost,noaacblock40adhesive*aacblock40cost,nofloortile20adhesive*floortile20cost,nowalltile20adhesive*walltile20cost, nostonetile20adhesive*stonetile20cost])<=int(production_cost))
        m.maximize(noaacblock30adhesive*aacblock30profit+ noaacblock40adhesive*aacblock40profit + nofloortile20adhesive*floortile20profit + nowalltile20adhesive*walltile20profit + nostonetile20adhesive*stonetile20profit)
        sol = m.solve()
        report = sol.display()
        st.write(f"{sol}", f"while not exceeding cost of production {production_cost}")
