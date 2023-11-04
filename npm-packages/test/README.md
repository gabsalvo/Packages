# ULTRA BASIC FIRST NPM PACKAGE

This npm package, takes 2 numbers and return its sum!!!! WOW

let's go through the process

## 1. Setup your project

```sh

mkdir my-cool-package
cd my-cool-package
npm init

```

The _npm init_ command will ask you a series of questions (like **package name, version, description, entry point, test command, git repository, keywords, author, license, etc.**) and create a _package.json_ file based on your answers. You can also run **npm init -y** to accept default values and create package.json automatically.

if you dont have node.js and npm, follow this [link](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).

## 2. Write your code

Write the code for your package. Let's say you're making a simple utility to add numbers:

```js
// index.js (this is the main file you specified during npm init)

function addNumbers(a, b) {
  return a + b;
}

module.exports = addNumbers;
```

## 3. Write tests

Writing tests for your package is a key part of the development process. It ensures that your code works as expected and helps prevent future changes from breaking existing functionality.

### 3.1 Install Jest

```sh

npm install --save-dev jest

```

### 3.2 Configure Jest

Create a jest.config.js file at the root of your project with the following contents for more complex configurations:

```js
module.exports = {
  verbose: true,
  // other configuration options
};
```

### 3.3 Set up your tests

Create a test file next to the code that you want to test. By convention, Jest looks for test files with any of the following popular naming conventions:

    Files with .js suffix in __tests__ folders.
    Files with .test.js suffix.
    Files with .spec.js suffix.

For example, if you have a file named _index.js_, you could create a file named _index.test.js_ for your tests.

Let's:

```sh

mkdir __tests__
cd __tests__
touch index.test.js

```

Then we need to configure change a tiny bit the _package.json_ by adding:

```js

"scripts": {
  "test": "jest"
}

```

### 3.4 Write your tests

Here's an example of what your index.test.js might look like:

```js
const addNumbers = require("../index");

test("adds 1 + 2 to be equal 3", () => {
  expect(addNumbers(1, 2)).toBe(3);
});
```

### 3.5 Run your Tests

```sh

npm test

```

#### 3.5.1 Test Coverage (optional)

Jest can also check how much of your code is covered by tests. You can run Jest with the --coverage flag to enable this feature.

```sh

npm test -- --coverage

```

This will create a coverage report in the coverage/ directory of your project, which you can view in your browser.

#### 3.5.2 Continuous Integration (Optional)

You can integrate Jest with continuous integration (CI) systems to run tests automatically when you push code changes. This can be configured using services like GitHub Actions, Travis CI, CircleCI, etc.

For next time 😉

## 4. Document Your Package

Create a README.md file explaining what your package does, how to install it, examples on how to use it, and any other information users might need.

## 5. Publish Your Package

Before publishing, make sure you have an account on [npm](https://www.npmjs.com/signup). Once you have an account and are logged in to npm on your machine **(npm login)**, you can publish your package:

```sh

npm publish

```

This is what you would normally do but we are learning here soooo

**THIS IS WHAT WE ARE GOING TO DO**

Let's change a bit out **package.json** like this:

```js

"name": "package-name",

```

to

```js

"name": "@username/package-name",

```

where _username_ is the one you use to npm login and remember to do the same in the **package-lock.json**

_Finally we can publish using:_

```sh

npm publish --access public

```

## 6. All Done!

[gif](https://media0.giphy.com/media/xT8qBhrlNooHBYR9f2/giphy.gif?cid=ecf05e47773j8zdhibb6bnzz1br90aca5sudct1iqlsc7qie&ep=v1_gifs_search&rid=giphy.gif&ct=g)
