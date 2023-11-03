
@freezed
 class Address with _$Address {
  const Address._();  
    
  @JsonSerializable(explicitToJson: true)  
  const factory Address({
  @Default('') String street,
  @Default('') String city,
  @Default('') String state,
  @Default('') String postalCode,
  }) = _Address;
  
  factory Address.fromJson(Map<String, dynamic> json) => _$AddressFromJson(json);
}

@freezed
 class PhoneNumbers with _$PhoneNumbers {
  const PhoneNumbers._();  
    
  @JsonSerializable(explicitToJson: true)  
  const factory PhoneNumbers({
  @Default('') String type,
  @Default('') String number,
  }) = _PhoneNumbers;
  
  factory PhoneNumbers.fromJson(Map<String, dynamic> json) => _$PhoneNumbersFromJson(json);
}

@freezed
 class FamilyMembers with _$FamilyMembers {
  const FamilyMembers._();  
    
  @JsonSerializable(explicitToJson: true)  
  const factory FamilyMembers({
  @Default('') String relation,
  @Default('') String name,
  }) = _FamilyMembers;
  
  factory FamilyMembers.fromJson(Map<String, dynamic> json) => _$FamilyMembersFromJson(json);
}

@freezed
 class Person with _$Person {
  const Person._();  
    
  @JsonSerializable(explicitToJson: true)  
  const factory Person({
  @Default('') String name,
  @Default(0) int age,
  @Default(0) int isEmployed,
   Address? address,
  @Default([]) List<PhoneNumbers> phoneNumbers,
  @Default([]) List<String> emailAddresses,
  @Default([]) List<FamilyMembers> familyMembers,
  }) = _Person;
  
  factory Person.fromJson(Map<String, dynamic> json) => _$PersonFromJson(json);
}

@freezed
 class Employees with _$Employees {
  const Employees._();  
    
  @JsonSerializable(explicitToJson: true)  
  const factory Employees({
  @Default('') String name,
  @Default('') String position,
  }) = _Employees;
  
  factory Employees.fromJson(Map<String, dynamic> json) => _$EmployeesFromJson(json);
}

@freezed
 class Company with _$Company {
  const Company._();  
    
  @JsonSerializable(explicitToJson: true)  
  const factory Company({
  @Default('') String name,
  @Default('') String industry,
  @Default([]) List<Employees> employees,
  }) = _Company;
  
  factory Company.fromJson(Map<String, dynamic> json) => _$CompanyFromJson(json);
}

@freezed
 class Products with _$Products {
  const Products._();  
    
  @JsonSerializable(explicitToJson: true)  
  const factory Products({
  @Default('') String name,
  @Default(0.0) double price,
  @Default([]) List<String> categories,
  }) = _Products;
  
  factory Products.fromJson(Map<String, dynamic> json) => _$ProductsFromJson(json);
}

@freezed
 class MyModel with _$MyModel {
  const MyModel._();  
    
  @JsonSerializable(explicitToJson: true)  
  const factory MyModel({
   Person? person,
   Company? company,
  @Default([]) List<Products> products,
  }) = _MyModel;
  
  factory MyModel.fromJson(Map<String, dynamic> json) => _$MyModelFromJson(json);
}
