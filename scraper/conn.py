import mysql.connector as mysqlpyth
from datetime import datetime

class Connecteur:

    @classmethod
    def connexion(cls):
        print('--------------------')
        print('Connexion en cours..')
        cls.db = mysqlpyth.connect(
            host = 'mysql-container',
            user = 'root',
            passwd = 'root',
            port = 3306,
            db = 'cac40'            
        )
        cls.cursor = cls.db.cursor(buffered = True)
        print('Connexion résussi !')

    @classmethod
    def deconnexion(cls):
        cls.cursor.close()
        cls.db.close()
        print('Connexion terminé !')

    @classmethod
    def insert_data(cls, points, pourcent):
        cls.connexion()
        try:
            query = f"INSERT INTO cac40_value (points, evolution, date_scraping) VALUES ({points}, {pourcent}, '{datetime.now()}')"
            print(query)
            cls.cursor.execute(query)
            cls.db.commit()
            print("Insertion effectué")
        except:
            print("L'insertion à échoué")
        cls.deconnexion()

    @classmethod
    def reset_database(cls):
        cls.connexion()
        query = "DELETE FROM cac40_value"
        cls.cursor.execute(query)
        print('Suppression effectué !')
        cls.deconnexion()
        


    # @classmethod
    # def get_data(cls):
    #     cls.connexion()
    #     query = "SELECT * FROM cac40"
    #     cls.cursor.execute(query)
    #     result = [elem for elem in cls.cursor]
    #     cls.deconnexion()
    #     return result