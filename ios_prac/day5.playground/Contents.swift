import UIKit

// 옵셔널이란? Comments
// 값이 있는지 없는지 모른다.

var someVariable : Int? = nil

if someVariable == nil {
    someVariable = 90
}

print("someVariable: \(someVariable)")
// 언랩핑이란? 감싸져있는 것을 벗기는 것 (옵셔널을 벗김)

if let otherVarible = someVariable {
    print("언래핑 되었다. 값이 있다. otherVarible :\(otherVarible)")
} else {
    print("값이 없다")
}

someVariable = nil

let myValue = someVariable ?? 10
print("\(myValue)")

var firstvalue : Int? = 30
var secondvalue : Int? = 50

print("\(firstvalue)")
print("\(secondvalue)")

unwrap(firstvalue)
unwrap(secondvalue)

func unwrap(_ parameter: Int?){
    print("unwrap() called")
    
    guard let unWrappedParam = parameter else {
        return
    }
    print("\(unWrappedParam)")
}
