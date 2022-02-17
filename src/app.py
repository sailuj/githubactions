jobs:
  build:
    runs-on: ubuntu-20.04
    strategy:
      matrix:
        java: [ '8', '11', '13', '15' ]
    name: Java ${{ matrix.Java }} sample
    steps:
      - uses: actions/checkout@v2
      - name: Setup java
        uses: actions/setup-java@v2
        with:
          distribution: '<distribution>'
          java-version: ${{ matrix.java }}
      - run: java -cp java HelloWorldApp
