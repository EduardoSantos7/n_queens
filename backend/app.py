import sys

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

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
        return jsonify(b.board.board)

    return jsonify({
        'error': f'Could not get the answer for {queens} queens'
    })


if __name__ == "__main__":
    app.run(debug=True)
