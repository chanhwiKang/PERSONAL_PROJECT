import UIKit

enum School {
    //    case elementary
    //    case middle
    //    case high
    case elementary, middle, high
}

let yourSchool = School.elementary

//print("yourSchool: \(yourSchool)")
print("yourSchool: ",yourSchool)

enum Grade : Int{
    case first = 1
    case seconde = 2
}

let yourGrade = Grade.seconde

print("yourGrade: \(yourGrade.rawValue)")

enum SchoolDetail {
    case elementary(name: String)
    case middle(name: String)
    case high(name: String)

    func getName() -> String {
        switch self {
        case .elementary(let name):
            return name
        case let .middle(name):
            return name
        case let .high(name):
            return name
        }
    }
}

let yourSchoolName = SchoolDetail.middle(name: "찬휘네중학교")
print("중학교 이름은: \(yourSchoolName.getName())")
