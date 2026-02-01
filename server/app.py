#!/usr/bin/env python3

import os
from flask import request
from flask_restful import Resource
from config import create_app, db, api
from models import Book, BookSchema

env = os.getenv("FLASK_ENV", "dev")
app = create_app(env)

class Books(Resource):
    def get(self):
        # Read query parameters with defaults
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=5, type=int)

        # Paginate the query
        pagination = Book.query.paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )

        # Serialize results
        items = BookSchema(many=True).dump(pagination.items)

        # Return structured response
        return {
            "page": page,
            "per_page": per_page,
            "total": pagination.total,
            "total_pages": pagination.pages,
            "items": items
        }, 200

api.add_resource(Books, "/books", endpoint="books")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
