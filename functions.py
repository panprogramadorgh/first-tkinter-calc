from tkinter import END

def delete_entry(entry):
  entry.delete(0, END)

def calculate(first, seccond, op):
  if op == 'sum': return first + seccond
  elif op == 'sub': return first - seccond
  elif op == 'multi': return first * seccond
  elif op == 'div': return first / seccond
  else: raise Exception("Unknown operation")

def handle_click(entries, op):
  first = entries[0].get()
  seccond = entries[1].get()
  try:
    first = float(first)
    seccond = float(seccond)
  except Exception:
    for entry in entries:
      delete_entry(entry)
    print("You can just operate with numbers")
  else:
    result = calculate(first, seccond, op)
    print(result)
