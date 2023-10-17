const code = require('./arr.diff.js')

test('finds diff between arrary', () => {
    expect(code([1,2,3], [1,2])).toStrictEqual([3])
})