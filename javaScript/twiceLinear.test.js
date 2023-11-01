const code = require('./twiceLinear.js')

test('returns nth digit of u', () => {
    expect(code(100)).toStrictEqual(447)
    expect(code(4)).toStrictEqual(9)
    expect(code(1028)).toStrictEqual(8769)
    expect(code(12095)).toStrictEqual(204859)
    expect(code(12304095)).toStrictEqual(1316195920)
})