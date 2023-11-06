import UIKit

// 함수, 메소드 정의
func myFunction(name: String) -> String{
    return "my name is \(name)"
}
// 함수, 메소드 호출
myFunction(name: "찬휘")


func myFunctionSecond(with name: String) -> String{
    return "my name is \(name)"
}

myFunctionSecond(with: "강찬휘")

func myFunctionThird(_ name: String) -> String{
    return "my name is \(name)"
}

myFunctionThird("찬휘강")
