const notes = require('../notes.js');

exports.command = 'update';

exports.description = 'update a new note';

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
  notes.updateNote(argv.title, argv.body);
};
