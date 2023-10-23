const breakCaesar = require('./break.ceaser.js')

test('breakes caeser', () => {
    expect(breakCaesar("Mjqqt, btwqi!")).toStrictEqual(5)
    expect(breakCaesar("Gur dhvpx oebja sbk whzcf bire gur ynml qbt.")).toStrictEqual(13);
})