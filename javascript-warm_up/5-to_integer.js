#!/usr/bin/node

const args = process.argv.slice(2);

if (isNaN(args[0])) {
    console.log('Not a number');
}

else {
    console.log('My number: ${parseInt(args[0])}');
}

// isNaN is true if args cannot be converted into an integer, stands for : Is Not A Number
// parseInt is to convert args into integer(not exactly but sort of)
// $ so that it doesn't print literally the args but rather the conversion. Used with {}