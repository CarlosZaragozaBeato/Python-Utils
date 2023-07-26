from fastapi import FastAPI
from ExcelScript import ExcelPython



app = FastAPI()



excel_python = ExcelPython()






@app.get("/update/")
def actualizar_row(saldo_actual, recogida, email):    
    print("s")
    
    return excel_python.modificar_general(
        saldo_actual=saldo_actual, 
        recogida=recogida,
        email=email)