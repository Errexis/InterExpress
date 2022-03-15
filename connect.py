import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="interexpress"
)
c = conn.cursor()

def requestquery(cep, product):
    c.execute("INSERT INTO entregas (cep, produto) VALUES (%s,%s)", (cep, product))
    conn.commit()
    print(f"Entrega para o CEP: {cep}, Produto: {product}.")

def trackingquery():
    c.execute("SELECT INTO rastreios")
    c.fetchone()

print("Database conectada.")