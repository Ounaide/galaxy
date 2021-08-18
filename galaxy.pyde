rings = []

def setup():
    global rings
    size(1200,600,P3D)
    blendMode(ADD)
    rayInf = 1
    rayExt = 9
    ict = 1
    for ringI in range(50):
        ring = createShape()
        ring.strokeWeight(1.5)
        ring.beginShape(POINTS) 
        ring.stroke(lerpColor(color(73,115,161),color(157,47,77), ringI/45),200)
        for starIndex in range(3000):
            a = random(0,1)*TWO_PI
            r = sqrt(random(sq(rayInf),sq(rayExt)))
            ring.vertex(r*cos(a),r*sin(a),random(-ict,ict))
        ring.endShape()
        rings.append(ring)
        rayInf += ict
        rayExt += ict*1.5
        ict += 1
        
def draw():
    background(0)
    camera(-width/2,-height/2,100,100,100,0,0,1,0)
    for _ in range(1,50):
        pushMatrix()
        rotateY((TWO_PI/sq(_)*frameCount)/10)
        rotateX(1.45)
        shape(rings[_])
        popMatrix()
        
