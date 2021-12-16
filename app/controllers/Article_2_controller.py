from app.controllers.controller import ControllerBase
from flask import render_template


class Article_2Controller(ControllerBase):
    @staticmethod
    def get():
        return render_template('Article_2.html')

