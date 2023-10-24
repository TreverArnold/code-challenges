function oneTwoThree(n) {
    return n > 8 ? ['9'.repeat(Math.floor(n/9)) + ((n % 9) > 0 ? (n % 9).toString() : ''), '1'.repeat(n)] :
    n > 0 ? [n.toString(), '1'.repeat(n)] : ['0', '0'];
}

module.exports = oneTwoThree