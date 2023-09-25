import UIKit


var a : String = "A"

switch a {
case "A":
    print("A")
case "a":
    print("a")
default:
    print("?")
}

var b : String = "b"

switch b {
case "A"..."Z":
    print("대문자")
case "a"..."z":
    print("소문자")
default:
    print("?")
}
