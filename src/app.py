steps:
- uses: actions/checkout@v2
- uses: actions/setup-java@v2
  with:
    distribution: 'temurin'
    java-version: '11'
    cache: 'maven'
- name: Build with Maven
  run: mvn -B package --file pom.xml
