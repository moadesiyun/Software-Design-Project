from flask import Flask, render_template, request, redirect, url_for
import flask.globals
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import unittest


app = Flask(__name__)


class testOverall(TestCase):
    def testHome(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def testLogin(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def testSignUp(self):
        response = self.client.get('/sign-up')
        self.assertEqual(response.status_code, 200)

    def testQuoteForm(self):
        response = self.client.get('/quote-form')
        self.assertEqual(response.status_code, 200)

    def testProfile(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)



unittest.main()
