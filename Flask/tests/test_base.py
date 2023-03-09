from flask_testing import TestCase
from flask import current_app, url_for
from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        
        return app
    
    def test_app_exists(self):
        self.assertIsNotNone(current_app)
        
    def test_app_in_test_mode(self): #realizar un test sobre si la app esta en modo test
        self.assertTrue(current_app.config['TESTING'])
        
    def test_index_redirects(self): #hacer un test de redireccionamiento
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello'))
                                           
    def test_hello_get(self): # probar si hello nos devuelve 200 al hacer un GET        
        response = self.client.get(url_for('hello'))  
        self.assert200(response)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        