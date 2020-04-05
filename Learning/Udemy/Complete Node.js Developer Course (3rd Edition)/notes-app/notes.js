const fs = require('fs');
const chalk = require('chalk');
const filename = 'notes.json';

const loadNotes = () => {
  try {
    const buff = fs.readFileSync(filename);
    const data = JSON.parse(buff.toString());

    return data;
  } catch (e) {
    return [];
  }
};

const saveNotes = (notes) => {
  const data = JSON.stringify(notes);
  fs.writeFileSync(filename, data);
};

const logSuccess = (msg) => {
  console.log(chalk.white.bgGreen('SUCCESS') + ' ' + msg);
};

const logError = (msg) => {
  console.log(chalk.white.bgRed('ERROR') + ' ' + msg);
};

const listNotes = () => {
  console.log(chalk.white.bgGreen.bold('LISTING NOTES'));

  const notes = loadNotes();

  const display = (note) => {
    console.log(chalk.bold.underline(note.title));
    console.log(note.body + "\n");
  }

  notes.forEach(display);
};

const addNote = (title, body) => {
  console.log(chalk.white.bgGreen.bold('ADDING NOTE'));

  const notes = loadNotes();

  const duplicateNote = notes.find((note) => note.title === title);

  if (!duplicateNote) {
    notes.push({
      title: title,
      body: body
    });
  
    saveNotes(notes);
    logSuccess('Note successfully added.');
  } else {
    logError('Note could not be added, title already exists.');
  }
};

const readNote = (title) => {
  console.log(chalk.white.bgGreen.bold('READING NOTE'));

  const notes = loadNotes();

  const noteToRead = notes.find((note) => note.title === title);

  if (noteToRead) {
    console.log(chalk.bold.underline(noteToRead.title));
    console.log(noteToRead.body + "\n");
  } else {
    logError('Could not read note, title not found.');
  }
};

const updateNote = (title, body) => {
  console.log(chalk.white.bgGreen.bold('UPDATING NOTE'));

  const notes = loadNotes();

  const noteUpdated = notes.find((note) => {
    var updated = false;

    if (note.title === title) {
      note.body = body;
      updated = true;
    }

    return updated;
  });

  if (noteUpdated) {
    saveNotes(notes);
    logSuccess('Note updated.');
  } else {
    logError('Could not update note, title not found.');
  }
};

const removeNote = (title) => {
  console.log(chalk.white.bgGreen.bold('REMOVE NOTE'));

  const notes = loadNotes();

  const notesToKeep = notes.filter((note) => note.title !== title);

  if (notes.length > notesToKeep.length) {
    saveNotes(notesToKeep);
    logSuccess('Note successfully removed.');
  } else {
    logError('Could not delete note, title not found.');
  }
};

module.exports = {
  listNotes: listNotes,
  addNote: addNote,
  readNote: readNote,
  updateNote: updateNote,
  removeNote: removeNote
};
