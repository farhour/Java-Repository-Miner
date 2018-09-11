#!/bin/bash
//usr/bin/env groovy  -cp spoon-core-7.0.0-jar-with-dependencies.jar "$0" "$@"; exit $?
//
@Grab('com.xlson.groovycsv:groovycsv:1.3')
import static com.xlson.groovycsv.CsvParser.parseCsv
import spoon.reflect.declaration.CtMethod;
import spoon.Launcher;
import spoon.processing.AbstractProcessor;

class Lister extends AbstractProcessor<CtMethod> {
  List result=[]
  void process(CtMethod c) {
    result.add(c.getParent().getQualifiedName()+"#"+c.getSignature());
  }
}

String pathToRepo = new File('output/pathToRepo.csv').getText('UTF-8')

inputFileHandler = new File('output/inputForSpoon.csv')
csvContent = inputFileHandler.getText('utf-8')
dataIterator = parseCsv(csvContent, readFirstLine: true)

outputFileHandler = new File("output/outputOfSpoon.csv")
outputFileHandler.write("")
exceptionsFileHandler = new File("output/exceptionsOfSpoon.csv")
exceptionsFileHandler.write("")

for (line in dataIterator) {
  countsOfElements = line.values.size()
  hashOfCommit = line[0]
  command = "git -C $pathToRepo checkout -b _PD $hashOfCommit"
  command.execute().text
  for (int i = 1; i<countsOfElements; i++) {
    outputFileHandler.append(hashOfCommit+'|')
    javaFilePath = line[i]
    outputFileHandler.append(javaFilePath)
    try {
      launcher = new Launcher()
      launcher.addInputResource(pathToRepo+javaFilePath)
      processor = new Lister();
      launcher.addProcessor(processor);
      launcher.getEnvironment().setNoClasspath(true);
      launcher.buildModel();
      launcher.getModel().processWith(processor)
      outputFileHandler.append('|')
      for(javaMethodSign in processor.result) {
        if(javaMethodSign == processor.result.last()) {
          outputFileHandler.append(javaMethodSign)
        }
        else
          outputFileHandler.append(javaMethodSign+'|')
      }
    outputFileHandler.append("\r\n")
    } catch(Exception ex) {
        exceptionsFileHandler.append(hashOfCommit+'|'+javaFilePath)
        exceptionsFileHandler.append("\r\n")
        outputFileHandler.append("\r\n")
    }
  }
  command = "git -C $pathToRepo checkout master"
  command.execute().text
  command = "git -C $pathToRepo branch -d _PD"
  command.execute().text
}
