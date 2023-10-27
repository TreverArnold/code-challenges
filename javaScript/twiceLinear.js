function dblLinear(n) {
    let i = 0, j = 0;
    let resultIndex = 0;
    let result = [1];

    while (resultIndex < n) {
        const x = 2 * result[i] + 1;
        const y = 3 * result[j] + 1;

        if (x <= y) {
            result.push(x);
            i++;
            if (x === y) j++;
        } else {
            result.push(y);
            j++;
        }

        resultIndex++;
    }

    return result[n];
}

module.exports = dblLinear