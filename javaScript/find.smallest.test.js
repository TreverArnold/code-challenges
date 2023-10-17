const code = require('./find.smallest.js')

test('returns smallest number possible by moving one digit', () => {
    expect(code(261235)).toStrictEqual([126235, 2, 0])
    expect(code(209917)).toStrictEqual([29917, 0, 1])
})