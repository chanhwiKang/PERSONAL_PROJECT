import UIKit

struct Myarray<T>{
    
    // 제네릭을담은 빈 배열
    var elements = [T]()
    //var elements : [T] = [T]()
    
    // 생성자
    init(_ elements: [T]){
        self.elements = elements
    }
}

struct Friend {
    var name: String
}

struct PpakCoder {
    var name: String
}

var mySomeArray = Myarray([1,2,3])
print("mySomeArrary : \(mySomeArray)")

var myStringArray = Myarray(["가","나","다"])
print("myStringArrary : \(myStringArray)")

let friend_01 = Friend(name: "철수")
let friend_02 = Friend(name: "영희")

var myFriendArray = Myarray([friend_01,friend_02])
print("\(myFriendArray)")
