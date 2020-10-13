import sys

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

from DBhandler import DBhandler, Solution

sys.path.append('../')
from algorithms.Backtrack import BacktrackSolution

app = Flask(__name__)
CORS(app)


# Routes
@app.route('/place_n_queens', methods=["GET"])
def place_n_queens():
    queens = request.args.get('queens', type=int)

    db = DBhandler()
    result = {}

    for n in range(1, queens + 1):
        record = db.get_solution(n)

        if record:
            result[n] = record.bt_solution
            continue

        bt = BacktrackSolution(n)
        is_solution = bt.process()

        if is_solution:
            result[n] = bt.get_board()
            db.add(Solution(n, result[n]))
            db.commit()

    return result


if __name__ == "__main__":
    app.run(debug=True)
