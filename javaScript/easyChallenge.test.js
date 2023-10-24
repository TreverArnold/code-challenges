const code = require('./easyChallenge.js')

test('does the operation', () => {
    expect(code(0)).toStrictEqual(['0', '0'])
    expect(code(3)).toStrictEqual(['3', '111'])
    expect(code(19)).toStrictEqual(['991', '1111111111111111111'])
})