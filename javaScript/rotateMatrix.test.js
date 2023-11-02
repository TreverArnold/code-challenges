const code = require('./rotateMatrix.js')

test('returns rotated matrix', () => {
  expect(code([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]], 'counter-clockwise')).toStrictEqual([[3, 6, 9], [2, 5, 8], [1, 4, 7]])
  expect(code([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]], 'clockwise')).toStrictEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]])
})