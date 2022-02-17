steps:
- uses: actions/checkout@v2
- uses: actions/setup-java@v2
  with:
    distribution: 'temurin'
    java-version: '8'
    cache: 'maven'
- name: Build with Maven
  run: mvn -B package --file pom.xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-war-plugin</artifactId>
    <configuration>
        <webXml>WebContent\WEB-INF\web.xml</webXml>
    </configuration>
</plugin>
