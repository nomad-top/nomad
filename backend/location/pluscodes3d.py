import openlocationcode as olc

def encode3D(lat, lon, alt, codeLength=10):
    """Get a 3D+ code from a latitude, longitude and altitude."""
    return f"{olc.encode(lat, lon, codeLength)}@{alt}"

def decode3D(code):
    """Get a latitude, longitude and altitude from a 3D+ code."""
    code = code.split("@")
    codeArea = olc.decode(code[0])
    lat, lon = format(codeArea.latitudeCenter, 'F'), format(codeArea.longitudeCenter, 'F')
    alt = int(code[1])
    return lat, lon, alt

if __name__ == "__main__":
    
    print("North Pole, 1000m altitude")

    code = encode3D(lat=90, lon=0, alt=1000, codeLength=13)
    short = olc.shorten(code.split("@")[0], latitude=90, longitude=0)
    decode = decode3D(code)

    print(short) # in short +X2RRR @ 1000
    print(code) # CFX2X2X2+X2RRR@1000
    print(decode) # ('90.000000', '0.000001', 1000)