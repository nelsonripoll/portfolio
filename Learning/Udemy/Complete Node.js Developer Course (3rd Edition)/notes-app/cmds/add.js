const notes = require('../notes.js');

exports.command = 'add';

exports.description = 'add a new note';

exports.builder = (yargs) => {
  return yargs.options({
    title: {
      description: 'the title of the note',
      demandOption: true,
      type: 'string'
    },
    body: {
      description: 'the body of the note',
      demandOption: true,
      type: 'string'
    }
  });
};

exports.handler = (argv) => {
  notes.addNote(argv.title, argv.body);
};
