from flask import Blueprint

main = Blueprint('main', __name__)

import json
from engine import RecommendationEngine

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from flask import Flask, request


@main.route("/<int:user_id>/ratings/top/<int:count>", methods=["GET"])
def top_ratings(user_id, count):
    """"Untuk menampilkan sejumlah <count> rekomendasi film ke user <user_id>"""
    logger.debug("User %s TOP ratings requested", user_id)
    top_rated = recommendation_engine.get_top_ratings(user_id, count)
    return json.dumps(top_rated)


@main.route("/movies/<int:movie_id>/recommend/<int:count>", methods=["GET"])
def movie_recommending(movie_id, count):
    """"Untuk menampilkan film <movie_id> terbaik direkomendasikan ke sejumlah <count> user"""
    logger.debug("MovieId %s TOP user recommending", movie_id)
    top_rated = recommendation_engine.get_top_movie_recommend(movie_id, count)
    return json.dumps(top_rated)


def create_app(spark_session, dataset_path):
    global recommendation_engine

    recommendation_engine = RecommendationEngine(spark_session, dataset_path)

    app = Flask(__name__)
    app.register_blueprint(main)
    return app
