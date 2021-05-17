from bech32m import decode_puzzle_hash, encode_puzzle_hash
from bottle import route, run
from byte_types import hexstr_to_bytes


@route('/decode/<address>')
def decode(address):
    return decode_puzzle_hash(address).hex()


@route('/encode/<puzzleHash>')
def encode(puzzleHash):
    return encode_puzzle_hash(hexstr_to_bytes(puzzleHash), "xch")


run(host='localhost', port=9988)
