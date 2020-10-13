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
    b = BacktrackSolution(queens)
    is_solution = b.process()
    print(is_solution)
    if is_solution:
        db = DBhandler()
        bt_solution = Solution()
        bt_solution.queens = queens
        bt_solution.bt_solution = b.board.board
        db.add(bt_solution)
        db.commit()
        return jsonify(b.board.board)

    return jsonify({
        'error': f'Could not get the answer for {queens} queens'
    })


if __name__ == "__main__":
    app.run(debug=True)
