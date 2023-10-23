const code = require('./rot13.js');

test('rot13 test', ()=> {
  expect(code('hello')).toStrictEqual('uryyb');
  expect(code('This is my first ROT13 excercise!')).toStrictEqual('Guvf vf zl svefg EBG13 rkprepvfr!');
  expect(code('ROT13 example.')).toStrictEqual('EBG13 rknzcyr.');
})