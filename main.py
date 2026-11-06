from js import document
from pyodide.ffi import create_proxy

# Python dictionary for the non-metal elements thing
non_metals = {
    "H": ("Hydrogen", "1", "1.008"),
    "C": ("Carbon", "6", "12.011"),
    "N": ("Nitrogen", "7", "14.007"),
    "O": ("Oxygen", "8", "15.999"),
    "F": ("Fluorine", "9", "18.998"),
    "P": ("Phosphorus", "15", "30.974"),
    "S": ("Sulfur", "16", "32.06"),
    "Cl": ("Chlorine", "17", "35.45")
}

def search_element(event):
    # Element1 variable is case sensitive
    Element1 = document.getElementById("element-symbol").value.strip()
    
    # Its a dash if it is nothing
    result = non_metals.get(Element1, ("Element not found in non-metals list", "-", "-"))
    
    element_name = result[0]
    atomic_number = result[1]
    atomic_mass = result[2]
    
    document.getElementById("res-symbol").innerText = Element1 if element_name != "Element not found in non-metals list" else "-"
    document.getElementById("res-name").innerText = element_name
    document.getElementById("res-number").innerText = atomic_number
    document.getElementById("res-mass").innerText = atomic_mass

def setup(event=None):
    button = document.getElementById("btn-submit")
    button.addEventListener("click", create_proxy(search_element))

setup()