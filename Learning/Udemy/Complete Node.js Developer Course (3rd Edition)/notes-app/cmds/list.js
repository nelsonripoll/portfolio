const notes = require('../notes.js');

exports.command = 'list';

exports.description = 'list notes';

exports.builder = (yargs) => { };

exports.handler = (argv) => {
  notes.listNotes();
};
