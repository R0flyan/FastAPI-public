from fastapi import FastAPI

app = FastAPI()
answer = 0

@app.post("/calculator")
#объявляем основную функцию, которая будет выполнять роль калькулятора
def calculator(first_number: float, second_number: float, operator: str):
    #Прописываем проверки на введенную команду оператора для вычислений.
    #При выполнении проверки, прописываем инструкции для вычисления, результат записываем в переменную ответа
    #и возвращаем из функции значение ответа.
    if operator == "+":
        answer = first_number + second_number
        return answer
    if operator == "-":
        answer = first_number - second_number
        return answer
    if operator == "*":
        answer = first_number * second_number
        return answer
    if operator == "/":
        if second_number != 0:
            return first_number / second_number
        if second_number == 0:
            return {"ошибка. делить на 0 нельзя"}
    else:
        return {"error. Проверьте введенные значения"}
