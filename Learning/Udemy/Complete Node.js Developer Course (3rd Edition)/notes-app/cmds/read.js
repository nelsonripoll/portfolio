const notes = require('../notes.js');

exports.command = 'read';

exports.description = 'read a note';

exports.builder = (yargs) => {
  return yargs.options({
    title: {
      description: 'the title of the note',
      demandOption: true,
      type: 'string'
    }
  });
};

exports.handler = (argv) => {
  notes.readNote(argv.title);
};
