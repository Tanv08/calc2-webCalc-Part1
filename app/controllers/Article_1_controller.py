from app.controllers.controller import ControllerBase
from flask import render_template


class Article_1Controller(ControllerBase):
    @staticmethod
    def get():
        return render_template('Article_1.html')
