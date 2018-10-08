static int minimumSwaps(int[] arr) {
    int arrLen = arr.length;
    int count = 0;
    int [] sarr = arr.clone();
    Arrays.sort(sarr);
    
    for (int i = 0; i < arrLen; i++) {
        if (arr[i] != sarr[i]) {
            count++;
            for (int j = i + 1; j < arrLen; j++) {
                if (arr[j] == sarr[i] ) {
                    int tmp = arr[j];
                    arr[j] = arr[i];
                    arr[i] = tmp;
                    break;
                }
            }
        }
    }
    return count;
}

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