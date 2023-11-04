const addNumbers = require("../index");

test("adds 1 + 2 to be equal 3", () => {
  expect(addNumbers(1, 2).toBe(3));
});
