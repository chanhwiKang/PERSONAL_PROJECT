import UIKit
//struct(구조체)
struct YoutuberStruct{
    var name : String
    var subscribersCount : Int
}

var devChan = YoutuberStruct(name: "찬휘", subscribersCount: 1000000)

var devChanClone = devChan
print("=======struct======")
print("변경 전 devChanClone Name : \(devChanClone.name)")

devChanClone.name = "찬휘양"
print("변경 후 devChanClone Name : \(devChanClone.name)")
print("변경 후 devChan Name : \(devChan.name)")

//class
class YoutuberClass {
    var name : String
    var subscribersCount : Int
    
    // 생성자 - 메모리에 올린다
    // init으로 매개변수를 가진 생성자 메소드를 만들어야 매개변수를 넣어 그 값을 가진 객체(object)를 만들 수 있다.
    init(name: String, subscribersCount: Int){
        self.name = name
        self.subscribersCount = subscribersCount
    }
}

var classChan = YoutuberClass(name: "C찬휘", subscribersCount: 1000000)

var classChanClone = classChan
print("=======class======")

print("변경 전 classChanClone\(classChanClone.name)")

classChanClone.name = "CC찬휘"

print("변경 후 classChanClone\(classChanClone.name)")

print("변경 후 classChan\(classChan.name)")
