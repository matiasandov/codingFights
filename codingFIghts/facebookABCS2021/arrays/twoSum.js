/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for(let i = 0; i < nums.length; i++){
        //no es necesario empezar desde el cero porque ese ya lo checaste con i
         for(let j = i+1; j < nums.length; j++){
             if((nums[i] + nums[j]) === target ){
                 //solo ocupas indices en un array
                 return [i,j];
             }
        
    }
    }
    
};
