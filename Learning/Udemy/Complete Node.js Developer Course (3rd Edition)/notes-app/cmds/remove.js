const notes = require('../notes.js');

exports.command = 'remove';

exports.description = 'remove a note';

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
  notes.removeNote(argv.title);
};
