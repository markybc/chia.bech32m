from bech32m import decode_puzzle_hash, encode_puzzle_hash
from bottle import route, run, template
from byte_types import hexstr_to_bytes


@route('/getPuzzleHash/<address>')
def getPuzzleHash(address):
    puzzleHash = decode_puzzle_hash(address).hex()
    res = {"code": "200", "data": puzzleHash}
    return res


@route('/getAddress/<puzzleHash>')
def getAddress(puzzleHash):
    address = encode_puzzle_hash(hexstr_to_bytes(puzzleHash), "xch")
    res = {"code": "200", "data": address}
    return res


run(host='localhost', port=9988)
