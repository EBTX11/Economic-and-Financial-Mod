const fs = require("fs");

//Here you change which languages you want included
const languages = [
  "braz_por",
  "english",
  "french",
  "german",
  "japanese",
  "korean",
  "polish",
  "russian",
  "simp_chinese",
  "spanish",
  "turkish",
];

//Choose source Folder here
const sourceFolder = "english";

/**
 * Transfers the content of the source file to the target language file.
 * @param {string} sourceFile - The path of the source file.
 * @param {string} targetLanguage - The target language for the transfer.
 */
function performTransfer(sourceFile, targetLanguage) {
  const fileName = sourceFile.split("/").pop();
  const targetFileName = fileName.replace(
    `_l_${sourceFolder}`,
    `_l_${targetLanguage}`
  );

  const targetFile = `${targetLanguage}/${targetFileName}`;

  if (fs.existsSync(sourceFile)) {
    const sourceContent = fs.readFileSync(sourceFile, "utf8");
    const languageIdentifier = sourceContent.match(/l_(\w+):/)[1];
    const targetContent = sourceContent.replace(
      new RegExp(`l_${languageIdentifier}:`),
      `l_${targetLanguage}:`
    );
    const contentWithoutBOM = targetContent.replace(/^\ufeff/, "");

    const utf8BOM = "\ufeff" + contentWithoutBOM;
    fs.writeFileSync(targetFile, utf8BOM, "utf8");

    console.log(
      `Successfully transferred the content of "${sourceFile}" to "${targetFile}".`
    );
  } else {
    console.log(`Error: "${sourceFile}" file not found.`);
  }
}

languages.forEach((targetLanguage) => {
  if (fs.existsSync(targetLanguage)) {
    console.log(
      `The "${targetLanguage}" folder already exists. Overwriting...`
    );
  } else {
    fs.mkdirSync(targetLanguage);
    console.log(`Created the "${targetLanguage}" folder.`);
  }

  const files = fs.readdirSync(sourceFolder);
  files.forEach((file) => {
    const sourceFile = `${sourceFolder}/${file}`;
    performTransfer(sourceFile, targetLanguage);
  });
});
