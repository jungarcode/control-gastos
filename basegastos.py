import sqlite3

class gastos:

    def abrir(self):
    
        conexion = sqlite3.connect("Desembolsos.db3")
        return conexion

    def alta(self,datos):
    
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "INSERT INTO gastos(nombre,fecha,monto) values(?,?,?)"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()
        
    def consulta(self,datos):
        
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="SELECT id, nombre, monto from gastos where fecha=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="SELECT id, fecha, nombre, monto from gastos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def baja(self,datos):
        
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="DELETE from gastos where id=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()
            
            
    def modificacion(self,datos):
        
        try:
            
            cone=self.abrir()
            cursor=cone.cursor()
            sql="UPDATE gastos set nombre=?, monto=? where id=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount
            
        except:
            cone.close()
            
    def suma(self,datos):
        
        try:
            
            cone=self.abrir()
            cursor=cone.cursor()
            sql="SELECT sum(monto) from gastos where fecha  between ? and ?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.fetchone()
            
        except:
            cone.close()
            
        
        
        