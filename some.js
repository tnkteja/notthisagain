
// define a lambda function to filter _id key
var no_id= key => key != "_id";

var compareObjects = function(object1, object2){
  
  var keys1 = R.filter(no_id, Object.getOwnPropertyNames(object1));
  var keys2 = R.filter(no_id, Object.getOwnPropertyNames(object2))
  
  // check if both objects have same number of keys
  if(keys1.length != keys2.length){
    return false;
  }
  
  //Order the keys
  keys1.sort();
  keys2.sort();
  
  for(var i=0;i<keys1.length;i++){
    
    // check if the keys are same
    if(keys1[i] != keys2[i]){
      return false;
    }

    // check if the value1 and value2 are array types
    if( R.isArrayLike(object1[keys1[i]]) && R.isArrayLike(object2[keys2[i]]) ){
       if(!compareArrays(object1[keys1[i]],object2[keys2[i]])){
          return false;
       }
    } else if( (object1[keys1[i]] instanceof Date && R.type(object2[keys2[i]]) == "String"
                || R.type(object1[keys1[i]]) == "String" && object2[keys2[i]] instanceof Date 
                   || object1[keys1[i]] instanceof Date && object2[keys2[i]] instanceof Date)  ){
        
        var v1=null;
        if(object1[keys1[i]] instanceof Date){
          v1=object1[keys1[i]].toISOString()
        } else {
          v1=object1[keys1[i]]
        } 

        var v2=null;
        if(object2[keys2[i]] instanceof Date){
          v2=object2[keys2[i]].toISOString()
        } else {
          v2=object2[keys2[i]]
        } 

        if(v1!=v2){
          return false;
        }

    } else if (typeof object1[keys1[i]] == "object" ){
      if (typeof object2[keys2[i]] == "object" && !compareObjects(object1[keys1[i]],object2[keys2[i]])){
        return false;
      }
        
    }else{ 
      if (object1[keys1[i]]!==object2[keys2[i]]){ // if not object types check equality
        return false;
      }
    }
  }
  return true;
}

var compareArrays = function(array1, array2){
  // First check if the array sizes are equal.
  
  if(array1.length != array2.length){
    return false;
  }
  
  // If they are of same size.
  // Since the arrays are unordered list, we cannot sort them to order as
  // comparision function is not determinable
  
  var array2copy=array2.slice();
  
  for(var i=0;i<array1.length; i++){
    for(var j=0;j<array2copy.length; j++){
  
        if ( R.isArrayLike(array1[i]) && R.isArrayLike(array2copy[j])  ) {
              
              if(compareArrays(array1[i],array2copy[j])){
                array2copy.splice(j,1);
              }
              
        } else if ( (array1[i] instanceof Date && R.type(array2copy[j]) == "String"
                || R.type(array1[i]) == "String" && array2copy[j] instanceof Date 
                   || array1[i] instanceof Date && array2copy[j] instanceof Date)  ){  

                   var v1=null;
                   if(array1[i] instanceof Date){
                     v1=array1[i].toISOString();
                   } else {
                     v1=array1[i];
                   } 

                   var v2=null;
                   if(array2copy[j] instanceof Date){
                     v2=array2copy[j].toISOString();
                   } else {
                     v2=array2copy[j];
                   }   
                   
              if(v1==v2){
                array2copy.splice(j,1);
              }
              
        } else if (typeof array1[i] == "object" && typeof array2copy[j] == "object") {
              
              if(compareObjects(array1[i],array2copy[j]) ){
                 array2copy.splice(j,1);
              }
              
        } else {
          
          if (array1[i]===array2copy[j]){
           array2copy.splice(j,1); 
          }
          
        }
    }
  }
  
  return array2copy.length==0;
}

console.log(compareObjects(offerA, offerB));
