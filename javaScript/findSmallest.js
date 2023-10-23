function smallest(num) {
  let move = [num, 0, 0];
  num = num.toString();
  let smallestNum = num;
  for (let i = 0; i < num.length; i++) {
    for (let j = 0; j <= num.length; j++) {
      let tempNum = num.split('');
      let digit = tempNum.splice(i, 1)[0];
      tempNum.splice(j, 0, digit);

      let currentNum = parseInt(tempNum.join(''));
      if (currentNum < smallestNum) {
        smallestNum = currentNum;
        move = [smallestNum, i, j];
            }
        }
    }
    return move;
}

module.exports = smallest