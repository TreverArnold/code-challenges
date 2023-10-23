const code = require('./createPhoneNumber.js')

test('makes a valid phone number', () => {
    expect(code([1, 2, 3, 4, 5, 6, 7, 8, 9, 1])).toBe('(123) 456-7891')
    expect(code([9, 8, 3, 8, 5, 1, 4, 8, 6, 3])).toBe('(983) 851-4863')
})