function rot13(str) {
    const alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM';
    let arr = str.split('');
    
    for (let i = 0; i < arr.length; i++) {
      if (alphabet.includes(str[i])) {
        arr[i] = alphabet[alphabet.indexOf(str[i]) + 13];
      }
    }
    
    return arr.join('');
  }

module.exports = rot13;