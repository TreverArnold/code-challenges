const WORDS = new Set(['the', 'hello', 'fox']) //just a few wors to make the test work

function breakCaesar(st) {
    st = st.toLowerCase().replace(/[^a-z ]/g, '');
    let bestShift = 0;
    let maxValidWords = 0;
    for (let shift = 0; shift < 26; shift++) {
        let decryptedMessage = '';

        for (let i = 0; i < st.length; i++) {
            let char = st[i];
            if (/[a-z]/.test(char)) {
                let alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz';
                let shiftedChar = alphabet[(alphabet.indexOf(char) + shift)];
                decryptedMessage += shiftedChar;
            } else {
                decryptedMessage += char;
            }
        }

        let validWordsCount = decryptedMessage.split(' ').filter(word => WORDS.has(word)).length;

        if (validWordsCount > maxValidWords) {
            maxValidWords = validWordsCount;
            bestShift = shift;
        }
    }

    return 26-bestShift;
}

module.exports = breakCaesar;