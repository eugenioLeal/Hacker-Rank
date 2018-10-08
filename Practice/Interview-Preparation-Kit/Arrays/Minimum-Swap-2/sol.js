var unsortedIndexes = new List<int>();
var swapSum = 0;

for(int iterator = 0; iterator < arr.Length; iterator++){
	while(arr[iterator] != iterator + 1){
		var swapKey = arr[iterator] - 1;

		var temp = arr[iterator];

		arr[iterator] = arr[swapKey];
		arr[swapKey] = temp;

		swapSum++;
	}
}

return swapSum;