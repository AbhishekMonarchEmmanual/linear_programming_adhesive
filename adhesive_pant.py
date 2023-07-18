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
st.write("GIVE CONSTRAINT VALUES FOR BAG PRODUCTION FOR EACH PRODCUT")
st.text("PRODUCTION NUMBER OF BAGS IN MONTH THAT SHOULD NOT EXCEED FOR EACH BAG")
st.text("FOR EXAMPLE IF YOU GIVE VALUE FOR AAC BLOCK ADHESIVE 30 KG = 200")
st.text("IT MEANS THAT PRODUCTION SHOULD NOT EXCEED BAGS FOR AAC BLOCK ADHESIVE 30 KG 200")
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
if st.checkbox("MONTHLY BAG PRUDUCTION YOU DONT WANT TO EXCEED"):
    total_no_bags = int(aac_30) + int(aac_40) + int(floor_tile_adhesive) + int(wall_tile_adhesive) + int(stone_tile_adhesive)
    st.write(total_no_bags)
if st.checkbox("TOTAL PRODUCTION COST YOU HAVE IF YOU PRODUCE ALL BAG"):
    total_production_cost = int(aac_30)*aacblock30cost + int(aac_40)*aacblock40cost + int(floor_tile_adhesive)*floortile20cost + int(wall_tile_adhesive) * walltile20cost + int(stone_tile_adhesive) * stonetile20cost
    st.write(total_production_cost)
if st.checkbox("CLICK TO CREATE THE CONSTRAINT"):
    total_no_bags = int(aac_30) + int(aac_40) + int(floor_tile_adhesive) + int(wall_tile_adhesive) + int(stone_tile_adhesive)
    total_production_cost = int(aac_30)*aacblock30cost + int(aac_40)*aacblock40cost + int(floor_tile_adhesive)*floortile20cost + int(wall_tile_adhesive) * walltile20cost + int(stone_tile_adhesive) * stonetile20cost

    st.write(f"MAX NUMBER OF BAG PRODUCE IN MONTH {total_no_bags}")
    st.write(f"MAX PRODUCTION COST YOU BASED ON NO. OF BAG PRODCUT {total_production_cost}")
    

    aacblock30constraint = m.add_constraint(noaacblock30adhesive <=int(aac_30))
    aacblock40constraint = m.add_constraint(noaacblock40adhesive <=int(aac_40))
    floortile20constraint = m.add_constraint(nofloortile20adhesive <=int(floor_tile_adhesive))
    walltile20constraint = m.add_constraint(nowalltile20adhesive <=int(wall_tile_adhesive))
    stonetile20constraint = m.add_constraint(nostonetile20adhesive <=int(stone_tile_adhesive))
    
    st.write("NOW LETS MAKE ANOTHER CONSTRAINT")
    st.write("TOTAL PRODCUTION CONSTRAINT : MONTHLY COST OF PRODUCING ALL PROCUCTS")
    st.write("THE VALUE THAT YOU WILL PROVIDE SIGNIFY THE AMOUNT YOU DONT WANT TO")
    st.write("EXCEED WHILE MANUFACTURING ALL THE PRODCUTS" )
    st.write("FOR EX : 200000 SIGNIFY TOTAL COST TO CREATE YOUR PRODUCT SHOULD BE LESS THAT 2LAC")
    
    production_cost= st.text_input("TOTAL COST OF PRODUCTION CONTRAINTS",)

    
    
    if st.checkbox("CLICK TO GENERATE REPORT"):
        totalproductionconstraint = m.add_constraint(m.sum([noaacblock30adhesive*aacblock30cost,noaacblock40adhesive*aacblock40cost,nofloortile20adhesive*floortile20cost,nowalltile20adhesive*walltile20cost, nostonetile20adhesive*stonetile20cost])<=int(production_cost))
        profit = m.maximize(noaacblock30adhesive*aacblock30profit+ noaacblock40adhesive*aacblock40profit + nofloortile20adhesive*floortile20profit + nowalltile20adhesive*walltile20profit + nostonetile20adhesive*stonetile20profit)
        sol = m.solve()
        report = sol.display()
        st.write(f"{sol}")
        st.write(f"MAX PROFIT YOU CAN ACHEIVE WITH PROVIDED CONSTRAINTS : {profit}")
        st.write(f"PROFIT WHEN YOU DO NOT EXCEED PRODCUTION COST IN MONTH : {production_cost}")
        st.write(f"ALSO MAX NUMBER OF OVERALL BAG YOU WANT TO PRODUCE IN MONTH : {total_no_bags}")
        st.write(f"WITH THE AMOUNT WOULD HAVE PAYED IN CASE YOU TOUCH YOUR MAX BAG VALUE {total_production_cost}")
        